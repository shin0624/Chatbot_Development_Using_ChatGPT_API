from openai import OpenAI
client = OpenAI(api_key = "")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content":"모든 설명을 3줄로 요약해서 설명해주세요."},
    {"role": "user", "content": ""}]
)
print("\n")
print(completion.choices[0].message)
print("\n")
#openAI의 API를 사용해서 챗봇 문제점
# 1. 개발이 어려움(난이도 상)-->더 쉽게 개발할 수 있는 "?"(프레임워크) 필요
# 2. 챗봇 개발 완성 -->Bard모델 변경 시 -->Bard API 처음부터 개발해야함 --> 프레임워크(LLM) 사용

# --> LangChain 프레임워크(코드는 동일, 모델 바꾸면 자동으로 바꿔짐) --> pip install [라이브러리명]