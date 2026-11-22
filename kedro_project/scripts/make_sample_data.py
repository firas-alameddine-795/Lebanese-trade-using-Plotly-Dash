"""Generate a small SYNTHETIC dataset with the same schema as the private customs files.

The real Lebanese customs workbooks are not redistributable, so this writes made-up numbers
(fixed seed) in the exact layout the pipeline expects, so `kedro run --env sample` works
from a fresh clone.  Nothing here reflects real trade flows.

    python scripts/make_sample_data.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "data" / "sample"
YEARS = range(2011, 2020)

# HS6 codes as reported by customs ("dddd.dd"), with their OEC-style names.
PRODUCTS = {
    "010110": "Pure-bred breeding horses",
    "020110": "Bovine carcasses, fresh or chilled",
    "080810": "Apples, fresh",
    "080520": "Mandarins and similar citrus, fresh",
    "100190": "Wheat, other than durum",
    "151110": "Palm oil, crude",
    "170199": "Refined sugar",
    "220421": "Wine in containers of 2 litres or less",
    "271019": "Medium petroleum oils",
    "300490": "Medicaments, retail packs",
    "392690": "Other articles of plastics",
    "620342": "Men's cotton trousers",
    "710239": "Diamonds, worked",
    "710812": "Gold, unwrought",
    "720890": "Flat-rolled iron, hot-rolled",
    "731815": "Screws and bolts, iron or steel",
    "841510": "Air conditioning machines",
    "851712": "Mobile telephones",
    "870323": "Cars, 1500-3000 cc",
    "940360": "Wooden furniture",
}
# Codes the customs data use after a revision; the WCO table maps them back to the HS92 code.
RENAMED = {"851713": "851712", "300491": "300490"}  # HS2012+/HS2017 spellings -> HS92
NATIONAL = {"980100": "Used furniture and household appliances"}  # chapter 98: no HS92 mapping
COUNTRIES = {
    "France": "Europe", "Germany": "Europe", "Italy": "Europe", "Turkey": "Middle east",
    "Egypt": "Arab States", "Saudi Arabia": "Middle east", "United Arab Emirates": "Middle east",
    "China": "Asia", "India": "Asia", "United States": "North America", "Brazil": "Latin America",
    "Ghana": "Africa", "Bahrain": "Arab States", "Free Zone": None,
}


def _fmt(n: float) -> str:
    return f"{int(round(n)):,}"


def make_yearly(rng: np.random.Generator) -> None:
    (OUT / "yearly").mkdir(parents=True, exist_ok=True)
    for year in YEARS:
        rows = []
        codes = list(PRODUCTS) + list(NATIONAL)
        if year >= 2012:   # revised nomenclature appears
            codes = [RENAMED.get(c, c) if c in ("851712", "300490") else c for c in codes]
        for country in COUNTRIES:
            for code in rng.choice(codes, size=rng.integers(8, 14), replace=False):
                def flow(scale):
                    if rng.random() < 0.45:
                        return 0, 0, 0
                    kg = rng.lognormal(mean=scale, sigma=1.2)
                    usd = kg * rng.uniform(0.5, 6) * (1 + 0.03 * (year - 2011))
                    return usd * 1500, usd, kg
                imp, exp = flow(10.5), flow(9)
                if not any(imp) and not any(exp):
                    imp = flow(10)
                    if not any(imp):
                        continue
                rows.append({
                    "year": year, "country": country, "hs_code": f"{code[:4]}.{code[4:]}",
                    "import_lbp": _fmt(imp[0]), "import_usd": _fmt(imp[1]), "import_kg": _fmt(imp[2]),
                    "export_lbp": _fmt(exp[0]), "export_usd": _fmt(exp[1]), "export_kg": _fmt(exp[2]),
                })
        pd.DataFrame(rows).to_excel(OUT / "yearly" / f"lebanese customs yearly HS6 {year}.xlsx", index=False)


def make_reference() -> None:
    ref = OUT / "reference"
    ref.mkdir(parents=True, exist_ok=True)
    identity = {int(c): int(c) for c in PRODUCTS}
    hs2007 = pd.DataFrame({"From": list(identity), "To": list(identity)})
    hs2012 = pd.DataFrame({"From": [int(k) for k in RENAMED] + list(identity),
                           "To": [int(v) for v in RENAMED.values()] + list(identity)})
    hs2017 = hs2012.copy()
    for name, table in [("2007", hs2007), ("2012", hs2012), ("2017", hs2017)]:
        table.to_excel(ref / f"HS {name} to HS 1992 Correlation and conversion tables.xlsx", index=False)

    names = {int(c): n for c, n in PRODUCTS.items()}
    for code, name in PRODUCTS.items():  # headings (HS4) and chapters (HS2) get a name too
        names.setdefault(int(code) // 100, name.split(",")[0])
        names.setdefault(int(code) // 10000, name.split(",")[0])
    products = pd.DataFrame({"hs92": list(names), "name": list(names.values())})
    sections = pd.DataFrame({"section": ["I", "II", "IV", "V", "VI", "VII", "XI", "XIV", "XV", "XVI", "XVII", "XX", "XXI"],
                             "name": ["Live animals", "Vegetable products", "Prepared foodstuffs", "Mineral products", "Chemicals",
                                      "Plastics and rubber", "Textiles", "Precious stones and metals",
                                      "Base metals", "Machinery and electrical", "Vehicles", "Miscellaneous", "Works of art; national codes"]})
    with pd.ExcelWriter(ref / "products_hs_92.xlsx") as xl:
        products.to_excel(xl, sheet_name="products_hs_92", index=False)
        sections.to_excel(xl, sheet_name="sections", index=False)
    regions = pd.DataFrame({"Country": [c for c, r in COUNTRIES.items() if r],
                            "Region": [r for r in COUNTRIES.values() if r]})
    regions.to_excel(ref / "country to region.xlsx", index=False)


if __name__ == "__main__":
    make_yearly(np.random.default_rng(42))
    make_reference()
    print(f"Sample data written to {OUT}")
