# survey.py: 사용자 질문 페이지
import streamlit as st
import datetime, time

# 이미지 변수 선언
botImgPath = 'https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang2.png'

# 페이지 제목 설정
st.set_page_config(page_title="survey", page_icon=":clipboard:", layout="wide",
                   initial_sidebar_state='collapsed')

# 사이드바 가림
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""", unsafe_allow_html=True)

# CSS 파일 불러오기
with open('style/survey_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 페이지 내용
st.title("📋시작 하기 전에")
st.caption("🚀 caption을 작성하는 부분")

##### progress bar #####
if 'percent_complete' not in st.session_state:
    st.session_state['percent_complete'] = 0

progressText = f"진행중.. {st.session_state['percent_complete']}%"
progress = st.progress(st.session_state['percent_complete'])
progress.progress(st.session_state['percent_complete'], text=progressText)

st.divider()
st.write(" ")

########################
##### 질문 0) 이름 #####
st.markdown(f"""
    <div class="chat-container">
        <img src="{botImgPath}" class="chat-icon" alt="chatbot">
        <div class="chat-bubble">
            <div class="chat-text">
            Hi there🖐️! 안녕하세요.<br>
            <strong class="title_text">친절한 제주도°C</strong> 입니다.<br>
            사용자의 <strong>이름</strong>을 알려주세요.   
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if 'user_name' not in st.session_state:
    # 이름 입력 필드 추가
    user_name = st.text_input("이름을 입력해주세요",
                              placeholder="이름을 입력해주세요", 
                              key='user_name_input',
                              label_visibility='hidden')
    
    if user_name:
        st.session_state['user_name'] = user_name
        st.rerun()

else:
    # 사용자의 대답
    st.markdown(f"""
    <div class="user-chat-container">
        <div class="chat-bubble">
            <div class="user-chat-text">
                {st.session_state['user_name']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    ########################
    ##### 질문 1) 성별 #####
    st.markdown(f"""
        <div class="chat-container">
            <img src="{botImgPath}" class="chat-icon" alt="chatbot">
            <div class="chat-bubble">
                <div class="chat-text">
                반갑습니다, <strong>{st.session_state['user_name']}</strong>님!<br>
                5가지 질문이 있습니다. <br>
                우선, <strong>성별</strong>을 선택해주세요.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    def onClick(selection_input):
        st.session_state['gender'] = selection_input
        st.session_state['percent_complete'] += 20         # progres bar +20

    if 'gender' not in st.session_state:
        with col1:
            selected = st.button('남성', on_click=onClick, args=('남성',), use_container_width=True)
        with col2: 
            selected = st.button('여성', on_click=onClick, args=('여성',), use_container_width=True)
    else: 
        # progress bar 변경
        progress.progress(st.session_state['percent_complete'], text=progressText)
        # 선택한 성별 출력
        st.markdown(f"""
        <div class="user-chat-container">
                <div class="chat-bubble">
                    <div class="user-chat-text">
                        {st.session_state['gender']}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        ##########################
        ##### 질문 2) 연령대 #####
        time.sleep(1)  # 성별 대답 후 잠시 대기
        st.markdown(f"""
            <br>
            <div class="chat-container">
                <img src="{botImgPath}" class="chat-icon" alt="chatbot">
                <div class="chat-bubble">
                    <div class="chat-text">
                        <strong>{st.session_state['gender']}</strong>을 선택하셨습니다. <br>
                        다음 질문입니다. <br>
                        사용자의 <strong>연령대</strong>를 선택해주세요.
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 연령대 selectbox
        if 'age' not in st.session_state:
            st.write("")
            st.divider()        
            age = st.selectbox("연령대를 선택해주세요", 
                            ("연령대를 선택해주세요", "10대", "20대", "30대", "40대", "50대", "60대 이상"), 
                            key="age_select", label_visibility="collapsed")
            
            if age != "연령대를 선택해주세요":              # 사용자가 나이를 선택하면
                st.session_state['age'] = age               # 선택된 값을 session_state에 저장
                st.session_state['percent_complete'] += 20  # progress bar + 20

                # 선택 후 selectbox를 숨기기 위해 'age'를 세션에 저장한 후 refresh
                st.rerun()

        else:
            # progress bar 상태 갱신
            progress.progress(st.session_state['percent_complete'], text=progressText)

            # 선택된 연령대 출력
            st.markdown(f"""
                <div class="user-chat-container">
                    <div class="chat-bubble">
                        <div class="user-chat-text">
                            {st.session_state['age']}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            ############################
            ##### 질문 3) 방문날짜 #####
            time.sleep(1)                   # 연령대 대답 후 잠시 대기
            st.markdown(f"""
                <br>
                <div class="chat-container">
                    <img src="{botImgPath}" class="chat-icon" alt="chatbot">
                    <div class="chat-bubble">
                        <div class="chat-text">
                        <strong>{st.session_state['age']}</strong>를 선택하셨습니다. <br>
                        다음 질문입니다. <br>
                        제주도를 언제 방문하실 계획인가요? <br>
                        <strong>제주도를 방문할 날짜를 선택</strong>해주세요.
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # 날짜 변수
            today = datetime.datetime.now()
            one_week_later = today + datetime.timedelta(days=7)

            if 'visit_dates' not in st.session_state:
                st.divider()
                # 날짜 선택 (기본값은 현재 날짜 ~ 일주일 후)
                visit_dates = st.date_input(
                    "제주도 방문일 선택",
                    value=(today, one_week_later),                       # 날짜 기본값
                    min_value=today,                                     # 선택 가능 최소 날짜: 오늘
                    max_value=today.replace(year=today.year + 1),        # 선택 가능 최대 날짜: 일년 후
                    format="YYYY-MM-DD",
                    label_visibility='collapsed'
                )
                confirm_button1 = st.button("확인")

                # 확인 버튼을 눌렀을 때만 세션에 저장하고, progress bar 갱신
                if confirm_button1:
                    st.session_state['visit_dates'] = visit_dates
                    st.session_state['percent_complete'] += 20
                    st.rerun()

            # 사용자가 날짜 선택 후 확인 버튼을 누른 경우에만 선택한 날짜 출력
            else:
                # progress bar 상태 갱신
                progress.progress(st.session_state['percent_complete'], text=progressText)

                # 선택된 방문 날짜 출력
                st.write("")
                st.markdown(f"""
                    <div class="user-chat-container">
                        <div class="chat-bubble">
                            <div class="user-chat-text">
                            {st.session_state['visit_dates'][0]}부터 {st.session_state['visit_dates'][1]}까지
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                ###############################
                ##### 질문 4) 방문 시간대 #####
                time.sleep(1)
                st.markdown(f"""
                    <br>
                    <div class="chat-container">
                        <img src="{botImgPath}" class="chat-icon" alt="chatbot">
                        <div class="chat-bubble">
                            <div class="chat-text">
                            방문 날짜를 선택하셨습니다. <br>
                            다음 질문입니다. <br>
                            맛집에 <strong>언제 방문하실 계획</strong>인가요? <br>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                # visit_times 값이 세션에 없을 때만 radio buttons 렌더링
                if 'visit_times' not in st.session_state:
                    # 방문 시간대 선택 (single select)
                    st.write("")
                    st.divider()
                    visit_times = st.radio(
                        "방문 시간대 선택",
                        options=["아침", "점심", "저녁", "야식", "심야"],
                        index=0,                        # 기본값은 첫 번째 항목으로 (아침)
                        label_visibility='collapsed'
                    )
                    confirm_button2 = st.button('확인')
                
                    if confirm_button2:
                        st.session_state['visit_times'] = visit_times
                        st.session_state['percent_complete'] += 20
                        st.rerun()
                
                # 사용자가 방문 시간대를 선택하고 확인 버튼을 누른 경우에만 선택한 시간대 출력
                else:
                    # progress bar 상태 갱신
                    progress.progress(st.session_state['percent_complete'], text=progressText)

                    # 선택된 방문 시간대 출력
                    st.markdown(f"""
                        <div class="user-chat-container">
                            <div class="chat-bubble">
                                <div class="user-chat-text">
                                {st.session_state['visit_times']}
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)


                    #############################
                    ##### 질문 5) 방문 지역 #####
                    time.sleep(1)
                    st.markdown(f"""
                        <br>
                        <div class="chat-container">
                            <img src="{botImgPath}" class="chat-icon" alt="chatbot">
                            <div class="chat-bubble">
                                <div class="chat-text">
                                <strong>{st.session_state['visit_times']}</strong>을(를) 선택하셨습니다. <br>
                                마지막 질문입니다. <br>
                                제주도 <strong>어느 지역의 맛집</strong>을 찾으시나요? <br>
                                <strong>하나 이상</strong> 선택할 수 있습니다.<br>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                    # 'region' 값이 세션에 없을 때만 multiselect 렌더링
                    if 'region' not in st.session_state:
                        # 지역 선택 (multiselect)
                        st.write("")
                        st.divider()
                        visit_region = st.multiselect(
                            "제주도 방문 지역 선택",
                            options=["제주시 서부 (애월읍, 한림읍, 한경면)", "제주시 (제주시)", "제주시 동부 (조천읍, 구좌읍)",
                                    "서귀포시 서부 (대정읍, 안덕면)", "서귀포시 (중문, 서귀포시)", "서귀포시 동부 (남원읍, 표선면, 성산읍)"],
                            default=None,
                            label_visibility='collapsed'
                        )
                        confirm_button3 = st.button('확인')

                        # 사용자가 확인 버튼을 눌렀을 때만 세션에 저장하고, progress bar 갱신 및 새로고침
                        if confirm_button3 and visit_region:
                            st.session_state['region'] = visit_region
                            st.session_state['percent_complete'] += 20
                            st.rerun()
                    # 사용자가 방문 지역을 선택하고 확인 버튼을 누른 경우에만 선택한 지역 출력
                    else:
                        # progress bar 상태 갱신
                        progressText = f"{st.session_state['percent_complete']}% ! 모든 질문이 끝났습니다"
                        progress.progress(st.session_state['percent_complete'], text=progressText)

                        # 선택된 방문 지역 출력
                        st.markdown(f"""
                            <div class="user-chat-container">
                                <div class="chat-bubble">
                                    <div class="user-chat-text">
                                    {', '.join(st.session_state['region'])}
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                        time.sleep(1)
                        st.markdown(f"""
                            <br>
                            <div class="chat-container">
                                <img src="{botImgPath}" class="chat-icon" alt="chatbot">
                                <div class="chat-bubble">
                                    <div class="chat-text">
                                    감사합니다.🙇‍♂️ <br>
                                    제주도 맛집을 찾기 위한 모든 질문이 끝났습니다. <br>
                                    <strong>다음 페이지로 넘어가주세요</strong>.
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                        # 시작하기 버튼 (or 로그인 버튼)
                        st.write("")
                        start_button = st.page_link("pages/chat.py",
                                                    label="**다음으로👉**"
                                                    )

