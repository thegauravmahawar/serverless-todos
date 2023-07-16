import json


def delete(event, context):

    id = event['pathParameters']['id']
    print(2)

    response = {
        "statusCode": 200,
        "body": "Task {} deleted successfully.".format(id),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
