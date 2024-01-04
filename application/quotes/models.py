from application import db, app

app.app_context().push()

class Quote(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(500), nullable=False)

    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __repr__(self):
        return f"Quote(id: {self.id}, text: {self.text})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "text": self.text,
            "author": self.author,
        }
