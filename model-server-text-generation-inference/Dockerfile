FROM ghcr.io/huggingface/text-generation-inference:0.9 

ENV MODEL="/content/saved-model"
ENV PORT=8080
ENV PATH="$PATH:/content/bin"

WORKDIR /content
RUN mkdir -p /content/src /content/bin /content/model-saved

COPY bin/ bin/

CMD --model-id /content/model-saved --num-shard 1
EXPOSE $PORT
