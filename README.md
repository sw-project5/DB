# DB
단어장, 회원(사용자, 관리자) db 코드입니다.

<h1><단어장 DB 구축 방법></h1>

<p>단어장 파일 형식 : .xlsx(엑셀파일) - 데이터 가공 전</p>
<p>(1)xlsx_to_json.py : xlsx 파일 -> json 파일로 변경</p>
<p>(2)json_to_dic.py : json 파일 -> dic 파일로 변경</p>

---
(1) xlsx_to_json

<img width="160" alt="스크린샷 2024-05-11 00 51 29" src="https://github.com/sw-project5/DB/assets/160165670/3876721a-d39c-4a6b-8c22-48a950c3e820">
<p>↓</p>
<img width="155" alt="스크린샷 2024-05-11 00 50 59" src="https://github.com/sw-project5/DB/assets/160165670/cdb217d1-a66c-4922-8f24-44c1d400f121">

<p>output_json.json 파일 생성</p>

---
(2) json_to_dic

<img width="155" alt="스크린샷 2024-05-11 00 50 59" src="https://github.com/sw-project5/DB/assets/160165670/cdb217d1-a66c-4922-8f24-44c1d400f121">
<p>↓</p>
<img width="159" alt="스크린샷 2024-05-11 00 56 20" src="https://github.com/sw-project5/DB/assets/160165670/8dcab5f2-8316-4d08-9c40-99bad84633ee">

<p>wordDB.py 파일 생성</p>
