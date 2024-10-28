from app.categories.models import Category, Tag
from app.notes.models import Note

def test_get_checkout_renders(client):
  # Page loads and renders checkout
  response = client.get('/checkout')
  assert b'Task' in response.data

def test_post_checkout_category(client):
  #creates a category record
  response = client.post('/checkout', data={
    'name': 'To do tomorrow',
    'category': 'Random',
    'task': 'Buy eggs'
  })
  
  assert Category.query.first()

def test_post_checkout_creates_tag(client):
  #Creates a tag related to the category
  response = client.post('/checkout', data={
    'tagName': 'climate change',
    'description': 'categories about climate change',
    'updated_at': '06/09/2022'
  })

  assert Tag.query.first().category_id is 1


def test_post_checkout_creates_note_tag(client):
  #creates note tag related to the tag model
  new_note = Note(slug='Groceries', title='Groceries', content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.')
  new_note.save()

  response = client.post('/checkout', data={
    'tagName': 'climate change',
    'description': 'categories about climate change',
    'updated_at': '06/09/2022'
  })

  assert Tag.query.first().note_tags[0].number_of_notes == 1
