from typing import Dict, List
from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts.example_selector.base import BaseExampleSelector

_=load_dotenv(find_dotenv())

#1.Chat 모델 생성
chat = ChatOpenAI(
    openai_api_key =os.getenv("OPEN_API_KEY") ,# .env에 있는 키를 불러온다-->개인 설정들 숨긴 상태로 작업 가능
    temperature = 0.1,#-->0.1~1.0까지의 값 / 질문 시 0에 가까울 수록 사실기반, 1에가까울수록 창의적인 답을 출력
    streaming = True,#streaming : 답변 생성 과정 시각화 가능
    callbacks = [StreamingStdOutCallbackHandler()]
)

# fewshot예제
# 질문과 답변의 양상을 보여준다. Q&A챗봇 등에 사용
examples = [
    {
        "question": "What do you know about France?",
        "answer": """       
        Here is what I know:        
        Capital: Paris        
        Language: French        
        Food: Wine and Cheese       
        Currency: Euro        
        """,
    },
    {
        "question": "What do you know about Italy?",
        "answer": """        
        I know this:        
        Capital: Rome        
        Language: Italian        
        Food: Pizza and Pasta       
        Currency: Euro       
        """,
    },
    {
        "question": "What do you know about Greece?",
        "answer": """       
        I know this:        
        Capital: Athens        
        Language: Greek        
        Food: Souvlaki and Feta Cheese       
        Currency: Euro        
        """,
    },
]

# RandomSelector설계
class RandomExampleSelector(BaseExampleSelector) :
    def __init__(self, examples):
        self.examples = examples
        
    def add_example(self, example):
        self.examples.append(example)
        
    def select_examples(self, input_variables):
        from random import choice
        return [choice(self.select_examples)]


# RandomSelector 생성
example_selector = RandomExampleSelector(examples = examples)


example_prompt = PromptTemplate.from_template(
    "Human : {question}\nAI : {answer}"
)
prompt = FewShotPromptTemplate(
    example_prompt = example_prompt,
    # examples = examples  : 전체 예제 모두 활용
    example_selector=example_selector, # 랜덤하게 예제 적용
    suffix = "Human : What do you know about {country}?",#아래에서 사용자가 입력한 country를 괄호에 넣고 질문으로 받아들인다.
    input_variables=["country"],
)

chain = prompt|chat
chain.invoke({
    "country":"japan"
})

