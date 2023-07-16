import json


def update(event, context):

    raw_payload = event['body']
    payload = json.loads(raw_payload)
    print(4)

    response = {
        "statusCode": 200,
        "body": json.dumps(payload),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
