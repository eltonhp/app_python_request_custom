import boto3


class DynamoConfig:

    def __init__(self) -> None:
        self.conf = {
            'aws_access_key_id': '*************',
            'aws_secret_access_key': '***************************',
            'region_name': 'us-east-1'
        }

        self.dynamodb = boto3.resource('dynamodb', **self.conf)