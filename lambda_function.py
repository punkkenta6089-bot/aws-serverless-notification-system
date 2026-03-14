import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('portfolio-table-tokyo')

sns = boto3.client('sns')

TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):
    record_id = str(uuid.uuid4())
    now = datetime.now().isoformat()

    table.put_item(
        Item={
            'id': record_id,
            'timestamp': now
        }
    )

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message="A file has been uploaded to S3.",
        Subject="Portfolio Notification"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
