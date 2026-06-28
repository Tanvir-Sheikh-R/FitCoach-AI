import base64
import time

import streamlit as st
import streamlit.components.v1 as components


def estimate_mp3_duration_seconds(audio_bytes: bytes) -> float:
    # gTTS MP3 is roughly 16–20 kbps for short phrases.
    if not audio_bytes:
        return 0.0
    return max(2.5, len(audio_bytes) / 3500)


def is_audio_playing() -> bool:
    return time.time() < st.session_state.get("audio_playback_until", 0)


def queue_coach_audio(audio_bytes: bytes, text: str = "") -> None:
    if not audio_bytes:
        return

    if "coach_audio_queue" not in st.session_state:
        st.session_state.coach_audio_queue = []

    st.session_state.coach_audio_queue.append(
        {"bytes": audio_bytes, "text": text or ""}
    )


def render_coach_audio() -> None:
    if is_audio_playing():
        return

    queue = st.session_state.get("coach_audio_queue") or []
    if not queue:
        return

    clip = queue.pop(0)
    st.session_state.coach_audio_queue = queue

    audio_bytes = clip["bytes"]
    duration = estimate_mp3_duration_seconds(audio_bytes)
    st.session_state.audio_playback_until = time.time() + duration + 0.35

    if clip.get("text"):
        st.session_state.coach_feedback = clip["text"]

    b64 = base64.b64encode(audio_bytes).decode("ascii")
    components.html(
        f"""
        <audio id="fitcoach-audio" autoplay playsinline>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3" />
        </audio>
        <script>
            const audio = document.getElementById("fitcoach-audio");
            if (audio) {{
                audio.play().catch(function () {{}});
            }}
        </script>
        """,
        height=0,
    )
