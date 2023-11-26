from pydantic import BaseModel
import json

class MyDataModel(BaseModel):
    key: str
    value: str



# Пример словаря данных
data_dict = {'key': 'ww', 'value': 'qa'}

# Преобразование словаря в JSON-строку
# json_data = json.dumps(data_dict, ensure_ascii=False)

# # Парсинг и верификация данных с использованием Pydantic
# try:
#     my_data = MyDataModel.model_validate_json(json_data)
#     print("Parsed Data:", my_data)
# except Exception as e:
#     print("Error:", e)

try:
    # my_data = MyModel.model_validate_json(json_data)
    my_data = MyDataModel.model_validate_json(json.loads(data_dict))
    print("Parsed Data:", my_data)
except Exception as e:
    print("Error:", e)