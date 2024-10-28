from app.notes.models import Note

def test_notes_renders_notes(client):
    #page laods and renders notes
    new_note = Note(slug='you again', title='Yes me again', content='Lorem ipsum')
    new_note.save()

    response = client.get('/notes')

    assert b'Groceries' in response.data