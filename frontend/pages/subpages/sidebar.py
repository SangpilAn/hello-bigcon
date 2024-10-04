# sidebar.py
import streamlit as st

from .widgets import weather, calendar
from .modal import edit_modal
from .modal import logout_modal

def show_sidebar():
  ### 1. 사용자 정보 ###
  st.subheader("{이름}님의 제주도 여행🏝️")
  
  # 1-1. 성별
  if 'gender' in st.session_state:
      st.markdown(f"**성별**: {st.session_state['gender']}")
  else:
      st.warning("성별 정보가 입력되지 않았습니다.")

  # 1-2. 연령대
  if 'age' in st.session_state:
      st.sidebar.markdown(f"**연령대**: {st.session_state['age']}")
  else:
      st.sidebar.warning("연령대 정보가 입력되지 않았습니다.")

  # 1-3. 방문 날짜
  if 'visit_dates' in st.session_state:
    visit_dates_str = f"{st.session_state['visit_dates'][0]} ~ {st.session_state['visit_dates'][1]}"
    st.sidebar.markdown(f"**방문 날짜**: {visit_dates_str}")
  else:
    st.sidebar.warning("날짜 정보가 입력되지 않았습니다.")

  # 1-4. 방문 시간대
  if 'visit_times' in st.session_state:
      st.sidebar.markdown(f"**방문 시간대**: {st.session_state['visit_times']}")
  else:
      st.sidebar.warning("시간대 정보가 입력되지 않았습니다.")

  # 1-5. 방문 지역
  if 'region' in st.session_state:
      st.sidebar.markdown(f"**방문 지역**: {', '.join(st.session_state['region'])}")
  else:
      st.sidebar.warning("지역 정보가 입력되지 않았습니다.")
  
  # 수정하기 버튼
  if st.button("수정하기🖋️",
               type="secondary",
               use_container_width=True):
     edit_modal.show_edit_modal()
  
  st.markdown("<hr>", unsafe_allow_html=True)


  ### 2. 달력 위젯 ###
  calendar.show_calendar()  

  ### 3. 날씨 위젯 ###
  weather.show_weather()

  ### 4. 로그아웃 버튼 ###
  if st.button("로그아웃➡️",
               type='secondary'):
     logout_modal.show_logout_modal()