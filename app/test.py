from pydantic import BaseModel
import json

class MyDataModel(BaseModel):
    key: str
    value: str
    datetime: str



# Пример словаря данных
data_dict = {'key': 'ww', 'value': 'qa', 'datetime': '27.11.2023 16:23:11.086'}

# Преобразование словаря в JSON-строку
json_data = json.dumps(data_dict, ensure_ascii=False)

# Парсинг и верификация данных с использованием Pydantic
try:
    my_data = MyDataModel.model_validate_json(json_data)
    print("Parsed Data:", my_data)
except Exception as e:
    print("Error:", e)

