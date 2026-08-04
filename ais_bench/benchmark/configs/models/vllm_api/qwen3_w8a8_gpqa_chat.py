from ais_bench.benchmark.models import VLLMCustomAPIChat
from ais_bench.benchmark.utils.postprocess.model_postprocessors import (
    extract_non_reasoning_content,
)


models = [
    dict(
        attr="service",
        type=VLLMCustomAPIChat,
        abbr="qwen3-w8a8-gpqa-chat",
        path="/mnt/shared_dir/Qwen3-30B-A3B-W8A8",
        model="qwen3_30B_w8a8",
        stream=False,
        request_rate=0,
        use_timestamp=False,
        retry=2,
        api_key="",
        host_ip="61.28.30.29",
        host_port=8080,
        url="",
        max_out_len=32768,
        batch_size=128,
        trust_remote_code=False,
        generation_kwargs=dict(
            temperature=0.6,
            top_p=0.95,
            repetition_penalty=1.05,
        ),
        pred_postprocessor=dict(type=extract_non_reasoning_content),
    )
]
