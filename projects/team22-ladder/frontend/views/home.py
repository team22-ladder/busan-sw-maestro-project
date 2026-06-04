import streamlit as st


def render():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center'>냉장고털이</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#6b7280;font-size:1.1em'>냉장고 속 재료로 만들 수 있는 레시피를 찾아드려요</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    for col, step_num, title, desc in [
        (col1, "1", "재료 입력", "사진 또는 텍스트로\n냉장고 속 재료를 입력해요"),
        (col2, "2", "재료 보강", "소스·조리도구·추가 재료를\n선택해요"),
        (col3, "3", "레시피 추천", "AI가 추천하는\n레시피를 확인해요"),
    ]:
        with col:
            st.markdown(
                f"""<div style='text-align:center;padding:24px;border:1px solid #e5e7eb;border-radius:12px'>
                <div style='font-size:1.4em;font-weight:bold;color:#3b82f6;margin-bottom:8px'>{step_num}</div>
                <div style='font-weight:bold;margin-bottom:4px'>{title}</div>
                <div style='color:#6b7280;font-size:0.9em'>{desc}</div>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    _, c, _ = st.columns([2, 3, 2])
    if c.button("시작하기", type="primary", use_container_width=True):
        st.session_state.step = 1
        st.rerun()
