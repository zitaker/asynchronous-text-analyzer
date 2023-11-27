import json
from pydantic import BaseModel, Field


class MyDataModel(BaseModel):
    datetime: str
    title: str
    text: str

# class TranslationStrInInt():
#     text: int = Field(alias="count_x_in_text")


    # @pydantic.root_validator(pre=True, allow_reuse=True)
    # def convert_text_to_count_x_in_text(cls, values):
    #     text_value = values.get('text')
    #     if text_value is not None:
    #         values['count_x_in_text'] = int(text_value)
    #     return values

    # class Config:
    #     populate_by_name = True



# Пример словаря данных
data_dict = {'datetime': '27.11.2023 16:23:11.086', 'title': '11', 'text': 'ххХХ цуа Х'}
def qwerty():
    # Преобразование словаря в JSON-строку
    json_data = json.dumps(data_dict, ensure_ascii=False)

    # Парсинг и верификация данных с использованием Pydantic
    try:
        my_data = MyDataModel.model_validate_json(json_data)
        # print(get_key_and_value('title', my_data)[1])
        # return my_data

        # some_model = MyDataModel(datetime=my_data.datetime, title=my_data.title, text=search_char_x(my_data))
        some_model = MyDataModel(datetime=my_data.datetime, title=my_data.title, text='qw2')
        print(some_model)
        print(some_model.model_dump_json(by_alias=True))
    except Exception as e:
        print("Error:", e)


# def get_key_and_value(name_key, data):
#     key = name_key
#     value = getattr(data, key)
#     return key, value

print(qwerty())

def search_char_x(text):
    my_text = text.search_char_x
    search_char = 'х'
    count_x = my_text.upper().count(search_char.upper())
    return count_x

# print(search_char_x(qwerty()))


# class SomeModel(BaseModel):
#     attr1: str = Field(alias="attr_1")
#     attr2: str = Field(alias="attr_2")
#     attr3: str = Field(alias="attr_3")
#
#     class Config:
#         populate_by_name = True
#
#
# some_model = SomeModel(attr1="someText", attr2="someText", attr3="someText")
# print(some_model)  # attr1='someText' attr2='someText' attr3='someText'
# print(some_model.model_dump_json(by_alias=True))  # {"attr_1": "someText", "attr_2": "someText", "attr_3": "someText"}
