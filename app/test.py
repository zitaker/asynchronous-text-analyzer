from constants import BOOKS


def create_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    list_books = file_contents.split('\n\n\n\n\n\n')
#
    dictionary = []
    for elems in list_books:

        lines = elems.split('\n')

        title1 = lines[0].strip()
        title = title1.replace('\ufeff', '')

        body2 = '\n'.join(lines[1:]).strip()
        body1 = body2.replace('\xa0', ' ')
        body = body1.replace('\n', ' ')

        data = {"title": title, "text": body}

        dictionary.append(data)
    return dictionary




print(create_dictionary(BOOKS))