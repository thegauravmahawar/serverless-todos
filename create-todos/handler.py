import json


def create_todos(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 201, "body": json.dumps(body)}

    return response
