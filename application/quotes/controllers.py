from flask import jsonify, request
from werkzeug import exceptions
from .models import Quote
from .. import db

def index():
    quotes = Quote.query.all()
    try:
        return jsonify({"data": [q.json for q in quotes ]})
    except:
        raise exceptions.InternalServerError(f"something has gone awfully wrong and we are trying to fix it")
    
def show(id):
    quote = Quote.query.filter_by(id=id).first()
    try:
        return jsonify({"data": quote.json}), 200
    except:
        raise exceptions.NotFound(f"big time fun and laughs")
    
def create():
    try:
        title, author = request.json.values()

        new_quote = Quote(title, author)
        db.session.add(new_quote)
        db.session.commit()
        return jsonify({ "data": new_quote.json}), 201
    except:
        raise exceptions.BadRequest(f"THIS IS A DISTINCT ERROR MESSAGE")

def update(id):
    data = request.json
    quote = Quote.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(quote, attribute):
            setattr(quote, attribute, value)
    db.session.commit()
    return jsonify({ "data":quote.json})


def destroy(id):
    quote = Quote.query.filter_by(id=id).first()
    db.session.delete(quote)
    db.session.commit()
    return "quote is now been removed and sent to quote heaven, where they belong", 204
