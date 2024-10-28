from app.categories.models import Category, Tag, NoteTag

def create_category(form_data, notes):
    #create a category
  category = Category(
    name = form_data.get('name'),
    category = form_data.get('category'),
    task = form_data.get('task'),
  )
  category.save()

  tag = Tag(
    tagName = form_data.get('tagName'),
    description = form_data.get('description'),
    updated_at = form_data.get('created_at'),
    category = category
  )
  tag.save()

  #Create note tags
  for note in notes:
    number_of_notes = form_data.get(note.slug, 0)

    if int(number_of_notes) > 0:
      note_tags = NoteTag(
        note=note,
        tag=tag,
        number_of_notes = number_of_notes
    )
      note_tags.save()

