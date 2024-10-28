from app.newnote.models import NewNote

def test_get_newnote_renders(client):
    response = client.get('/newnote')
    assert b'NewNote' in response.data

def test_post_newnote_creates_newnote(client):
    respone = client.post('/newnote', data={
        'name': 'To do now',
        'category': 'Random',
        'task': 'Store sugar'
    })
    assert NewNote.query.first() is not None

