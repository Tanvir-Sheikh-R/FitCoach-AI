from functools import lru_cache
from io import BytesIO

from gtts import gTTS


@lru_cache(maxsize=64)
def _synthesize(text: str, lang: str) -> bytes:
    buffer = BytesIO()
    gTTS(text=text, lang=lang).write_to_fp(buffer)
    buffer.seek(0)
    return buffer.read()


class TextToSpeech:
    def speak(self, text, lang="en"):
        cleaned = (text or "").strip()
        if not cleaned:
            return None

        try:
            return _synthesize(cleaned, lang)
        except Exception:
            return None