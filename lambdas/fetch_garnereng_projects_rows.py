import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    table_name = 'garnereng_projects'
    response = client.scan(TableName=table_name, Limit=2000)

    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': response
    }
