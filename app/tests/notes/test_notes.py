def test_notes_success(client):
    # page loads
    response = client.get('/notes')
    assert response.status_code == 200

def test_notes_content(client):
    # returns content on index page
    response = client.get('/notes')
    assert b'My Sticky Notes' in response.data