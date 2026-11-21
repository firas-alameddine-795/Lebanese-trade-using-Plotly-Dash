"""Add the HS hierarchy, human-readable descriptions and world regions."""
from __future__ import annotations

import pandas as pd

MASTER_COLUMNS = [
    "year", "region", "country", "trade_flow",
    "hs1_code", "hs1_desc", "hs2_code", "hs2_desc", "hs4_code", "hs4_desc", "hs6_code", "hs6_desc",
    "trade_value_usd", "trade_value_lbp", "trade_value_kg",
]


def add_hs_hierarchy(trade: pd.DataFrame, hs_sections: dict[str, list[int]]) -> pd.DataFrame:
    """HS2 (chapter) and HS4 (heading) come from the HS6 digits; HS1 (section) from the chapter."""
    chapter_to_section = {chapter: section for section, chapters in hs_sections.items() for chapter in chapters}
    trade = trade.copy()
    trade["hs4_code"] = trade["hs6_code"] // 100
    trade["hs2_code"] = trade["hs6_code"] // 10000
    trade["hs1_code"] = trade["hs2_code"].map(chapter_to_section)
    return trade


def add_hs_descriptions(
    trade: pd.DataFrame,
    products: pd.DataFrame,
    sections: pd.DataFrame,
    missing_hs6_desc: dict[int, str],
    missing_hs4_desc: dict[int, str],
    fallback_hs2_desc: str,
) -> pd.DataFrame:
    """Descriptions from the OEC tables, with manual text for national codes."""
    names = dict(zip(products["hs92"], products["name"]))
    section_names = dict(zip(sections["section"], sections["name"]))

    trade = trade.copy()
    trade["hs6_desc"] = trade["hs6_code"].map(names).fillna(trade["hs6_code"].map(missing_hs6_desc))
    trade["hs4_desc"] = trade["hs4_code"].map(names).fillna(trade["hs4_code"].map(missing_hs4_desc))
    trade["hs2_desc"] = trade["hs2_code"].map(names).fillna(fallback_hs2_desc)
    trade["hs1_desc"] = trade["hs1_code"].map(section_names)
    return trade


def add_regions(trade: pd.DataFrame, country_regions: pd.DataFrame, regions: dict) -> pd.DataFrame:
    """Attach a world region to every country, applying the manual corrections from parameters."""
    mapping = {}
    for country, region in zip(country_regions["Country"], country_regions["Region"]):
        mapping[country] = regions["country_overrides"].get(country, regions["region_overrides"].get(region, region))

    trade = trade.copy()
    trade["region"] = trade["country"].map(mapping).fillna(trade["country"].map(regions["manual_fills"]))
    return trade[MASTER_COLUMNS]
