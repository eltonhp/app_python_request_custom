from .http_request import HttpRequest
from ..errors import HttpRequestError


def read(filename):
    """ read a text file and return a list of numbers """
    with open(filename) as f:
        lines = f.readlines()
        return [float(line.strip()) for line in lines]


def calculate_total(filename):
    """ return the sum of numbers in a text file """
    numbers = read(filename)
    return sum(numbers)

def test_get_payload():
    http_request = HttpRequest()
    response = http_request.get_payload(1, "https://swapi.dev/api/people")
    print(response)

    error = HttpRequestError(any, 400)
    assert error.status_code == 400
    assert response.status_code == 200


