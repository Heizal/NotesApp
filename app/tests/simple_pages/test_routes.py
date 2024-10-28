# ROUTE TESTS
def test_index_success(client):
    # page loads
    response = client.get('/')
    assert response.status_code == 200

# test for contact route
def test_contact_success(client):
    # page laods
    response = client.get('/contact')
    assert response.status_code == 200

# CONTENT TESTS
def test_index_content(client):
    # returns content on index page
    response = client.get('/')
    assert b'Note taking made easier' in response.data

def test_contact_content(client):
    # returns content on contact page
    response = client.get('/contact')
    assert b'Have questions about how to use Sticky?' in response.data



