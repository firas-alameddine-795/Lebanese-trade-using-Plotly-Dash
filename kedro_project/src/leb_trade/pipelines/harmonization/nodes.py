"""Convert HS codes reported under HS 2007/2012/2017 to the original HS 1992 nomenclature."""
from __future__ import annotations

import pandas as pd


def _to_mapping(table: pd.DataFrame) -> dict[int, int]:
    """First column = code in the newer revision ('From'), second = HS92 code ('To')."""
    return dict(zip(table.iloc[:, 0], table.iloc[:, 1]))


def build_conversion_maps(
    hs2007: pd.DataFrame, hs2012: pd.DataFrame, hs2017: pd.DataFrame
) -> dict[str, dict[int, int]]:
    return {"hs2007": _to_mapping(hs2007), "hs2012": _to_mapping(hs2012), "hs2017": _to_mapping(hs2017)}


def convert_to_hs92(
    trade: pd.DataFrame, maps: dict[str, dict[int, int]], periods: list[dict]
) -> pd.DataFrame:
    """Map each row's HS6 code with the table valid for its year.

    Codes absent from a table (e.g. national chapter 98) keep their original value.
    """
    trade = trade.copy()
    new_code = trade["hs6_code"].copy()
    for period in periods:
        mask = trade["year"].between(period["start_year"], period["end_year"])
        mapped = trade.loc[mask, "hs6_code"].map(maps[period["table"]])
        new_code.loc[mask] = mapped.fillna(trade.loc[mask, "hs6_code"])
    trade["hs6_code"] = new_code.astype("int64")

    trade = trade.sort_values(["trade_flow", "year", "country", "hs6_code"]).reset_index(drop=True)
    return trade[
        ["year", "country", "trade_flow", "hs6_code", "trade_value_usd", "trade_value_lbp", "trade_value_kg"]
    ]
