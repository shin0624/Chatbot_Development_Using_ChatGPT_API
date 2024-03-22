# Chosun_Edu_ChatGPT
OpenAI사의 GPT모델을 활용한 챗봇 개발하기
#VS CODE를 사용한 파이썬 개발 환경 구축
    1. VSCODE설치
    2.파이썬 설치(python.org) + 환경변수(path)체크!
    3. vscode에서 extentions(python, python Extension pack, gitgraph ofr gitlens) 추가
    4. vscode에서 github 계정으로 로그인(연동)
    5. github에서 repository(프로젝트) 생성
    6. vscode에서 "git clone repository"로 5번에서 생성한 프로젝트 내려받기
    7. 가상환경 생성(venv) : 가상환경 구축 참조
    8. vscode에서 select python Interpreter 설정(ctrl+shift+P)->venv

# OPEN ai API사용하기(platform.openai.com)
    1. API 키 발급
    2. 카드등록

# 라이브러리관리
    1. venv
    2. anaconda

# 개발환경구축
python -m venv .\venv

# .\venv\Scripts\activate
pip install openai

# Ctrl + K + F : json파일 이쁘게 정렬