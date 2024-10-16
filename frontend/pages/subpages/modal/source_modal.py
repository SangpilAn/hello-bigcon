# source_modal.py
import streamlit as st
import datetime
# 데이터 출처 표기 모달
@st.dialog("데이터 정보는 여기에")
def show_source_modal():
    st.write("이곳에 데이터 출처나 참고문헌(?) etc.를 적을 예정")