import pandas as pd
import pytest

from leb_trade.dashboard import create_app, figures
from leb_trade.dashboard.callbacks import is_root


@pytest.fixture
def trade():
    rows = []
    for year in (2014, 2019):
        for flow in ("import", "export"):
            for region, country in (("Europe", "France"), ("Africa", "Egypt")):
                rows.append({"year": year, "trade_flow": flow, "region": region, "country": country,
                             "hs1_desc": "S", "hs2_desc": "C", "hs4_desc": "H", "hs6_desc": f"P{year}{country}",
                             "trade_value_usd": 100 * (year - 2013)})
    return pd.DataFrame(rows)


@pytest.mark.parametrize("data", [None, {}, {"points": []}, {"points": [{"percentRoot": 1, "label": "x"}]},
                                  {"points": [{"label": ""}]}])
def test_is_root_true_cases(data):
    assert is_root(data)


def test_is_root_handles_missing_percent_root():
    # the path-bar click that used to raise KeyError('percentRoot')
    assert not is_root({"points": [{"label": "Africa"}]})
    assert not is_root({"points": [{"label": "Africa", "percentRoot": 0.3}]})


def test_figures_return_plotly_figures(trade):
    assert figures.create_time_series(trade, "export").data
    assert figures.create_products_treemap(trade, "export", "All years", 2).data
    assert figures.create_countries_treemap(trade, "import", 2019).data
    assert figures.build_diff_treemap_countries(trade, [2014, 2019], "export").data


def test_app_registers_all_callbacks(trade):
    app = create_app(trade)
    assert len(app.callback_map) >= 14
