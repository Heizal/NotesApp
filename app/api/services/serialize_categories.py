# def serialize_note_tags(note_tags):
#     note_tags_list = []

#     for note_tag in note_tags:
#         note_tags_list.append({
#             'note_id': note_tag.note_id,
#             'tag_id': note_tag.tag_id,
#             'number_of_notes': note_tag.number_of_notes,
#             'note_title': note_tag.note.title
#         })

#     return note_tags_list

def serialize_categories(categories):
    categories_list = []

    for category in categories:
        categories_list.append({
            'id': category.id,
            'name': category.name,
            'category': category.category,
            'task': category.task,
            'tag': {
                'tagName': category.tag.tagName,
                'description': category.tag.description,
                'updated_at': category.tag.updated_at
            }
            # 'note_tags': serialize_note_tags(categories.note_tags)
        })

    return categories_list