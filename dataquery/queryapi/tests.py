from django.test import TestCase
import types
import re
from pathlib import Path
from .apis import *

class SearchTestCase(TestCase):
    def test_data_request(self):
        data = get_data()
        BASE_DIR = Path(__file__).resolve().parent
        TEMPLATE_PATH = Path.joinpath(BASE_DIR, "static", "data.txt")
        with open(TEMPLATE_PATH, 'r') as f:
            self.assertEqual(json.dumps(json.loads(data)), json.dumps(json.loads(f.read())))


    def test_first_example_query(self):
        params = { 'attribute' : 'subject', 'value' : 'missing' }
        request = types.SimpleNamespace()
        request.GET = types.SimpleNamespace()
        request.GET.get = lambda key, default: params.get(key) if params.get(key) else default
        result = search_request(request)
        BASE_DIR = Path(__file__).resolve().parent
        TEMPLATE_PATH = Path.joinpath(BASE_DIR, "static", "example1.txt")
        with open(TEMPLATE_PATH, 'r') as f:
            self.assertEqual(result.content.decode('utf-8'), json.dumps(json.loads(f.read())))


    def test_second_example_query(self):
        pass
