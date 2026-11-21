from kedro.pipeline import Pipeline, node, pipeline

from .nodes import add_hs_descriptions, add_hs_hierarchy, add_regions

NAMESPACE = "data_processing.enrichment"


def create_pipeline(**kwargs) -> Pipeline:
    """Add HS hierarchy, descriptions and regions (`trade_hs92` -> `trade_master`)."""
    return pipeline(
        [
            node(
                add_hs_hierarchy,
                inputs=["trade_hs92", "params:hs_sections"],
                outputs="trade_hierarchy",
                name="add_hs_hierarchy",
            ),
            node(
                add_hs_descriptions,
                inputs=[
                    "trade_hierarchy",
                    "hs92_products",
                    "hs92_sections",
                    "params:missing_hs6_desc",
                    "params:missing_hs4_desc",
                    "params:fallback_hs2_desc",
                ],
                outputs="trade_described",
                name="add_hs_descriptions"
            ),
            node(
                add_regions,
                inputs=["trade_described", "country_regions", "params:regions"],
                outputs="trade_master",
                name="add_regions"
            ),
        ],
        inputs={"trade_hs92", "hs92_products", "hs92_sections", "country_regions"},
        outputs={"trade_master"},
        parameters={"hs_sections", "missing_hs6_desc", "missing_hs4_desc", "fallback_hs2_desc", "regions"},
        namespace=NAMESPACE,
        tags=["data_processing", "enrichment"],
    )
