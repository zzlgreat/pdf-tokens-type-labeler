from huggingface_hub import hf_hub_download

import config

pdf_tokens_type_model = hf_hub_download(
    repo_id="HURIDOCS/pdf-segmetation",
    filename="pdf_tokens_type.model",
    revision="9c6dd557abf29e683854178d39c790e33de84c2f",
    cache_dir=config.HUGGINGFACE_PATH,
)

token_type_finding_config_path = hf_hub_download(
    repo_id="HURIDOCS/pdf-segmetation",
    filename="tag_type_finding_model_config.txt",
    revision="7d98776dd34acb2fe3a06495c82e64b9c84bdc16",
    cache_dir=config.HUGGINGFACE_PATH,
)

letter_corpus_path = hf_hub_download(
    repo_id="HURIDOCS/pdf-segmetation",
    filename="letter_corpus.txt",
    revision="da00a69c8d6a84493712e819580c0148757f466c",
    cache_dir=config.HUGGINGFACE_PATH,
)
