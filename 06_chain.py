from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv

# 1. PromptTemplate : 질문 -> 답변 ->끝(1회성)
#2. ChatPromptTemplate : Chat(채팅처럼)

_=load_dotenv(find_dotenv())#env파일 경로를 찾아 load_dotenv에 전달

#1.Chat 모델 생성
chat = ChatOpenAI(
    openai_api_key =os.getenv("OPEN_API_KEY") ,# .env에 있는 키를 불러온다-->개인 설정들 숨긴 상태로 작업 가능
    temperature = 0.1#-->0.1~1.0까지의 값 / 질문 시 0에 가까울 수록 사실기반, 1에가까울수록 창의적인 답을 출력
)

#2. parser 생성
from langchain.schema import BaseOutputParser
#CommaOutputParser는 BaseOutputParser를 상속받음
class CommaOutputParser(BaseOutputParser) : 
    #self = java의 this와 같음
    #parse : 답변을 받으면 strip으로 좌우여백 제거 후 컴마 기준으로 분할
    def parse(self, text):
        items = text.strip().split(",")
        return list(map(str.strip, items))
    
p = CommaOutputParser()

#3. template 생성
template = ChatPromptTemplate.from_messages([
    ("system", "너는 리스트 생성 기계다. 모든 답변을 콤마로 구분해서 대답해라."),
    ("human", "{question}")
])
#4. chain 생성 - 모든 요소를 합쳐주는 역할, 합쳐진 요소들은 하나의 체인으로 실행(하나하나 순서대로  result를 반환할 때 까지)
#2개 이상의 체인을 연결
#template, chat model, parser 모두 연결
chain = template | chat | CommaOutputParser()
#5. chain 실행(입력 매개변수 : dict 타입 전달)
result = chain.invoke({
    "max_items" : 5,
    "question" : "포켓몬은 무엇인가?"
})
print("\n")
print(result)
print("\n")
