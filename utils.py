from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

# import os
# from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛頓提出過那些知名的定律？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一個問題是什麼？", memory, os.getenv("OPENAI_API_KEY")))