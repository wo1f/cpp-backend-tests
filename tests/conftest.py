import os
import pytest
from xprocess import ProcessStarter
from dataclasses import dataclass
import requests
from urllib.parse import urljoin


@dataclass
class Server:
    url: str

    def get(self, endpoint):
        return requests.get(urljoin(self.url, endpoint))

    def post(self, endpoint, data):
        return requests.post(urljoin(self.url, endpoint), data)


@pytest.fixture(scope='module')
def myserver(xprocess):
    class Starter(ProcessStarter):
        pattern = 'Running on'
        path = os.environ['DELIVERY_APP']
        args = ['python3', path]

    logfile = xprocess.ensure("myserver", Starter)
    print(logfile)
    yield Server('http://localhost:8000/')

    xprocess.getinfo("myserver").terminate()
