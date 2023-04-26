import csv
import json

from Otus2.files import BOOKS_FILE_PATH, USERS_FILE_PATH


with open(USERS_FILE_PATH) as alfa:
    users = json.load(alfa)


with open(BOOKS_FILE_PATH) as alfa:
    rd = csv.DictReader(alfa)
    books_list = [beta for beta in rd]


num_books = len(books_list)
num_users = len(users)


max_books = num_books // num_users
rem_books = num_books % num_users


distribution = [max_books] * num_users
for c in range(rem_books):
    distribution[c] += 1


book_index = 0
for c, user in enumerate(users):
    user_books = books_list[book_index:book_index + distribution[c]]
    user['books'] = user_books
    book_index += distribution[c]


with open('result.json', 'w') as alfa_out:
    json.dump(users, alfa_out, indent=4)