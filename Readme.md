# Development
To serve with 🤗[HuggingFace](https://huggingface.co) models, go to `infer.py` and feel free to modify the commented code.
- check the `Dockerfile` for the intended docker image
- configure `compose.yml` for GPU support if needed

# Launch 🚀
```bash
docker compose up
```

# Request
```bash
# stream outputs
curl -L -d '{"prompt": "FILL YOUR PROMPT HERE"}' localhost:8080/infer
# all at once
curl -d '{"prompt": "FILL YOUR PROMPT HERE"}' localhost:8080/generate
```

# Webpage
There's a chat window @`http://localhost:8080`. Try it out!
