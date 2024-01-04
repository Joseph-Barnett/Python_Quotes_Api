from flask import request
from werkzeug import exceptions
from application import app # app from __init__.
from .controllers import index, create, show, update, destroy


@app.route('/quotes', methods=["GET", "POST"])
def handle_quotes():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@app.route('/quotes/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_quote(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
