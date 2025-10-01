import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("💬 AI 聊天助手")

with st.sidebar:
    openai_api_key = st.text_input("請輸入OpenAI API密鑰: ", type="password")
    st.markdown("[獲取OpenAI API密鑰](https://platform.openai.com/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，有什麼可以幫你的嗎？"}]

# 每一條對話的打印
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("請輸入你的OpenAI API密鑰")
        st.stop()
    # 存入用戶輸入的對話
    st.session_state["messages"].append({"role": "human", "content": prompt})
    # 打印用戶輸入的對話
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，請稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)
    msg = {"role": "ai", "content": response}
    # 存入AI傳回的對話
    st.session_state["messages"].append(msg)
    # 打印AI傳回的對話
    st.chat_message("ai").write(response)