# Amongsus-api
![Task](https://hackmd.io/_uploads/SkPMSNaj3.png)

## Recon

![](https://hackmd.io/_uploads/rJgqLBNTin.png)
- Đầu tiên khi vừa mới vào trong bài ta có thể thấy được một đoạn json được in ra cho người dùng ngoài ra thì không còn gì khác nên chúng ta sẽ phân tích source code và exploit luôn

## Exploit

- Bài có cung cấp source code cho chúng ta nên hãy phân tích nó một cách cẩn thận

![](https://hackmd.io/_uploads/HJHl8ETih.png)

- Các import bao gồm request, jsonify cùng với đó là sử dụng database là sqlite3
- Đầu tiên kết nối với database rồi tạo bảng users với id, username, sus
- Ở hàm index đầu tiên ta có thể thấy một **anotation** là với route là '/' sử dụng phương thức **GET**
- Hàm **index()** trả về một đoạn json ngay khi ta vừa mới mở trang web lên nên hãy chuyển sang hàm khác
![](https://hackmd.io/_uploads/SJWzONpi3.png)
- Ở hàm thứ hai với route là **/signup** sử dụng phương thức **POST** việc sử dụng **url + /signup** sẽ không có hiệu quả do chúng ta đang sử dụng phương thức **GET** nên sẽ nhận về màn hình báo lỗi **method not support** không còn cách nào khác ta sẽ sử dụng postman (trên discord) theo như gợi ý của đề bài
- Cùng với đó ta phải đăng ký **username** và **password** để có thể thực hiện câu lệnh sql nữa
![](https://hackmd.io/_uploads/HkaDqE6ih.png)
- Ở hàm tiếp theo
![](https://hackmd.io/_uploads/SyzT5VTj3.png)
- Hàm login được điều hướng đến trang **/login** ta có thể thấy biến **username** và **password** được truyền đi bởi phương thức **POST** câu lệnh **SELECT** để lấy các data được lưu trữ trong database và tạo một token một các ngẫu nhiên bởi các ký tự ASCII in hoa và các số nếu như ta đăng nhập thành công ta sẽ được biết **token** của ta là gì
![](https://hackmd.io/_uploads/BJ0P3Naon.png)
- Giờ ta đã có **token** giờ là lúc đi đến trang **/account**
![](https://hackmd.io/_uploads/Syps2Epin.png)
- Sử dụng phương thức **GET** nhưng lần này ta phải lấy cả trường [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) và bên trong trường Arthorization này cũng phải chứa "Bearer " đây chính là lúc postman tỏa sáng
![](https://hackmd.io/_uploads/HyPF64ajn.png)
- Giờ chỉ còn tìm cách để đọc flag thôi
![](https://hackmd.io/_uploads/SyypTVTj3.png)
- Giờ thì ta có thể thấy được để có thể đọc flag cần phải có sus là 1 trong khi ngay khi vừa mới tạo tài khoản ta có thể thấy rằng sus của tài khoản đã bị mặc định là 1 nên là không còn cách nào khác ta sẽ triển khai **sql injection** do dễ dàng thấy được rằng không có filter ở những chỗ nhạy cảm như là **username** hay **password** nên ta có thể dễ dàng triển khai **sql injection** ở phần **/account/update**
![](https://hackmd.io/_uploads/HJLrgHTjn.png)
- **sql injection** đã thành công và đừng quên việc gửi cả **Authorization** nhé
- Giờ ta chỉ còn việc đọc flag thôi

## Flag
![](https://hackmd.io/_uploads/SyCebHpo2.png)



