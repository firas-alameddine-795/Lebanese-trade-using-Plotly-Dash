import pandas as pd

from leb_trade.pipelines.harmonization.nodes import build_conversion_maps, convert_to_hs92

PERIODS = [
    {"start_year": 2011, "end_year": 2011, "table": "hs2007"},
    {"start_year": 2012, "end_year": 2016, "table": "hs2012"},
    {"start_year": 2017, "end_year": 2019, "table": "hs2017"},
]


def _trade():
    return pd.DataFrame(
        {
            "year": [2011, 2014, 2018, 2018],
            "country": ["A", "A", "A", "A"],
            "trade_flow": ["import"] * 4,
            "hs6_code": [100, 100, 100, 980100],  # 980100: national code, in no table
            "trade_value_usd": [1, 2, 3, 4], "trade_value_lbp": [1, 2, 3, 4], "trade_value_kg": [1, 2, 3, 4],
        }
    )


def test_each_year_uses_its_own_table_and_unmapped_codes_are_kept():
    maps = build_conversion_maps(
        pd.DataFrame({"From": [100], "To": [11]}),
        pd.DataFrame({"From": [100], "To": [12]}),
        pd.DataFrame({"From HS 2017": [100], "To HS 1992": [17]}),
    )
    out = convert_to_hs92(_trade(), maps, PERIODS)
    by_year = out.groupby("year")["hs6_code"].apply(list).to_dict()
    assert by_year == {2011: [11], 2014: [12], 2018: [17, 980100]}
    assert out["hs6_code"].dtype == "int64"
