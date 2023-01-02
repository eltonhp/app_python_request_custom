from http_request import HttpRequest


def test_get_payload():
    http_request = HttpRequest()
    response = http_request.get_payload(1, "https://swapi.dev/api/people")
    print(response)

    assert response.status_code == 200


