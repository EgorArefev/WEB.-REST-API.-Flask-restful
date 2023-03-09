from flask import Flask
from data import db_session
from flask_restful import reqparse, abort, Api, Resource
from data import users_resources, db_session

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("mars_explorer.sqlite")
    # для списка объектов
    api.add_resource(users_resources.UsersListResource, '/api/v2/user')

    # для одного объекта
    api.add_resource(users_resources.UsersResource, '/api/v2/news/<int:user_id>')
    app.run()


if __name__ == '__main__':
    main()


