import pandas as pd

from leb_trade.pipelines.ingestion.nodes import clean_numbers, concatenate_yearly_files, to_long_format


def _raw():
    return pd.DataFrame(
        {
            "year": [2011],
            "country": ["France"],
            "hs_code": ["0810.20"],
            "import_lbp": ["2,940,783"], "import_usd": ["1,950"], "import_kg": ["33"],
            "export_lbp": ["0"], "export_usd": ["0"], "export_kg": ["0"],
        },
        dtype="object",
    )


def test_concatenate_orders_partitions_by_name():
    parts = {"b": lambda: pd.DataFrame({"x": [2]}), "a": lambda: pd.DataFrame({"x": [1]})}
    assert concatenate_yearly_files(parts)["x"].tolist() == [1, 2]


def test_to_long_format_has_one_row_per_flow():
    long = to_long_format(_raw())
    assert long["trade_flow"].tolist() == ["import", "export"]
    assert list(long.columns) == ["year", "country", "trade_flow", "hs6_code",
                                  "trade_value_lbp", "trade_value_usd", "trade_value_kg"]
    assert long.loc[0, "trade_value_usd"] == "1,950"


def test_clean_numbers_strips_separators_and_casts():
    clean = clean_numbers(to_long_format(_raw()))
    assert clean.loc[0, "hs6_code"] == 81020
    assert clean.loc[0, "trade_value_lbp"] == 2940783
    assert clean["trade_value_usd"].dtype == "int64"
