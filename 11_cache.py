from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

# Caching을 사용하는 이유?
# --> LLM모델의 생성된 답변을 저장할 수 있음
# --> 반복된 동일한 질문이 계속되면 새로 생성하지 않고 Cache에 저장한 내용을 재사용
# --> 금전적으로 효율
set_llm_cache(InMemoryCache) # 메모리에 저장됨(휘발성)
set_llm_cache(SQLiteCache("cache.db"))


_=load_dotenv(find_dotenv())

#1.Chat 모델 생성
chat = ChatOpenAI(
    openai_api_key =os.getenv("OPEN_API_KEY") ,# .env에 있는 키를 불러온다-->개인 설정들 숨긴 상태로 작업 가능
    temperature = 0.1,#-->0.1~1.0까지의 값 / 질문 시 0에 가까울 수록 사실기반, 1에가까울수록 창의적인 답을 출력
    streaming = True,#streaming : 답변 생성 과정 시각화 가능
    callbacks = [StreamingStdOutCallbackHandler()]
)

chat.predict("한국인은 돈까스를 어떻게 만드나요?")