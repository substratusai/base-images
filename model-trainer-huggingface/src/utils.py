import typing
import inspect
import json

from transformers import TrainingArguments


def parse_training_args(params: typing.Mapping) -> TrainingArguments:
    typed_params = dict(
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        warmup_steps=2,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=1,
        output_dir="/content/model/checkpoints",
        optim="paged_adamw_32bit",
    )

    training_parameters = inspect.signature(TrainingArguments.__init__).parameters
    for k, v in training_parameters.items():
        if k in params:
            val = params.get(k)
            if v.annotation == bool:
                # https://stackoverflow.com/questions/715417/converting-from-a-string-to-boolean-in-python
                val = json.loads(str(val).lower())
            if v.annotation == str:
                val = str(val)
            if v.annotation == int:
                val = int(val)
            if v.annotation == float:
                val = float(val)
            typed_params[k] = val

    args = TrainingArguments(**typed_params)

    return args
