from .models import Note
from app.extensions.database import db
from flask import Blueprint, render_template, request, current_app,flash,redirect,url_for
import re

blueprint = Blueprint('notes', __name__)

# Notes route
@blueprint.route('/notes')
def notes():
    page_number = request.args.get('page', 1, type=int)
    notes_pagination = Note.query.paginate(page=page_number, per_page=current_app.config['NOTES_PER_PAGE'])
    return render_template('notes/notes.html', notes_pagination=notes_pagination)

@blueprint.route('/notes/<slug>')
def note(slug):
    # return slug
    note = Note.query.filter_by(slug=slug).first()
    #x = note_data[slug]
    return render_template('notes/tasks.html', note=note)

@blueprint.post('/notes/delete/<slug>')
def delete_note(slug):
    note = Note.query.filter_by(slug=slug).first()

    if note:
        try:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted successfully!', 'success')
        except Exception as e:
            flash(f"An error occurred while deleting the note: {e}", 'danger')
            db.session.rollback()
    else:
        flash('Note not found!', 'warning')

    # Redirect back to the notes page
    return redirect(url_for('notes.notes'))

# GET route to render edit form
@blueprint.get('/notes/edit/<slug>')
def get_edit_note_form(slug):
    # Logic to show edit form for the note
    note = Note.query.filter_by(slug=slug).first()

    if not note:
        abort(404)
    
    return render_template('notes/edit.html',note=note)

# POST route to update the note
@blueprint.post('/notes/edit/<slug>')
def post_edit_note_form(slug):
    note = Note.query.filter_by(slug=slug).first()

    # If the note is not found, return a 404 error
    if not note:
        abort(404)

    # Get updated data from the form
    title = request.form.get('title')
    content = request.form.get('content')

    if title and content:
        # Update the note's title and content
        note.title = title
        note.content = content

        # Update the slug if the title has changed
        new_slug = re.sub(r'\W+', '-', title.lower()).strip('-')
        if new_slug != note.slug:
            # Ensure the new slug is unique
            existing_note = Note.query.filter_by(slug=new_slug).first()
            if existing_note and existing_note.id != note.id:
                new_slug = f"{new_slug}-{note.id}"

            note.slug = new_slug

        try:
            db.session.commit()
            flash('Note updated successfully!', 'success')
            return redirect(url_for('notes.note', slug=note.slug))
        except Exception as e:
            flash(f"An error occurred while updating the note: {e}", 'danger')
            db.session.rollback()
    else:
        flash('Title and content are required to update the note!', 'warning')

    # Re-render the edit form with the note to correct validation errors
    return render_template('notes/edit.html', note=note)