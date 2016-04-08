from sqlalchemy import create_engine

from src.model.base import Base
from src.controller import api
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api.api)

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)