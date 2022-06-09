

def test_ping(myserver):
    res = myserver.get('/ping')
    assert res.text == 'pong'


def test_pong(myserver):
    res = myserver.get('/pong')
    assert res.text == 'ping'


def test_hello(myserver):
    name = 'John'
    res = myserver.get(f'/hello/{name}')
    assert res.text == f'Hello {name}!'
