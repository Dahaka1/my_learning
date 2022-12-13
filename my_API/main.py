# http://127.0.0.1:5000/hi http://127.0.0.1:5000/hi/ http://127.0.0.1:5000/hi/*ID*  - возможные запросы к серверу
# for test:
# curl -X *COMMAND* -d "{\"text\":\"val text dksh\", \"lang\":\"oo\"}" - H "Content-Type: application/json" http://127.0.0.1:5000/hi/5
# screening (slashes '\') is required for windows

from random import choice # модуль рандома для выдачи случайного значения в случае, если запрашиваемый id ответа не указан
from flask import Flask # веб-разработка
from flask_restful import Api, Resource, reqparse # функции для разработки апи

# заданный по умолчанию список возвращаемых данных по номеру запрашиваемого ID
lst = [
    {   'id': 1,
        'text': 'Hello, world!',
        'lang': 'en'
    },
    {   'id': 2,
        'text': '안녕 모두',
        'lang': 'kr'
    },
    {   'id': 3,
        'text': 'Привет всем!',
        'lang:': 'ru'
    },
    {   'id': 4,
        'text': 'Hi all!',
        'lang': 'en'
    }
]

# класс методов для взаимодействия с ресурсами сервера
class HiResource(Resource):
    # метод получения ресурса (в случае без указания id запрашиваемых данных в запросе и в случае с указанным id)
    def get(self, id=0):
        if id == 0:
            return choice(lst), 200 # случайные данные
        for val in lst:
            if val['id'] == id:
                return val, 200
        return "Warning! Can't find text. ", 404 # в случае, если указанного id не существует

    # метод обновления текущего ресурса (данных)
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        parser.add_argument('lang')
        params = parser.parse_args()# в переменную params помещаем запрошенные данные (аргументы) у парсера
        for val in lst:
            if val['id'] == id: # обновляем текстовые данные при существующем id
                val['text'] = params['text']
                val['text'] = params['lang']
                return val, 200
        val = { # добавляем данные при отсутствующем id
            'id': id,
            'text': params['text'],
            'lang': params['lang']
        }
        lst.append(val)
        return val, 200

    # метод для создания нового ресурса
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        parser.add_argument('lang')
        params = parser.parse_args() # аналогично принимаем текстовые данные
        for val in lst:
            if val['id'] == id:
                return f"This text with id={id} already exists", 400 # выдаем ошибку, если данные с указанным id уже существуют
        val = { # добавляем данные при отсутствующем id
            'id': id,
            'text': params['text'],
            'lang': params['lang']
        }
        lst.append(val)
        return val, 200

    # метод для удаления данных с запрошенным id
    def delete(self, id):
        global lst
        lst = [val for val in lst if val['id'] != id]
        return f"Record with id={id} was deleted!", 200


# идентификация апи и возможных запросов к серверу
if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(HiResource, '/hi', '/hi/', '/hi/<int:id>')
    app.run(debug=True)