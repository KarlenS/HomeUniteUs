import json
from flask import Blueprint, render_template, abort, jsonify, current_app, request, Response
from jinja2 import TemplateNotFound
import pymongo
from bson import ObjectId
from config.constants import DB_NAME

caseworker_api = Blueprint('caseworker_api', __name__,
                          template_folder='templates')

@caseworker_api.route('/api/<orgname>/caseworkers', methods=['GET'])
def get_all_caseworkers(org): 
  try:

  except Exception as e:
    return jsonify(error=str(e)), 404
  # return all caseworkers for organization

@caseworker_api.route('/api/<orgname>/caseworkers/<caseworker_id>', methods=['GET'])
def get_caseworkers(org): 
  try:
    
  except Exception as e:
    return jsonify(error=str(e)), 404
  # return all caseworkers for organization

@caseworker_api.route('/api/<orgname>/caseworkers', methods=['POST'])
def add_caseworker(org, caseworker_id): 
  try:
    
  except Exception as e:
    return jsonify(error=str(e)), 404
  # add a new caseworker to an organization

@caseworker_api.route('/api/<orgname>/caseworkers/<caseworker_id>', methods=['PUT'])
def update_caseworker(org, caseworker_id): 
  try:
    
  except Exception as e:
    return jsonify(error=str(e)), 404
  # update a caseworker by id

@caseworker_api.route('/api/<orgname>/caseworkers/<caseworker_id>', methods=['PUT'])
def uodate_caseworker(org, caseworker_id): 
  try:
    
  except Exception as e:
    return jsonify(error=str(e)), 404
  # delete a caseworker by id