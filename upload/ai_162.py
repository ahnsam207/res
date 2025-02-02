import openai
import os

api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = api_key

def response_from_ChatAI(user_content, r_num = 1):
    messages = [
        {"role": "user", "content": user_content}
    ]

    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo", # GPT 모델 선택
        messages = messages, # 전달할 메시지 지정
        temperature = 0.8, # 완성의 다양성을 조절하는 온도 설정
        max_tokens = 1000, # 응답 최대 토큰 수 지정
        n=r_num # 응답 개수 지정
    )

    assistant_replies = []

    for choice in response.choices:
        assistant_replies.append(choice.message.content)

    return assistant_replies

resp = response_from_ChatAI("대한민국 헌법 제1조 1항은?")

print(resp)