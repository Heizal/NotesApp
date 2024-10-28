from app.notes.models import Note
from app.newnote.models import NewNote
from flask import Blueprint, render_template, request, redirect, url_for,flash
from app.extensions.database import db
import re

import logging

logging.basicConfig(level=logging.DEBUG)

blueprint = Blueprint('newnote', __name__)

@blueprint.get('/newnote')
def get_newnote():
    return render_template('newnote/new.html')

@blueprint.post('/newnote')
def post_newnote(): 
    # Get form data
    title = request.form.get('title')
    content = request.form.get('content')

    if title and content:
        # Generate a slug from the title
        slug = re.sub(r'\W+', '-', title.lower()).strip('-')

        # Ensure slug is unique by appending a random suffix if it exists already
        existing_note = Note.query.filter_by(slug=slug).first()
        if existing_note:
            slug = f"{slug}-{str(existing_note.id)}"

        try:
            # Create and add new note with slug to the database
            new_note = Note(title=title, content=content, slug=slug)
            db.session.add(new_note)
            db.session.commit()

            # Redirect to the /notes page or the new note page
            return redirect(url_for('notes.notes'))
        except Exception as e:
            flash(f"An error occurred: {e}", 'danger')
            db.session.rollback()
            return render_template('newnote/new.html')
    else:
        flash('Title and content are required to create a note!', 'warning')

    return render_template('newnote/new.html')


