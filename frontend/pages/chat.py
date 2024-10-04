# mainpage.py
import streamlit as st
from pages.subpages import sidebar

# 페이지 제목 설정
st.set_page_config(page_title="main", page_icon="💬", layout="wide",
                   initial_sidebar_state='expanded')

# CSS 파일 불러오기
with open('style/chat_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    sidebar.show_sidebar()

# tabs
tab1, tab2, tab3 = st.tabs(['Chat', 'Maps', 'Trends'])
with tab1:
    st.write("tab1 here")
with tab2:
    st.write("tab2 here")
with tab3:
    st.write("tab3 here")
