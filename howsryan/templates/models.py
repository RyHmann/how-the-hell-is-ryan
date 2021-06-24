from howsryan import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    date_started = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"