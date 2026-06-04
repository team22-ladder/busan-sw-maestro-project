import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from views import step1, step2, step3, home

st.set_page_config(
    page_title="냉장고털이",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화
defaults = {
    "step": 0,
    "ingredients": [],
    "sauces": [],
    "tools": [],
    "extra_ingredients": [],
    "recipes": {},
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

STEPS = [home, step1, step2, step3]

# 상단 헤더
col_logo, col_progress = st.columns([1, 4])
with col_logo:
    if st.button("🧊 냉장고털이", key="home_btn", help="홈으로"):
        for k in ["ingredients", "sauces", "tools", "extra_ingredients", "recipes"]:
            st.session_state[k] = [] if k != "recipes" else {}
        st.session_state.step = 0
        st.rerun()

with col_progress:
    if st.session_state.step > 0:
        labels = ["재료 입력", "재료 보강", "레시피 결과"]
        prog_cols = col_progress.columns(3)
        for i, (pcol, label) in enumerate(zip(prog_cols, labels)):
            step_num = i + 1
            if step_num < st.session_state.step:
                pcol.markdown(f"<div style='text-align:center;color:#6ee7b7;font-size:0.85em'>✓ {label}</div>", unsafe_allow_html=True)
            elif step_num == st.session_state.step:
                pcol.markdown(f"<div style='text-align:center;color:#3b82f6;font-weight:bold;font-size:0.9em'>▶ {label}</div>", unsafe_allow_html=True)
            else:
                pcol.markdown(f"<div style='text-align:center;color:#9ca3af;font-size:0.85em'>{label}</div>", unsafe_allow_html=True)

st.markdown("<hr style='margin:8px 0 20px'>", unsafe_allow_html=True)

STEPS[st.session_state.step].render()
