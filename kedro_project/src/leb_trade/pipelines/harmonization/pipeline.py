from kedro.pipeline import Pipeline, node, pipeline

from .nodes import build_conversion_maps, convert_to_hs92

NAMESPACE = "data_processing.harmonization"


def create_pipeline(**kwargs) -> Pipeline:
    """Convert HS 2007/2012/2017 codes to HS 1992 (`trade_clean` -> `trade_hs92`)."""
    return pipeline(
        [
            node(
                build_conversion_maps,
                inputs=["hs2007_to_hs92", "hs2012_to_hs92", "hs2017_to_hs92"],
                outputs="hs_conversion_maps",
                name="build_conversion_maps"
            ),
            node(
                convert_to_hs92,
                inputs=["trade_clean", "hs_conversion_maps", "params:hs_conversion_periods"],
                outputs="trade_hs92",
                name="convert_to_hs92",
            ),
        ],
        inputs={"trade_clean", "hs2007_to_hs92", "hs2012_to_hs92", "hs2017_to_hs92"},
        outputs={"trade_hs92"},
        parameters={"hs_conversion_periods"},
        namespace=NAMESPACE,
        tags=["data_processing", "harmonization"],
    )
