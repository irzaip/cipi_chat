import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello Worldhehe',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'outme': 'I am the best'
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
