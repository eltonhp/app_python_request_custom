from src.repository.dynamo_config import DynamoConfig
from boto3.dynamodb.conditions import Key

class DynamoRepository:
    def __init__(self) -> None:
        self.dynamodb = DynamoConfig().dynamodb

    def put_item(self, payload):
        payload['codigo_particao'] = payload['name'] + "#" + payload['height'] + "#" + payload['mass']
        self.dynamodb.Table('mavel').put_item(
            Item=payload
        )

    def get_item(self, chaveParticao):
        response = self.dynamodb.Table('mavel').query(
            KeyConditionExpression=Key('codigo_particao').eq(chaveParticao)
        )
        return response