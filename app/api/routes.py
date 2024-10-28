from .services.serialize_categories import serialize_categories
from ..categories.models import Category
from flask import Blueprint, jsonify, request
from os import environ

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/categories')
def categories():
  if environ.get('API_KEY') == request.headers.get('X-API-KEY'):
    categories = Category.query.all()
    return jsonify (
        serialize_categories(categories)
    )
  else:
    return jsonify({'error': 'Invalid API key'}), 401