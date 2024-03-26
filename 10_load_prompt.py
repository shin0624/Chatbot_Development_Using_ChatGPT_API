
from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate, ChatPromptTemplate, load_prompt
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

_=load_dotenv(find_dotenv())

prompt = load_prompt("./Lecture/data.json")
# prompt = load_prompt("./data.yaml")yaml파일로 불러오기도 가능

#1.Chat 모델 생성
chat = ChatOpenAI(
    openai_api_key =os.getenv("OPEN_API_KEY") ,# .env에 있는 키를 불러온다-->개인 설정들 숨긴 상태로 작업 가능
    temperature = 0.1,#-->0.1~1.0까지의 값 / 질문 시 0에 가까울 수록 사실기반, 1에가까울수록 창의적인 답을 출력
    streaming = True,#streaming : 답변 생성 과정 시각화 가능
    callbacks = [StreamingStdOutCallbackHandler()]
)

prompt.format(country = "Japan")
