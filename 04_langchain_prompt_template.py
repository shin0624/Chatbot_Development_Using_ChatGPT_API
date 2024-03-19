from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv


# 1. PromptTemplate : 질문 -> 답변 ->끝(1회성)
#2. ChatPromptTemplate : Chat(채팅처럼)

_=load_dotenv(find_dotenv())#env파일 경로를 찾아 load_dotenv에 전달

chat = ChatOpenAI(
    # .env에 있는 키를 불러온다-->개인 설정들 숨긴 상태로 작업 가능
    openai_api_key =os.getenv("OPEN_API_KEY") ,
    #-->0.1~1.0까지의 값 / 질문 시 0에 가까울 수록 사실기반, 1에가까울수록 창의적인 답을 출력
    temperature = 0.1
    
    
)
template = ChatPromptTemplate.from_messages( [
  ("system",   SystemMessage(content = "너는 탐험가야. 너는 모든 답변을 {language}로 해야해.")),
     ("ai", AIMessage(content = "Hello, Im {name}")),
     ("human", HumanMessage(content = "{country_a}과 {country_b}의 거리는 얼마인가요? 너의 이름은 무엇이니?")),
    
])
prompt = template.format_messages(
    language = "Greek",
    name = "Socrates",
    country_a = "Mexico",
    country_b = "Thailand"
)
print("\n")
print(chat.predict_messages(prompt))
print("\n")