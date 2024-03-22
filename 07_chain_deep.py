from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

# 1. PromptTemplate : 질문 -> 답변 ->끝(1회성)
#2. ChatPromptTemplate : Chat(채팅처럼)

_=load_dotenv(find_dotenv())#env파일 경로를 찾아 load_dotenv에 전달

#1.Chat 모델 생성
chat = ChatOpenAI(
    openai_api_key =os.getenv("OPEN_API_KEY") ,# .env에 있는 키를 불러온다-->개인 설정들 숨긴 상태로 작업 가능
    temperature = 0.1,#-->0.1~1.0까지의 값 / 질문 시 0에 가까울 수록 사실기반, 1에가까울수록 창의적인 답을 출력
    streaming = True,#streaming : 답변 생성 과정 시각화 가능
    callbacks = [StreamingStdOutCallbackHandler()]
)


# chain 1 생성(=>음식 종류?)
chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 전 세계에서 유명한 요리사입니다. 찾기 쉬운 재료를 사용해서 모든 종류의 요리에 대해 쉽게 따라할 수 있는 레시피를 만드세요."),
    ("human", "나는 {cook} 요리를 만들고 싶어요!")
])
chef_chain = chef_prompt | chat


# chain 2 생성(=>recipe)
veg_chef_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 전통적인 요리법을 채식으로 만드는 채식주의 요리사입니다. 대체 재료를 찾고 그 준비과정을 설명하세요. 근본적으로 레시피를 수정하지는 말고, 대체재료가 없는 경우 없다고 하세요."),
    ("human", "{recipe}")
])
veg_chain = veg_chef_prompt| chat


#chain 3 생성(연결)
final_chain = {"recipe" : chef_chain} | veg_chain
#-->chain 1이 먼저 실행 되고 그 결과를 chain2에 넘긴다.

#chain 실행
final_chain.invoke({
    #chef_chain의 입력값
    "cook":"indian"
})


