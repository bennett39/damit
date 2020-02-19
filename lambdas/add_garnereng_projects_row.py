import datetime
import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    table_name = 'garnereng_projects'
    item = {
        'date': {
            'N': str(datetime.datetime.now().timestamp())
        },
        'project_name': {
            'S': event.get('project_name')
        },
        'client_name': {
            'S': event.get('client_name')
        },
    }
    response = client.put_item(Item=item, TableName=table_name)

    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': response
    }

