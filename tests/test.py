import csv
import json

from Otus2.files import BOOKS_FILE_PATH

books = BOOKS_FILE_PATH

books_file = open('books.csv')
users_file = open('users.json')
result_file = open('result.json')


books = csv.DictReader(books_file)
users = json.load(users_file)


result_list = []


for user in users:

    user_dict = {
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': []
    }


    for book in books_reader:

        if book['author_id'] == user['id']:
            user_dict['books'].append({
                'title': book['title'],
                'author': book['author'],
                'pages': int(book['pages']),
                'genre': book['genre']
            })

    result_list.append(user_dict)

    books_file.seek(0)
    books_reader = csv.DictReader(books_file)


json.dump(result_list, result_file)



