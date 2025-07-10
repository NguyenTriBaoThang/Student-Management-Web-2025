import json
import boto3

def lambda_handler(event, context):
    # Kết nối tới DynamoDB trong vùng us-east-1
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('studentData')
    
    # Lấy toàn bộ dữ liệu từ bảng studentData
    response = table.scan()
    data = response['Items']

    # Tiếp tục quét nếu còn dữ liệu (phân trang)
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    # Trả về dữ liệu ở dạng JSON
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
