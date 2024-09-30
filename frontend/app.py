# app.py
import streamlit as st
# test

# 페이지 제목 설정
st.set_page_config(page_title="시작 페이지", page_icon=":🍊:", layout="wide",
                   initial_sidebar_state='collapsed')

# 사이드바 가림
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""", unsafe_allow_html=True,)

# CSS 파일 불러오기
with open('style/start_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 이미지 변수 선언
titleImgPath = 'https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/title.png'
botImgPath = 'https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang.png'


# 타이틀 이미지
titleImg = (f"""
<div class=titleImg>
    <img src="{titleImgPath}" alt="title image" width="10%">
</div>
""")
st.markdown(titleImg, unsafe_allow_html=True)

st.caption("🚀 caption을 작성하는 부분")
st.markdown("<hr>", unsafe_allow_html=True)

# 말풍선
st.markdown(f"""
    <div class="chat-container">
        <img src="{botImgPath}" class="chat-icon" alt="chatbot">
        <div class="chat-bubble">
            <div class="chat-text">
                hihi.<br>
                서비스를 소개하는 말
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 긴 말풍선 테스트
textTest = "추가적인 설명은 여기에" * 15
st.markdown(f"""
    <div class="chat-container">
        <img src={botImgPath} class="chat-icon" alt="chatbot">
        <div class="chat-bubble">
            <div class="chat-text">
                {textTest}
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# 시작하기 버튼 (or 로그인 버튼)
st.write("")

start_button = st.page_link("pages/survey.py",
                              label="✈️시작하기🚢")

