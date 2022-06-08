import requests


def test_ping():
    res = requests.get('http://localhost:8000/ping')
    assert res.text == 'pong'


def test_pong():
    res = requests.get('http://localhost:8000/pong')
    assert res.text == 'ping'


def test_hello():
    name = 'John'
    res = requests.get(f'http://localhost:8000/hello/{name}')
    assert res.text == f'Hello {name}!'
