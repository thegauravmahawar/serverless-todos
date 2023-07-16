import json


def get(event, context):

    id = event['pathParameters']['id']
    payload = {
        'task': 'Run',
        'description': 'Run 5 Kms',
        'priority': 3,
        'date': '15-07-2023'
    }

    response = {
        "statusCode": 200,
        "body": payload,
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
