import boto3
import datetime
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Truy cập bảng DynamoDB
    table = dynamodb.Table('studentData')
    response = table.scan()
    items = response['Items']

    # Lưu dữ liệu vào file tạm trong Lambda
    backup_file = '/tmp/backup.json'
    with open(backup_file, 'w') as f:
        json.dump(items, f)

    # Tải file lên S3
    s3_bucket = 'student-backup-20250706'  # Thay bằng tên bucket thực tế
    s3_key = f'backups/backup-{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
    s3_client.upload_file(backup_file, s3_bucket, s3_key)

    # Tạo pre-signed URL (hết hạn sau 1 giờ)
    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': s3_bucket, 'Key': s3_key},
        ExpiresIn=3600
    )

    # Tạo email HTML đẹp
    sender = 'baothangvip@gmail.com'
    recipient = 'nguyentribaothang@gmail.com'
    subject = 'Thông Báo Sao Lưu Dữ Liệu Sinh Viên'
    expiry_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    
    html_body = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; line-height: 1.6; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 8px; }}
            .header {{ background-color: #4CAF50; color: white; padding: 10px; text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ padding: 20px; background-color: white; border-radius: 0 0 8px 8px; }}
            .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white !important; text-decoration: none; border-radius: 5px; margin-top: 20px; }}
            .footer {{ font-size: 12px; color: #777; text-align: center; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>Sao Lưu Dữ Liệu Sinh Viên</h2>
            </div>
            <div class="content">
                <p>Kính gửi Quý khách,</p>
                <p>Dữ liệu sinh viên đã được sao lưu thành công và lưu trữ trên AWS S3.</p>
                <p><strong>Tải file sao lưu tại đây:</strong></p>
                <a href="{presigned_url}" class="button">Tải File Sao Lưu</a>
                <p><strong>Lưu ý:</strong> Liên kết này sẽ hết hạn vào {expiry_time}.</p>
            </div>
            <div class="footer">
                <p>Đây là email tự động. Vui lòng không trả lời trực tiếp email này.</p>
            </div>
        </div>
    </body>
    </html>
    """

    try:
        response = ses.send_email(
            Source=sender,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Html': {'Data': html_body},
                    'Text': {'Data': f'File sao lưu: {presigned_url}\nHết hạn: {expiry_time}'}
                }
            }
        )
        print(f"Email sent! Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"Lỗi gửi email: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Sao lưu thành công nhưng gửi email thất bại: {str(e)}'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Sao lưu và gửi email thành công!'})
    }