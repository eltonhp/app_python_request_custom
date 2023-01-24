from src.http.http_request import HttpRequest
from src.repository.dynamo_repository import DynamoRepository


def test_save():
    http_request = HttpRequest()
    payload = http_request.get_payload(1, "https://swapi.dev/api/people")
    results = payload.response['results'];

    for dado in results:
        dynamodb = DynamoRepository()
        dynamodb.put_item(dado)
        print(dado)

def test_get():
    dynamodb = DynamoRepository()
    result = dynamodb.get_item("Obi-Wan Kenobi#182#77")
    print(result)



