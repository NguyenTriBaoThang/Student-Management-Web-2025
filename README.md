# Student-Management-Web: Source Code for Serverless Student Management Website on AWS 🚀

![AWS Serverless](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws) ![Duration](https://img.shields.io/badge/Duration-8%20Hours-blue) ![Level](https://img.shields.io/badge/Level-Intermediate-green)

Chào mừng bạn đến với repository **Student-Management-Web**, nơi chứa **source code** của dự án workshop **Triển Khai Website Serverless Quản Lý Thông Tin Sinh Viên với AWS**. Repository này bao gồm mã nguồn giao diện web tĩnh (HTML, CSS, JavaScript) và các hàm Lambda (Python) để triển khai ứng dụng serverless trên AWS, sử dụng các dịch vụ như **S3**, **CloudFront**, **API Gateway**, **Lambda**, **DynamoDB**, **SES**, và **EventBridge**. Dự án giúp quản lý thông tin sinh viên, hỗ trợ sao lưu tự động và gửi thông báo qua email.

**Welcome to the Student-Management-Web repository**, which hosts the **source code** for the workshop **Deploying a Serverless Student Management Website with AWS**. This repository includes the static web interface (HTML, CSS, JavaScript) and Lambda functions (Python) for deploying a serverless application on AWS, using services like **S3**, **CloudFront**, **API Gateway**, **Lambda**, **DynamoDB**, **SES**, and **EventBridge**. The project enables student information management, automated backups, and email notifications.

<p align="center">
  <a href="https://nguyentribaothang.github.io/" rel="dofollow" target="blank"><strong>Explore the hugo »</strong></a>
	<br/>
	<br/>
	<a href="https://github.com/NguyenTriBaoThang/NguyenTriBaoThang.github.io/blob/main/.github/PROPOSAL.md">💡Workshop Proposal</a>
	|
	<a href="https://github.com/NguyenTriBaoThang/Student-Management-Web-2025.git">📂Source code</a>
	|
	<a href="https://github.com/NguyenTriBaoThang/NguyenTriBaoThang.github.io.git">📚Main Repository</a>
</p>

<p>Sơ đồ kiến trúc tổng hợp: </p> 
<p align="center">
	<img loading="lazy" src="./images/system-architecture-overview.svg" alt="Project">
</p>

---

## Giới Thiệu / Introduction

Dự án **Student-Management-Web** là một ứng dụng web serverless để quản lý thông tin sinh viên, được phát triển trong workshop kéo dài **8 giờ**. Giao diện web tĩnh (HTML, CSS với Tailwind CSS, JavaScript) cho phép người dùng nhập, xem, và sao lưu dữ liệu sinh viên. Backend serverless sử dụng **Lambda**, **API Gateway**, và **DynamoDB** để xử lý dữ liệu, tích hợp **S3** và **CloudFront** để lưu trữ/phân phối giao diện, **EventBridge** để lên lịch sao lưu, và **SES** để gửi email thông báo.

**The Student-Management-Web project** is a serverless web application for managing student information, developed during an **8-hour workshop**. The static web interface (HTML, CSS with Tailwind CSS, JavaScript) allows users to input, view, and back up student data. The serverless backend uses **Lambda**, **API Gateway**, and **DynamoDB** for data processing, with **S3** and **CloudFront** for hosting/distribution, **EventBridge** for scheduling backups, and **SES** for sending email notifications.

---

## Thông Tin Sinh Viên Thực Tập / Internship Student Information

### Nguyễn Tri Bão Thắng  
- **Trường / University**: Đại Học Công nghệ TP.HCM (HUTECH)  
- **MSSV / Student ID**: 2180601452  
- **Gmail**: [nguyentribaothang@gmail.com](mailto:nguyentribaothang@gmail.com)  
- **GitHub**: [NguyenTriBaoThang](https://github.com/NguyenTriBaoThang)  

### Võ Thành Trung  
- **Trường / University**: Đại Học Công nghệ TP.HCM (HUTECH)  
- **MSSV / Student ID**: 2180603167  
- **Gmail**: [vothanhtrung9379@gmail.com](mailto:vothanhtrung9379@gmail.com)  
- **GitHub**: [ttrung03](https://github.com/ttrung03)  

---

## Nội Dung Repository / Repository Contents

Repository **Student-Management-Web** chứa mã nguồn của ứng dụng, bao gồm:

### Frontend
- **`index.html`**: Giao diện chính với form nhập liệu, bảng hiển thị sinh viên, và nút chức năng (Lưu, Xem, Sao lưu).  
- **`styles.css`**: File CSS sử dụng Tailwind CSS để định dạng giao diện.  
- **`scripts.js`**: JavaScript xử lý tương tác người dùng và gọi API Gateway (GET/POST /students, POST /backup).  

### Backend
- **`getStudentData.py`**: Lambda function truy xuất dữ liệu sinh viên từ DynamoDB table `studentData`.  
- **`insertStudentData.py`**: Lambda function thêm dữ liệu sinh viên vào DynamoDB.  
- **`BackupDynamoDBAndSendEmail.py`**: Lambda function sao lưu dữ liệu từ DynamoDB vào S3 bucket `student-backup-20250706` và gửi email qua SES.  

### Cấu Hình
- **JSON Scripts** (tùy chọn): Các file JSON mẫu để cấu hình API Gateway hoặc Lambda (nếu có).  

### Cấu Trúc Thư Mục
```
Student-Management-Web/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── scripts.js
├── backend/
│   ├── getStudentData.py
│   ├── insertStudentData.py
│   └── BackupDynamoDBAndSendEmail.py
└── config/
    └── (optional JSON scripts)
```

---

## Hướng Dẫn Cài Đặt và Triển Khai / Setup and Deployment Instructions

### 1. Clone Mã Nguồn / Clone the Repository
Sao chép mã nguồn từ repository:

```bash
git clone https://github.com/NguyenTriBaoThang/Student-Management-Web.git
cd Student-Management-Web
```

### 2. Cài Đặt Công Cụ / Install Development Tools
- **Node.js** (v16+): Tải từ [https://nodejs.org/](https://nodejs.org/) để quản lý Tailwind CSS.  
- **Visual Studio Code**: Tải từ [https://code.visualstudio.com/](https://code.visualstudio.com/) để chỉnh sửa mã.  
- **AWS CLI**: Tải từ [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/) để cấu hình AWS.  
- **Postman**: Tải từ [https://www.postman.com/downloads/](https://www.postman.com/downloads/) để kiểm tra API.  

Cấu hình AWS CLI:
```bash
aws configure
```
Nhập **Access Key**, **Secret Key**, vùng (`us-east-1`), và định dạng đầu ra (`json`).

### 3. Triển Khai Giao Diện Web / Deploy the Web Interface
- **Tạo S3 Bucket**: Tạo bucket `student-management-website-2025`, bật **Static Website Hosting**, và cấu hình Bucket Policy với Origin Access Identity (OAI).  
- **Tải Frontend**: Tải các file trong thư mục `frontend/` (`index.html`, `styles.css`, `scripts.js`) lên bucket.  
  ```bash
  aws s3 sync frontend/ s3://student-management-website-2025/
  ```
- **Cấu Hình CloudFront**: Tạo CloudFront Distribution `StudentWebsiteDistribution`, đặt `index.html` làm Default Root Object, và tạo invalidation để làm mới cache.  

### 4. Triển Khai Backend / Deploy the Backend
- **Tạo DynamoDB Table**: Tạo bảng `studentData` với Partition Key là MSSV.  
- **Tạo Lambda Functions**: Tải các file Python trong thư mục `backend/` lên Lambda:  
  - `getStudentData` (gắn vai trò `LambdaGetStudentRole`).  
  - `insertStudentData` (gắn vai trò `LambdaInsertStudentRole`).  
  - `BackupDynamoDBAndSendEmail` (gắn vai trò `DynamoDBBackupRoleStudent`, cấu hình 128 MB RAM, 512 MB lưu trữ).  
- **Tạo API Gateway**: Tạo API REST `student` (stage `prod`) với các endpoint:  
  - GET/POST `/students` (tích hợp với `getStudentData`, `insertStudentData`).  
  - POST `/backup` (tích hợp với `BackupDynamoDBAndSendEmail`).  
  - Cấu hình API Key (`StudentApiKey`), Usage Plan (`StudentUsagePlan`), và bật CORS.  

### 5. Thiết Lập Sao Lưu và Thông Báo / Setup Backup and Notifications
- **Tạo S3 Backup Bucket**: Tạo bucket `student-backup-20250706` để lưu trữ dữ liệu sao lưu.  
- **Cấu Hình EventBridge**: Tạo Rule `DailyDynamoDBBackup` (07:00 AM +07) để kích hoạt `BackupDynamoDBAndSendEmail`.  
- **Cấu Hình SES**: Xác minh email `no-reply@studentapp.com` để gửi thông báo sao lưu.  

### 6. Kiểm Tra Hệ Thống / Verify the System
- **Giao Diện**: Truy cập CloudFront URL để kiểm tra giao diện web.  
- **API**: Kiểm tra các endpoint GET/POST `/students`, POST `/backup` bằng Postman.  
- **Dữ Liệu**: Xác minh bản ghi trong DynamoDB `studentData` và file sao lưu trong S3 `student-backup-20250706`.  
- **Email**: Kiểm tra email thông báo từ SES.  
- **Logs**: Phân tích log bằng CloudWatch Logs Insights (ví dụ: `fields @message | filter @message like /ERROR/`).  

### 7. Dọn Dẹp Tài Nguyên / Clean Up Resources
- Xóa các tài nguyên để tránh chi phí: DynamoDB (`studentData`), Lambda, S3 (`student-management-website-2025`, `student-backup-20250706`), API Gateway (`student`), CloudFront (`StudentWebsiteDistribution`), SES, IAM roles, EventBridge (`DailyDynamoDBBackup`).  
- Kiểm tra AWS Billing Dashboard để đảm bảo tài khoản sạch.  

---

## Yêu Cầu Hệ Thống / System Requirements

- **Hệ Điều Hành / OS**: Windows, macOS, hoặc Linux  
- **AWS Account**: Tài khoản AWS Free Tier (vùng `us-east-1`)  
- **Công Cụ / Tools**: Node.js (v16+), Visual Studio Code, AWS CLI, Postman  
- **Trình Duyệt / Browser**: Chrome, Firefox, hoặc Edge (hỗ trợ JavaScript)  
- **Kết Nối / Connectivity**: Internet ổn định để truy cập AWS và GitHub  

---

📚 **Tài Liệu Tham Khảo**:

- [The First Cloud Journey](https://cloudjourney.awsstudygroup.com/)
- [AWS Special Force Portal](https://specialforce.awsstudygroup.com/)
- [AWS Serverless Workshops](https://aws.amazon.com/serverless/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [VTI Cloud](https://vticloud.io/)

---

## Liên Hệ / Contact

Có thắc mắc hoặc cần hỗ trợ? Liên hệ với chúng tôi:  
- **Nguyễn Tri Bão Thắng**: [nguyentribaothang@gmail.com](mailto:nguyentribaothang@gmail.com)  
- **Võ Thành Trung**: [vothanhtrung9379@gmail.com](mailto:vothanhtrung9379@gmail.com)  

🌟 **Cảm ơn bạn đã quan tâm đến dự án của chúng tôi!** Triển khai mã nguồn để trải nghiệm ứng dụng serverless quản lý sinh viên trên AWS! / **Thank you for your interest in our project!** Deploy the source code to experience a serverless student management application on AWS! 🚀
