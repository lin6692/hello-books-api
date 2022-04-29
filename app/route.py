from urllib import response
from flask import Blueprint, jsonify, abort, make_response

'''
HELLO WORLD
'''
# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_word():
#     response_body = "Hello, World!"
#     return response_body

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def get_json():
#     return {
#     "name": "Ada Lovelace",
#     "message": "Hello!",
#     "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body
'''
BOOK HARDCODE
'''
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ] 

# books_bp = Blueprint("books", __name__, url_prefix="/books")
# @books_bp.route("", methods=["GET"])
# def get_all_books():
#     res = []
#     for book in books:
#         res.append({"id": book.id, "title": book.title, 
#                     "description": book.description})
#     return jsonify(res)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validdate_book(book_id)
#     return {
#         "id":book.id,
#         "title":book.title,
#         "description":book.description
#         }

# def validdate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))