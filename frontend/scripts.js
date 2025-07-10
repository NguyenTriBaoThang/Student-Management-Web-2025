var API_ENDPOINT = "https://23pm3n1vk5.execute-api.us-east-1.amazonaws.com/prod";
var API_KEY = "3sltqJjS1ha5DNJ7O9ITj5jOmMkju1658MnC0KHd";

// Hàm mã hóa HTML để ngăn XSS
function escapeHTML(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
}

// Xử lý lưu dữ liệu sinh viên (POST)
document.getElementById("savestudent").onclick = function () {
    var inputData = {
        studentid: $('#studentid').val(),
        name: $('#name').val(),
        class: $('#class').val(),
        birthdate: $('#birthdate').val(),
        email: $('#email').val()
    };

    // Kiểm tra rỗng và định dạng email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!inputData.studentid || !inputData.name || !inputData.class || !inputData.birthdate || !inputData.email) {
        alert("Vui lòng nhập đầy đủ thông tin.");
        return;
    }
    if (!emailPattern.test(inputData.email)) {
        alert("Email không hợp lệ.");
        return;
    }

    console.log("Dữ liệu gửi POST:", { body: JSON.stringify(inputData) });

    $.ajax({
        url: API_ENDPOINT,
        type: 'POST',
        data: JSON.stringify({ body: JSON.stringify(inputData) }),
        contentType: 'application/json',
        headers: {
            'x-api-key': API_KEY
        },
        success: function (response) {
            console.log("Phản hồi POST:", response);
            let message = "Dữ liệu sinh viên đã được lưu!";
            if (response && response.statusCode === 400) {
                try {
                    const error = JSON.parse(response.body || "{}");
                    message = `Lỗi: ${escapeHTML(error.message || "Không xác định")}`;
                } catch (e) {
                    console.error("Lỗi phân tích body:", e);
                    message = "Lỗi: Không xác định";
                }
            } else if (response && typeof response.body === 'string') {
                try {
                    const data = JSON.parse(response.body);
                    if (data && data.name && data.studentid) {
                        message = `Đã lưu sinh viên: ${escapeHTML(data.name)} (${escapeHTML(data.studentid)})`;
                    } else {
                        console.warn("Dữ liệu body không chứa name hoặc studentid:", data);
                    }
                } catch (e) {
                    console.error("Lỗi phân tích body:", e);
                }
            } else {
                console.warn("Phản hồi không có body hoặc body không phải chuỗi:", response);
            }
            document.getElementById("studentSaved").textContent = message;
        },
        error: function (xhr) {
            let errorMessage = "Không xác định";
            try {
                const error = JSON.parse(xhr.responseText || "{}");
                errorMessage = error.message || errorMessage;
            } catch (e) {
                errorMessage = xhr.responseText || errorMessage;
            }
            alert("Lỗi khi lưu: " + errorMessage);
        }
    });
};

// Xử lý lấy danh sách sinh viên (GET)
document.getElementById("getstudents").onclick = function () {
    $.ajax({
        url: API_ENDPOINT,
        type: 'GET',
        contentType: 'application/json',
        headers: {
            'x-api-key': API_KEY
        },
        success: function (response) {
            console.log("Phản hồi GET:", response); // Ghi log để kiểm tra
            $('#studentTable tbody').empty();
            let students = response;
            // Kiểm tra nếu response là đối tượng chứa body
            if (response && typeof response.body === 'string') {
                try {
                    students = JSON.parse(response.body);
                } catch (e) {
                    console.error("Lỗi phân tích body:", e);
                    alert("Dữ liệu trả về không đúng định dạng JSON.");
                    return;
                }
            }
            // Kiểm tra nếu students là mảng
            if (Array.isArray(students)) {
                if (students.length === 0) {
                    alert("Không có dữ liệu sinh viên.");
                } else {
                    jQuery.each(students, function (i, data) {
                        $("#studentTable tbody").append(
                            `<tr>
                                <td class='p-4'>${escapeHTML(data.studentid)}</td>
                                <td class='p-4'>${escapeHTML(data.name)}</td>
                                <td class='p-4'>${escapeHTML(data.class)}</td>
                                <td class='p-4'>${escapeHTML(data.birthdate)}</td>
                                <td class='p-4'>${escapeHTML(data.email)}</td>
                            </tr>`
                        );
                    });
                }
            } else {
                console.warn("Dữ liệu trả về không phải mảng:", students);
                alert("Dữ liệu trả về không đúng định dạng.");
            }
        },
        error: function (xhr) {
            let errorMessage = "Không xác định";
            try {
                const error = JSON.parse(xhr.responseText || "{}");
                errorMessage = error.message || errorMessage;
            } catch (e) {
                errorMessage = xhr.responseText || errorMessage;
            }
            alert("Lỗi khi lấy dữ liệu sinh viên: " + errorMessage);
        }
    });
};

document.getElementById("backupstudents").onclick = function(){
    $.ajax({
        url: API_ENDPOINT + "/backup",
        type: 'POST',
        data: JSON.stringify({}),
        contentType: 'application/json',
        headers: {
            'x-api-key': API_KEY
        },
        success: function (response) {
            alert("Backup dữ liệu thành công! Kiểm tra email để tải file backup.");
        },
        error: function () {
            alert("Lỗi khi thực hiện backup dữ liệu.");
        }
    });
};