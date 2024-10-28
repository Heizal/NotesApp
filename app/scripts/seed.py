from app.app import create_app
from app.notes.models import Note
from app.extensions.database import db


if __name__ == '__main__':
  app = create_app()
  app.app_context().push()


# Notes template dictionary
note_data = {
  'Groceries' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'title':'Groceries', 'categoryName': 'basic'},
  'Class Assignment' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'title':'Class Assignment', 'categoryName': 'basic'},
  'My thoughts' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'title':'My thoughts', 'categoryName': 'basic'},
  'Class notes for Wednesday' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'title':'Class notes for Wednesday', 'categoryName': 'basic'},
  'To buy on Friday' : {'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam sequi error aliquid.', 'title':'To buy on Friday', 'categoryName': 'basic'},
}

for slug, note in note_data.items():
  new_note = Note(slug=slug, title=note['title'], content=note['content'])
  db.session.add(new_note)

db.session.commit()
