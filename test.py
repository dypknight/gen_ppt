CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server \
    --model /mnt/data-nas/diaoyapeng/level_single_token/Qwen3-VL-8B-Instruct \
    --served-model-name Qwen3-VL-8B-Instruct \
    --port 8001 \
    --host 0.0.0.0 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.9