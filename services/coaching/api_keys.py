import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

APP_DIR = Path(__file__).resolve().parents[2]
load_dotenv(APP_DIR / ".env")


def get_groq_api_key() -> str:
    key = os.environ.get("GROQ_API_KEY", "").strip()
    if key:
        return key

    try:
        key = st.secrets.get("GROQ_API_KEY", "")
        if key:
            return str(key).strip()
    except Exception:
        pass

    secrets_path = APP_DIR / ".streamlit" / "secrets.toml"
    if secrets_path.is_file():
        try:
            import tomllib

            with secrets_path.open("rb") as f:
                data = tomllib.load(f)
            key = data.get("GROQ_API_KEY", "")
            if key:
                return str(key).strip()
        except Exception:
            pass

    return ""
