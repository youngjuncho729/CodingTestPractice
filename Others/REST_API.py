""""
HTTP Methods: 
  GET -> 특정 데이터 조회 요청
  POST -> 특정 데이터 생성 요청
  PUT -> 특정 데이터 수정 요청
  DELETE -> 특정 데이터 삭제 요청
"""

import requests

target = "http://www.google.com"
responce = requests.get(url=target)
# print(responce.text)

"""
JSON (Javascript Object Notation)
데이터를 주고받는데 사용하는 경량의 데이터 형식
키-값 쌍으로 이루어진 데이터 객체
"""
import json

user = {
  "id": "gildong",
  "password": "12345",
  "age": 30,
  "hobby": ["football", "programming"]
}

# 인코딩: 파이썬 변수를 JSON 객체로 변환(띄어쓰기 4칸 적용)
json_data = json.dumps(user, indent = 4)
#print(json_data)

# 디코딩: JSON 객체를 파이썬 변수로 변환
data = json.loads(json_data)
#print(data)

# JSON 데이터를 변환하여 파일로 저장
"""
with open("user.json", "w", encoding="utf-8") as file:
  json.dump(user, file, indent = 4)
"""

"""
REST (Representational State Protocol) API
REST는 각 자원에 대하여 자원의 상태에 대한 정보를 주고받는 개발방식, 
서버의 자원을 어떠한 방식으로 접근하도록 해야하는지 구체적으로 명시한것이다.
REST API는 REST 아키택쳐를 따르는 API를 의미한다
"""

# JSON Placeholder: http://jsonplaceholder.typicode.com
# 사용자 정보 API 실습

"""
API 호출 경로: http://jsonplaceholder.typicode.com/users
HTTP 메서드: GET
"""

# get the information of id=1 user
target = "http://jsonplaceholder.typicode.com/users/1"
responce = requests.get(target)
print(responce.text)

# get all users information
target = "http://jsonplaceholder.typicode.com/users"
responce = requests.get(target)
print(responce.text)

# 번호 순서대로 이름만 리스트에 담기
data = responce.json()

name_list = []
for user in data:
  name_list.append(user["name"])
print(name_list)