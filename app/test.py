import json
from pydantic import BaseModel, Field


class MyDataModel(BaseModel):
    datetime: str
    title: str
    text: str


# Пример словаря данных
data_dict = {'datetime': '27.11.2023 16:23:11.086', 'title': '11', 'text': 'ххХХ цуа Х'}
def qwerty():
    # Преобразование словаря в JSON-строку
    json_data = json.dumps(data_dict, ensure_ascii=False)

    # Парсинг и верификация данных с использованием Pydantic
    try:
        my_data = MyDataModel.model_validate_json(json_data)

        print(my_data.datetime)
        print(my_data.title)
        print(search_char_x(my_data))

    except Exception as e:
        print("Error:", e)



def search_char_x(text):
    my_text = text.text
    search_char = 'х'
    count_x = my_text.upper().count(search_char.upper())
    return count_x

print(qwerty())

# print(search_char_x(qwerty()))


