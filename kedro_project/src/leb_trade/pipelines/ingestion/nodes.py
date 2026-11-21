"""Nodes that turn the yearly Lebanese Customs spreadsheets into one clean long table."""
from __future__ import annotations

from typing import Callable

import pandas as pd

TRADE_COLUMNS = ["value_lbp", "value_usd", "kg"]
NUMERIC_COLUMNS = ["hs6_code", "trade_value_lbp", "trade_value_usd", "trade_value_kg"]


def concatenate_yearly_files(partitions: dict[str, Callable[[], pd.DataFrame]]) -> pd.DataFrame:
    """Load every yearly spreadsheet (in filename order) and stack them."""
    frames = [load() for _, load in sorted(partitions.items())]
    return pd.concat(frames, ignore_index=True)


def to_long_format(df: pd.DataFrame) -> pd.DataFrame:
    """One row per (year, country, HS6 code, trade flow) instead of separate import/export columns."""
    df = df.rename(columns={"hs_code": "hs6_code"})
    flows = []
    for flow in ("import", "export"):
        part = df[["year", "country", "hs6_code", *[f"{flow}_{c.split('_')[-1]}" for c in TRADE_COLUMNS]]].copy()
        part.columns = ["year", "country", "hs6_code", "trade_value_lbp", "trade_value_usd", "trade_value_kg"]
        part.insert(2, "trade_flow", flow)
        flows.append(part)
    return pd.concat(flows, ignore_index=True)


def clean_numbers(df: pd.DataFrame) -> pd.DataFrame:
    """Strip thousand separators / dots from the text columns and cast them to integers."""
    df = df.copy()
    df["year"] = df["year"].astype("int64")
    df["hs6_code"] = df["hs6_code"].astype(str).str.replace(".", "", regex=False).astype("int64")
    for col in ("trade_value_lbp", "trade_value_usd", "trade_value_kg"):
        df[col] = df[col].astype(str).str.replace(",", "", regex=False).astype("int64")
    return df
