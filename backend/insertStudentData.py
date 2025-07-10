import json
import boto3
import logging

# Thiết lập logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Khởi tạo kết nối DynamoDB và SES
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')
ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
    logger.info("Event nhận được: %s", json.dumps(event))

    # Xử lý request body
    try:
        if isinstance(event.get('body'), str):
            body = json.loads(event['body'])
        elif isinstance(event.get('body'), dict):
            body = event['body']
        else:
            body = {}
    except Exception as e:
        logger.error("Lỗi khi parse JSON: %s", str(e))
        return _response(400, "Dữ liệu gửi lên không hợp lệ.")

    # Lấy các trường
    student_id = body.get('studentid')
    name = body.get('name')
    student_class = body.get('class')
    birthdate = body.get('birthdate')
    email = body.get('email')

    # Kiểm tra dữ liệu hợp lệ
    if not all([student_id, name, student_class, birthdate, email]):
        logger.error("Thiếu các trường: studentid=%s, name=%s, class=%s, birthdate=%s, email=%s",
                     student_id, name, student_class, birthdate, email)
        return _response(400, "Thiếu thông tin sinh viên cần thiết.")

    # Kiểm tra trùng mã sinh viên
    try:
        existing = table.get_item(Key={'studentid': student_id})
        if 'Item' in existing:
            logger.error("Mã sinh viên %s đã tồn tại", student_id)
            return _response(409, f"Mã sinh viên '{student_id}' đã tồn tại.")
    except Exception as e:
        logger.error("Lỗi khi kiểm tra mã sinh viên: %s", str(e))
        return _response(500, "Lỗi khi kiểm tra dữ liệu.")

    # Lưu dữ liệu vào DynamoDB
    try:
        table.put_item(
            Item={
                'studentid': student_id,
                'name': name,
                'class': student_class,
                'birthdate': birthdate,
                'email': email
            }
        )
        logger.info("Lưu dữ liệu thành công cho studentid: %s", student_id)
    except Exception as e:
        logger.error("Lỗi khi lưu vào DynamoDB: %s", str(e))
        return _response(500, "Lỗi khi lưu dữ liệu vào hệ thống.")

    # Gửi email thông báo
    email_error = None
    try:
        ses.send_email(
            Source='baothangvip@gmail.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Dữ Liệu Sinh Viên Đã Được Lưu'},
                'Body': {
                    'Text': {
                        'Data': (
                            f'📢 THÔNG BÁO TỪ HỆ THỐNG QUẢN LÝ SINH VIÊN HUTECH\n\n'
                            f'Chào bạn {name},\n\n'
                            f'✅ Thông tin sinh viên của bạn đã được lưu thành công trên hệ thống.\n\n'
                            f'🔹 Mã sinh viên: {student_id}\n'
                            f'🔹 Họ tên: {name}\n'
                            f'🔹 Lớp: {student_class}\n'
                            f'🔹 Ngày sinh: {birthdate}\n\n'
                            f'📬 Vui lòng giữ email này để đối chiếu khi cần thiết.\n\n'
                            f'Thân mến,\n'
                            f'📘 Hệ thống quản lý sinh viên\n'
                            f'📧 Email: hutech@system.edu.vn (nếu bạn muốn dùng tên miền riêng)\n'
                        )
                    }
                }
            }
        )
        logger.info("Gửi email thành công tới: %s", email)
    except Exception as e:
        email_error = str(e)
        logger.error("Lỗi khi gửi email tới %s: %s", email, email_error)

    # Trả kết quả
    if email_error:
        return _response(200, f"Dữ liệu sinh viên đã được lưu nhưng gửi email tới {email} thất bại: {email_error}")
    return _response(200, "Dữ liệu sinh viên đã được lưu và email thông báo đã được gửi!")

# Hàm trả về response chuẩn
def _response(status_code, message):
    return {
        'statusCode': status_code,
        'body': json.dumps({'message': message}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }