import json

# 불러온 파일(input_file) -> json_data에 저장 함수
def json_to_dict(input_file):
    # JSON 파일을 딕셔너리로 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    return json_data

def dict_to_json(output_file, data_dict):
    # 딕셔너리를 JSON으로 변환하여 파일로 저장
    # output_file을 w(파일 쓰기 모드)로 열기
    with open(output_file, 'w', encoding='utf-8') as f:
        # 딕셔너리를 JSON 형식으로 파일에 작성
        # json으로 내보낼 객체(data_dict)

        # ensure_ascii=False : 유니코드 문자 -> UTF-8로 인코딩
        # indent : 들여쓰기(4칸)
        json.dump(data_dict, f, ensure_ascii=False, indent=4)

# 저희 데이터 파일(.xlsx)파일 보면 이상치가 있습니다.
# 그 이상치을 제거하는 함수입니다.
def remove_third_key_value(data):
    for item in data:
        del item["Unnamed: 2"]

# 딕셔너리 리스트의 구조 변경(단어, 뜻 부분 제거)
def convert_dictionary_list(dictionary_list):
    # 딕셔너리 구조 변경하여 새로운 리스트에 추가
    new_dictionary_list = []

    for dictionary in dictionary_list:
        new_dictionary = {dictionary["단어"]: dictionary["뜻"]}
        new_dictionary_list.append(new_dictionary)

    return new_dictionary_list


# 입력 파일 경로와 출력 파일 경로
input_file_path = 'db/output2.json'
output_file_path = 'db/wordDB.py'

# JSON 파일을 딕셔너리로 변환
data_dict = json_to_dict(input_file_path)

# 이상치 삭제
remove_third_key_value(data_dict)

new_data_dict = convert_dictionary_list(data_dict)

# 딕셔너리를 JSON으로 변환하여 파일로 저장
dict_to_json(output_file_path, new_data_dict)

