from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

#FewShot Learning : 이전에 학습을 완료한 모델에게 추가 학습을 시킨다.
# - 모델에게 생성하는 대답의 예제를 전달하는 것이 fewshot.
# - 기본적인 messages(system)을 활용한 엔지니어링보다 훨씬 더 강력한 성능을 보임.(대답의 양식을 주는 것으로 생각)
# - 즉, prompt 작성보다 예제를 보여주는 fewshot이 훨씬 더 좋음.
# - 대화 기록 등 DB에서 가져와서 fewshot으로 사용

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

example_prompt = PromptTemplate.from_template(
    "Human : {question}\nAI : {answer}"
)
prompt = FewShotPromptTemplate(
    example_prompt = example_prompt,
    examples = examples,
    suffix = "Human : What do you know about {country}?",#아래에서 사용자가 입력한 country를 괄호에 넣고 질문으로 받아들인다.
    input_variables=["country"],
)

chain = prompt|chat
chain.invoke({
    "country":"japan"
})

