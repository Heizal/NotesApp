from app.extensions.database import db, CRUDMixin

class Note(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(250))
    note_tags = db.relationship('NoteTag', backref='note', lazy=True )