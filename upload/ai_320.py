import openai
import os

def summarize_text(user_text, lang="en"):
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key

    if lang == "en":
        messages = [
            {"role" : "system", "content" : "You are a helpful assistant in the summary."},
            {"role" : "user", "content" : f"Summarize the following. \n {user_text}"}
        ]
    elif lang == "ko":
        messages = [
            {"role" : "system", "content" : "You are a helpful assistant in the summary."},
            {"role" : "user", "content" : f"Summarize the following in korea. \n {user_text}"}
        ]
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo", # GPT 모델 선택
        messages = messages, # 전달할 메시지 지정
        temperature = 0.8, # 완성의 다양성을 조절하는 온도 설정
        max_tokens = 2000, # 응답 최대 토큰 수 지정
        n=1 # 응답 개수 지정
    )
# assistant_reply = response.choices[0].message.content
# print(assistant_reply)
    summary = response.choices[0].message.content
    return summary


from PyPDF2 import PdfReader
import tiktoken

pdf_file = 'streamlit.pdf'
reader = PdfReader(pdf_file)
page = reader.pages[0]
print("page_num", len(reader.pages))
page_text = page.extract_text()
summary = summarize_text(page_text, "ko")
print(page_text)
print("#" * 50)
print(summary)