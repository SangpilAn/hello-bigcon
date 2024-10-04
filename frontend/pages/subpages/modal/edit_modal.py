# edit_modal.py
import streamlit as st
import datetime

# sidebar 사용자 정보 수정하기 모달
@st.dialog("여행 정보 수정하기")
def show_edit_modal():
   st.markdown("### 여행 정보를 변경할 수 있습니다.")

   # 성별 수정 (radio button)
   gender = st.radio(
      "성별을 선택해주세요.",
      options=['남성', '여성'],
      index=['남성', '여성'].index(st.session_state.get('gender', '남성'))
   )

   # 연령대 수정 (셀렉트박스)
   age = st.selectbox(
      "연령대를 선택해주세요:",
      options=["10대", "20대", "30대", "40대", "50대", "60대 이상"],
      index=["10대", "20대", "30대", "40대", "50대", "60대 이상"].index(st.session_state.get('age', "20대"))
   )

   # 방문 날짜 수정 (날짜 선택기)
   today = datetime.datetime.now()
   visit_dates = st.date_input(
      "방문 날짜를 선택해주세요:",
      value=st.session_state.get('visit_dates', (today, today + datetime.timedelta(days=7))),
      min_value=today,
      max_value=today.replace(year=today.year + 1),
   )

   # 방문 시간대 수정 (라디오 버튼)
   visit_times = st.radio(
      "방문 시간대를 선택해주세요:",
      options=["아침", "점심", "저녁", "야식", "심야"],
      index=["아침", "점심", "저녁", "야식", "심야"].index(st.session_state.get('visit_times', "아침"))
   )

   # 방문 지역 수정 (멀티셀렉트)
   region = st.multiselect(
      "방문 지역을 선택해주세요:",
      options=["동쪽 제주시", "서쪽 제주시", "동쪽 서귀포시", "서쪽 서귀포시"],
      default=st.session_state.get('region', [])
   )

   # 수정 내용 저장 버튼
   if st.button("수정 내용 저장"):
      # 방문지역 최소 하나 이상 선택하도록 설정
      if not region:
         st.warning("방문 지역을 최소 1개 이상 선택해주세요.")
      else:
         # session_state에 수정된 값 저장
         st.session_state['gender'] = gender
         st.session_state['age'] = age
         st.session_state['visit_dates'] = visit_dates
         st.session_state['visit_times'] = visit_times
         st.session_state['region'] = region

         # 알림 메시지
         st.success("수정된 정보가 저장되었습니다!")
         st.rerun()  # 페이지 새로고침

