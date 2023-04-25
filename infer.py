from typing import Iterable
# from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
# from threading import Thread
# tok = AutoTokenizer.from_pretrained("gpt2")
# model = AutoModelForCausalLM.from_pretrained("gpt2")


def generate(prompt: str) -> Iterable[str]:
    # inputs = tok([prompt], return_tensors="pt")
    # streamer = TextIteratorStreamer(tok)
    # generation_kwargs = dict(inputs, streamer=streamer, max_new_tokens=20)
    # thread = Thread(target=model.generate, kwargs=generation_kwargs)
    # thread.start()
    # for o in streamer:
    #     yield o
    # return
    for dummy_output in prompt:
        yield dummy_output
