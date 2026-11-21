"""Project-level checks: the registered pipelines are wired consistently."""
from pathlib import Path

from kedro.framework.project import pipelines
from kedro.framework.startup import bootstrap_project


def test_pipelines_are_registered():
    bootstrap_project(Path.cwd())
    assert {"ingestion", "harmonization", "enrichment", "__default__"} <= set(pipelines)


def test_default_pipeline_ends_in_trade_master():
    bootstrap_project(Path.cwd())
    assert "trade_master" in pipelines["__default__"].outputs()
