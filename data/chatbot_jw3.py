# 오류 발생시 재시도 횟수 터미널에 출력하는 코드 추가
import streamlit as st
import google.generativeai as genai

# API 키설정
API_KEY = 'AIzaSyDHXL0nieSrOKcWtoepxOfMAN6RdTK7jNQ'
genai.configure(api_key=API_KEY)

# 모델 설정
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="Chat like You're my very close friend.")
chat = model.start_chat(history=[])

# Streamlit UI 재구성
st.title("jw 연습용 챗봇2 - 입력창 위치 변경")

if 'history' not in st.session_state:
    st.session_state.history = []    
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""   

def send_message():
    user_input = st.session_state.user_input
    if user_input:
        if user_input:
            for i in range(5):
                try:
                    response = chat.send_message(user_input)
                except:
                    print(1)
                    continue
                else:
                    break
        response = chat.send_message(user_input)
        reply = response.text.replace("\n\n", "\n").strip()
        st.session_state.history.append(f"You: {user_input}")
        st.session_state.history.append(f"Gemini: {reply}")
        st.session_state.user_input = ""  # 입력 필드 초기화

# 대화 기록 출력
for line in st.session_state.history:
    st.write(line)

# user input
st.text_input("You :", key='user_input', on_change=send_message)