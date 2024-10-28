from app.extensions.database import db
from app.notes.models import Note

def test_note_update(client):
    # updates note properties
    note = Note(slug='Things', title='salt', content='Lorem ipsum dolor sit amet consectetur adipisicing.')
    db.session.add(note)
    db.session.commit()

    note.title = 'Milk'
    note.save()

    updated_note = Note.query.filter_by(slug='Things').first()
    assert updated_note.title == 'Milk'

def test_note_delete(client):
    #deletes note
    note = Note(slug='butter', title='Butter', content='Lorem ipsum dolor sit amet consectetur adipisicing')
    db.session.add(note)
    db.session.commit()

    note.delete()

    deleted_note = Note.query.filter_by(slug='butter').first()
    assert deleted_note is None
