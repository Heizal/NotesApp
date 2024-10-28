from flask import Blueprint, render_template, request, current_app
from app.notes.models import Note
from app.categories.models import Category, Tag,  NoteTag
from .services.create_category import create_category
from flask_login import login_required

blueprint = Blueprint('categories', __name__)

@blueprint.get('/checkout')
@login_required
def get_checkout():
  notes = Note.query.all()

  return render_template('categories/category.html', notes = notes)

@blueprint.post('/checkout')
def post_checkout():
  #Add exceptions with try and except
  try:
    notes = Note.query.all()

    #validations
    if not all([
        request.form.get('name'),
        request.form.get('category'),
        request.form.get('task')

    ]):
        raise Exception('Please fill out all the fields')
    
    create_category(request.form, notes)
    return render_template('categories/category.html', notes = notes)
  except Exception as error_message:
     error = error_message or 'An error occured while processing your note. Please make sure to enter valid data'
     current_app.logger.info(f'Error creating an category: {error}')
     return render_template('categories/category.html', 
                            notes = notes,
                            error = error)
