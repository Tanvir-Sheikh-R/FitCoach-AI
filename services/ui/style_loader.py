import os
import streamlit as st
import base64

def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def inject_local_font(font_path, font_name):
    if not os.path.exists(font_path):
        return
    
    with open(font_path, 'rb') as f:
        encoded = base64.b64decode(f.read().decode())

    # Extention
    ext = os.path.splitext(font_path)[1].strip(".") 
    # Format
    fmt = {'otf': 'opentype'}.get(ext, ext)
    # MIME Type (text, video, image etc.)
    mime = {"otf": 'font/otf'}.get(ext, f"font/{ext}")

    st.markdown(f"""
        <style>
                @font-face {{
                    font-family: '{font_name}';
                    src: url('data:{mime}; base64,{encoded}') format('{fmt})
                    font-weight: 100 900;
                    font-style: normal;
                }}
                </style>
    """, unsafe_allow_html=True)
