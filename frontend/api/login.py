# login.py
import streamlit as st
import streamlit.components.v1 as components
import requests

# https://developers.google.com/identity/gsi/web/reference/js-reference#google.accounts.id.renderButton
# google cloud id
client_id = "CLIENT_ID_HERE"

# 로그인 URL
SPRING_LOGIN_URL = "http://<AWS주소>/api/login"

# streamlit 세션 상태 초기화 (로그인 여부)
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# 로그인 함수
# def login_with_google():
#   try:
#     # POST 요청
#     response = requests.post(SPRING_SERVER_URL, json={})

#     # 응답 처리
#     if response.status_code == 200:
#       st.success("---- Successfully logged innn!")
#       # 서버에서 받은 인증 정보를 활용하여 세션 상태 업데이트
#       st.session_state['auth_token'] = response.json().get('auth_token', None)
#       return True
#     else:
#       st.error(f"---- Failed to login. Status code: {response.status_code}")
#       return False
#   except Exception as e:
#     st.error(f"---- error occurred during login: {e}")
#     return False


# 구글 로그인 버튼 렌더링 함수 >> 자바스크립트 사용
def render_google_login_button():
    # Google 로그인 버튼 렌더링 & Spring API로 POST 요청 보냄
    components.html(f"""
        <script src="https://accounts.google.com/gsi/client" async defer></script>
        
        <!-- Google Sign-In Button -->
        <div id="g_id_onload"
             data-client_id="{client_id}"
             data-context="signin"
             data-ux_mode="popup"
             data-auto_prompt="false"
             data-callback="handleCredentialResponse">
        </div>
        
        <!-- 버튼 디자인 옵션 -->
        <div class="g_id_signin"
             data-text="sign_in_with"
             data-logo_alignment="center">
        </div>

        <script>
            // 인증 성공 시 호출되는 콜백 함수
            function handleCredentialResponse(response) {{
                const credential = response.credential;             // JWT ID Token
                console.log("Encoded JWT ID token: " + credential);

                // 인증 정보를 Spring 서버로 POST 요청 보내기
                const loginUrl = "{SPRING_LOGIN_URL}";
                
                fetch(loginUrl, {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json',
                    }},
                    body: JSON.stringify({{ credential: credential }}),
                }})
                .then(response => response.json())
                .then(data => {{
                    if (data.success) {{
                        alert("successfully logged in");
                    }} else {{
                        alert("failed to login: " + data.message);
                    }}
                }})
                .catch(error => {{
                    console.error("에러 발생:", error);
                }});
            }}
        </script>
    """, height=300)