import requests
from src.util.string_util import StringUtil
from src.model.person import Person
from src.model.address import Address
from src.model.base import Base

from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def root():
    return jsonify({'hello': 'world'})

@api.route('/sample_http_request', methods=['GET'])
def sample():
    url = 'http://jsonplaceholder.typicode.com/posts?userId=1'
    r = requests.get(url)
    ret = {
        'status-code': r.status_code,
        'content-type': r.headers['content-type'],
        'encoding': r.encoding,
        'text': r.text,
        'json': r.json()
    }
    return jsonify(ret)


@api.route('/length', methods=['GET'])
def length():
    input = request.args['input']
    return jsonify(
        {
            'input': input,
            'length': str(StringUtil.char_count(input))
        })

@api.route('/create_db', methods=['GET'])
def create_db():
    return "a"
    # engine = create_engine('sqlite:///sqlalchemy_example.db')
    # Base.metadata.bind = engine
    # DBSession = sessionmaker(bind=engine)
    # session = DBSession()
    # 
    # new_person = Person(name='new person')
    # session.add(new_person)
    # session.commit()
    # 
    # # Insert an Address in the address table
    # new_address = Address(post_code='00000', person=new_person)
    # session.add(new_address)
    # session.commit()
