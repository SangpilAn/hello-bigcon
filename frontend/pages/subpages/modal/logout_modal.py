# logout_modal.py
import streamlit as st

# 수정하기 모달
@st.dialog("로그아웃 하시겠습니까?")
def show_logout_modal():
  st.write("이 자리에 로그아웃 버튼")