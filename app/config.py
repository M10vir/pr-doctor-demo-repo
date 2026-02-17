import os

API_KEY = os.getenv("API_KEY", "")
if not API_KEY:
    raise RuntimeError("API_KEY is missing. Set it via environment variables or a secret manager.")
