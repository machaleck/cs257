'''
    api.py
    Jeff Ondich, 25 April 2016
    Updated 8 November 2021

    Tiny Flask API to support the tiny books web application.
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@api.route('/states/') 
def get_states():
    ''' Returns a list of all the states in our database.

        By default, the list is presented in alphabetical order
        by state name.

            http://.../states/

        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT states.id, states.name
               FROM states ORDER BY states.name'''

    state_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            state = {'name':row[1]}
            state_list.append(state)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(state_list)
get_states()
# @api.route('/books/author/<author_id>')
# def get_books_for_author(author_id):
#     query = '''SELECT books.id, books.title, books.publication_year
#                FROM books, authors, books_authors
#                WHERE books.id = books_authors.book_id
#                  AND authors.id = books_authors.author_id
#                  AND authors.id = %s
#                ORDER BY books.publication_year'''
#     book_list = []
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         cursor.execute(query, (author_id,))
#         for row in cursor:
#             book = {'id':row[0], 'title':row[1], 'publication_year':row[2]}
#             book_list.append(book)
#         cursor.close()
#         connection.close()
#     except Exception as e:
#         print(e, file=sys.stderr)

#     return json.dumps(book_list)

