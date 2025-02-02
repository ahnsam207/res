import openai
#import os
import json

#openai.api_key = os.environ["OPENAI_API_KEY"]

def get_price_info_temp(product_name):
   # print("함수", product_name)
    price_info = {
        "product_name":product_name,
        "price":"10,000"
    }
    return json.dumps(price_info)  # json 형식으로 데이터 변환

# Chat API에 사용자 입력과 함수 정보를 보내는 함수
def run_conversation_temp(user_query):
    # 사용자 입력
    messages = [{"role" : "user", "content":user_query}]

    # 함수 정보 입력
    functions =[
        { "name":"get_price_info_temp",
          "description":"제품 이름에 따른 가격 가져오기",
          "parameters":{
              "type":"object",
              "properties":{
                  "product_name":{
                      "type":"string",
                      "description":"제품 이름, 예를 들면, 키보드, 마우스",
                  },
              },
              "required":["product_name"],
           },

        }
    ]
    # 1단계 : 사용자 입력과 함수 정보를 Chat API 모델로 보내기
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo", # GPT 모델 선택
        messages = messages, # 전달할 메시지 지정
        functions = functions,
        function_call = "auto"
    )

    # 2단계 : 응답 생성
    response_message = response.choices[0].message # 응답 메시지

    return response_message  # 응답 메시지 반환
user_query = "대한민국의 수도는 어디입니까?"
response_message = run_conversation_temp(user_query)
print(response_message)
#print(json.dumps(response_message, ensure_ascii=False))

