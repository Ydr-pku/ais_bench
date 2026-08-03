from ais_bench.benchmark.models import VLLMCustomAPIChat
from ais_bench.benchmark.utils.postprocess.model_postprocessors import (
    extract_non_reasoning_content,
)


models = [
    dict(
        attr="service",
        type=VLLMCustomAPIChat,
        abbr="qwen3-5-gpqa-chat",
        path="/home/y00906461/models/Qwen3.5-35B-A3B",
        model="qwen3_5",
        stream=False,
        request_rate=0,
        use_timestamp=False,
        retry=2,
        api_key="",
        host_ip="",
        host_port=8080,
        url="",
        max_out_len=32768,
        batch_size=32,
        trust_remote_code=False,
        generation_kwargs=dict(
            temperature=1.0,
            top_p=0.95,
            top_k=20,
            chat_template_kwargs={"enable_thinking": True},
        ),
        pred_postprocessor=dict(type=extract_non_reasoning_content),
    )
]
