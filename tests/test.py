import csv
import json
path = 'C:/Users/User/Desktop/example.txt'
with open('users.json') as users_file, open('books.csv') as books_file:

    users = json.load(users_file)


    books = []
    for book in csv.reader(books_file):
        books.append({
            'title': book[0],
            'author': book[1],
            'pages': int(book[2]),
            'genre': book[3]
        })


    num_users = len(users)
    num_books = len(books)
    books_per_user = num_books // num_users
    remaining_books = num_books % num_users

    for i in range(num_users):
        start = i * books_per_user
        end = start + books_per_user
        if i < remaining_books:
            end += 1

        users[i]['books'] = books[start:end]


    result = users


with open('result.json', 'w') as result_file:
    json.dump(result, result_file)
