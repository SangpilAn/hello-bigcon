# mainpage.py
import streamlit as st
import streamlit.components.v1 as components

# 페이지 제목 설정
st.set_page_config(page_title="main", page_icon="🤖", layout="wide",
                   initial_sidebar_state='expanded')

# CSS 파일 불러오기
with open('style/main_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    # 날씨 위젯
    components.html("""
        <div id="ww_9fca590b9f788" v='1.3' loc='id' a='{"t":"horizontal","lang":"ko","sl_lpl":1,"ids":["wl7477"],
                    "font":"Malgun Gothic","sl_ics":"one_a","sl_sot":"celsius","cl_bkg":"#FFFFFF","cl_font":"#000000",
                    "cl_cloud":"#d4d4d4","cl_persp":"#2196F3","cl_sun":"#FFC107","cl_moon":"#FFC107","cl_thund":"#FF5722"}'
                    style="border-radius: 15px; overflow: hidden;">
        More forecasts:
        <a href="https://oneweather.org/seoul/30_days/" id="ww_9fca590b9f788_u" target="_blank">Seoul 30 day forecast</a>
        </div>
        <script async src="https://app3.weatherwidget.org/js/?id=ww_9fca590b9f788"></script>
        """,
        height=280)

