from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean_numbers, concatenate_yearly_files, to_long_format

NAMESPACE = "data_processing.ingestion"


def create_pipeline(**kwargs) -> Pipeline:
    """Yearly workbooks -> one clean long table.

    Intermediate datasets (`trade_concat`, `trade_long`) are prefixed with the namespace;
    the catalog entries listed in `inputs` / `outputs` keep their global names.
    """
    return pipeline(
        [
            node(
                concatenate_yearly_files,
                inputs="raw_yearly_trade",
                outputs="trade_concat",
                name="concatenate_yearly_files"
            ),
            node(to_long_format, inputs="trade_concat", outputs="trade_long", name="to_long_format"),
            node(clean_numbers, inputs="trade_long", outputs="trade_clean", name="clean_numbers"),
        ],
        inputs={"raw_yearly_trade"},
        outputs={"trade_clean"},
        namespace=NAMESPACE,
        tags=["data_processing", "ingestion"],
    )
