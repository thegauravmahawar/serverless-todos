import json
import boto3

def create(event, context):

    raw_payload = event['body']
    payload = json.loads(raw_payload)
    print(payload)
    print(2)

    response = {
        "statusCode": 201,
        "body": json.dumps(payload),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
