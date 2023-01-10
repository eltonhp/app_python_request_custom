from .http_request import HttpRequest
from ..errors import HttpRequestError

def test_get_payload():
    http_request = HttpRequest()
    response = http_request.get_payload(1, "https://swapi.dev/api/people")
    print(response)

    error = HttpRequestError(any, 400)
    assert error.status_code == 400
    assert response.status_code == 200


