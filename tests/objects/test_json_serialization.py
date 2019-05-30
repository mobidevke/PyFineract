import json

from fineract.handlers import RequestHandler
from fineract.objects import Client


def test_json_serialization():
    with open('tests/files/client.json', 'r') as in_file:
        data = json.load(in_file)
        request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
        client = Client(request_handler, data, False)
        json_string = json.dumps(client.as_dict())
        assert isinstance(json_string, str)