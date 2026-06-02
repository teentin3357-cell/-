import streamlit as st
import google.generativeai as genai

st.title("💖 연애 상담 챗봇")

# API 키 설정 (Streamlit Secrets 사용)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 세션에 대화 기록 저장 공간 만들기
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 보여주기
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력 받기
if prompt := st.chat_input("고민을 말해보세요..."):
    # 1. 유저 메시지 표시 및 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. 챗봇 답변 생성 및 저장
    with st.chat_message("assistant"):
        try:
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash-lite",
                system_instruction="당신은 친절하고 공감 능력이 뛰어난 연애 상담사입니다."
            )
            
            # 이전 대화 기록을 Gemini 형식에 맞게 변환
            history = [{"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} for m in st.session_state.messages[:-1]]
            
            chat = model.start_chat(history=history)
            response = chat.send_message(prompt)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error("오류가 발생했습니다. API 키를 확인해주세요.")
