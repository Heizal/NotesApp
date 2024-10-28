from datetime import datetime
from app.extensions.database import db, CRUDMixin

class Category(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(80))
    task = db.Column(db.String(250))
    tag = db.relationship('Tag', backref='category', uselist=False, lazy=True )

class Tag(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    tagName = db.Column(db.String(80))
    description = db.Column(db.String(80))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    note_tags = db.relationship('NoteTag', backref='tag', lazy=True)


class NoteTag (db.Model, CRUDMixin):
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
    number_of_notes = db.Column(db.Integer)



