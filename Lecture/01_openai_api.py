# OPEN ai API사용하기(platform.openai.com)
# 1. API 키 발급
# 2. 카드등록

#라이브러리관리
# 1. venv
# 2. anaconda
#개발환경구축
#python -m venv .\venv
# .\venv\Scripts\activate
#pip install openai
from openai import OpenAI
client = OpenAI(api_key = "")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content":""},
    {"role": "user", "content": "클라우드 설명해줘"}
  ]
)

print(completion.choices[0].message)
