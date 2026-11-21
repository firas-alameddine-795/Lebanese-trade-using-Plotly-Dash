import pandas as pd

from leb_trade.pipelines.enrichment.nodes import add_hs_descriptions, add_hs_hierarchy, add_regions

SECTIONS = {"I": [1, 2], "XXI": [97, 98]}


def _trade(codes, countries=("Lebanon",)):
    n = len(codes)
    return pd.DataFrame(
        {"year": [2015] * n, "country": list(countries) * n if len(countries) == 1 else list(countries),
         "trade_flow": ["export"] * n, "hs6_code": codes,
         "trade_value_usd": [1] * n, "trade_value_lbp": [1] * n, "trade_value_kg": [1] * n}
    )


def test_hierarchy_digits_and_sections():
    out = add_hs_hierarchy(_trade([10110, 980100]), SECTIONS)
    assert out["hs2_code"].tolist() == [1, 98]
    assert out["hs4_code"].tolist() == [101, 9801]
    assert out["hs1_code"].tolist() == ["I", "XXI"]


def test_descriptions_fall_back_to_manual_text_for_national_codes():
    trade = add_hs_hierarchy(_trade([10110, 980100]), SECTIONS)
    products = pd.DataFrame({"hs92": [1, 101, 10110], "name": ["Animals", "Horses", "Pure-bred horses"]})
    sections = pd.DataFrame({"section": ["I", "XXI"], "name": ["Live animals", "Misc"]})
    out = add_hs_descriptions(trade, products, sections, {980100: "Used furniture"}, {9801: "Used furniture"}, "Fallback")
    assert out["hs6_desc"].tolist() == ["Pure-bred horses", "Used furniture"]
    assert out["hs2_desc"].tolist() == ["Animals", "Fallback"]
    assert out["hs1_desc"].tolist() == ["Live animals", "Misc"]


def test_regions_apply_overrides_and_manual_fills():
    trade = add_hs_descriptions(
        add_hs_hierarchy(_trade([10110] * 4, ["Bahrain", "Egypt", "Kuwait", "Ivory Coast"]), SECTIONS),
        pd.DataFrame({"hs92": [1, 101, 10110], "name": ["a", "b", "c"]}),
        pd.DataFrame({"section": ["I"], "name": ["s"]}), {}, {}, "x",
    )
    table = pd.DataFrame({"Country": ["Bahrain", "Egypt", "Kuwait"],
                          "Region": ["Arab States", "Arab States", "Middle east"]})
    regions = {"country_overrides": {"Bahrain": "Middle east"}, "region_overrides": {"Arab States": "Africa"},
               "manual_fills": {"Ivory Coast": "Africa"}}
    out = add_regions(trade, table, regions)
    assert out["region"].tolist() == ["Middle east", "Africa", "Middle east", "Africa"]
