from ais_bench.benchmark.models import VLLMCustomAPIChat
from ais_bench.benchmark.utils.postprocess.model_postprocessors import (
    extract_non_reasoning_content,
)


models = [
    dict(
        attr="service",
        type=VLLMCustomAPIChat,
        abbr="qwen3-gpqa-chat",
        path="/home/y00906461/models/Qwen3-30B-A3B-Instruct-2507",
        model="qwen3_30B",
        stream=False,
        request_rate=0,
        use_timestamp=False,
        retry=2,
        api_key="",
        host_ip="61.28.30.29",
        host_port=8080,
        url="",
        max_out_len=16384,
        batch_size=32,
        trust_remote_code=False,
        generation_kwargs=dict(
            temperature=0.7,
            top_p=0.8,
            top_k=20,
            min_p=0,
        ),
        pred_postprocessor=dict(type=extract_non_reasoning_content),
    )
]
