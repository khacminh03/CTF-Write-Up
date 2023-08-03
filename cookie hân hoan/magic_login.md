# Magic Login

![alt text](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364194964_825922548924350_3022196504351440967_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_ohc=xBc4s4zb5QQAX8SMXaY&_nc_ht=scontent.fhan5-8.fna&oh=03_AdQqgCHKY43L2T3HCu34Lq7T3TYqVjvkAu6SEE7heH8Zzg&oe=64F2D63A)

# Recon
Đầu tiên khi mở challenge lên thì mình có thể thấy rằng có hai chỗ để điền username và password
![alt text](https://scontent.xx.fbcdn.net/v/t1.15752-9/364186693_6413974692014236_2513235090293403284_n.png?_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_ohc=6w_tCgA_wkAAX_ASJFb&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRYAHDeM3LED5XGbhHdDIcr4az8vqhpzHg1ThgyJXkqnQ&oe=64F2B692)
  
Thử ctrl+U để xem mã nguồn của nó 
![alt text](https://scontent.xx.fbcdn.net/v/t1.15752-9/360034135_809648154002457_4970670844088211554_n.png?stp=dst-png_p206x206&_nc_cat=104&ccb=1-7&_nc_sid=aee45a&_nc_ohc=aGY-f32Lr-cAX8Ellz7&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTXe6HnTrL9Tzunk98MqckTdBYYeKwrdCb4pi7ICY9yIw&oe=64F2BC77)
  
Hừm giờ thì ta có thể hiểu đoạn code trên như sau 
- Đầu tiên người dùng sẽ nhập vào password và username được gửi đi dưới dạng POST
- Kiểm tra xem dữ liệu đã được chuyển đi hay chưa với hàm [isset](https://www.php.net/manual/en/function.isset.php)
- Nếu như có data ở trong ta sẽ lưu username vào trong biến **usr** với hàm [mysql_real_escape_string](https://www.php.net/manual/en/function.mysql-real-escape-string.php) hàm này có tác dụng để chống sql injection
- Lưu password và biến **pas** và hash với sha256 một loại hàm băm
- Nếu như **pas** bằng với "0" chuyển hướng đến trang **upload.php**
- Nếu không thì điều hướng lại về trang **login_page.php**

# Exploit
- Bằng việc đọc source code ta có thể thấy rằng phải tấn công vào biến pas phải có cách nào để nó đi vào được hàm **upload.php** nhưng làm thế nào để có thể tấn công vào trong hàm **pas** khi mà mọi ký tự ta điền vào đều bị hash bởi sha256 và việc có được một số 0 gần như là bất khả thi.
- Nhưng ta có thể thấy họ sử dụng **==** để so sánh trong khi ở php có tới hai loại so sánh đó chính là === và == việc sử dụng == có thể dẫn đến [php type juggling](https://viblo.asia/p/php-type-juggling-924lJPYWKPM)
- Khái quát một chút thì khi mà sử dụng == php sẽ đưa cả hai đối tượng so sánh về cùng một loại kiểu so sánh trong khi === thì sẽ chắc chắn khi mà kiểm tra cả kiểu dữ liệu và giá trị so sánh
- Như vậy ta có thể rút ra được thứ nhất ta cần phải có được một giá mà khi bị hash bởi sha256 php sẽ hiểu nhầm và đưa về thành "0"
- Bằng việc nhìn bảng dưới đây bạn cũng có thể hiểu rằng chúng ta cần phải tìm giá trị gì rồi đúng không?  
![alt text](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364192780_3564544020499843_7472861504372139481_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_ohc=eRiNojkZ_KQAX9I9G4i&_nc_ht=scontent.fhan5-8.fna&oh=03_AdRyYZMfNOqXKYBPpak-cpnKZHrdwnHFu_zyZDs2AGVlmQ&oe=64F2B8D3)
- Vậy là ta cần một loại giá  mà khi hash ra có 0e ở đầu giờ là lúc tra gg
- Mình tra với cú pháp **php type juggling sha256** và ngay lập tức tìm thấy trang payload all the things và thấy một thứ  ![alt text](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364192832_179996771635988_511217825745725636_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=isT3S7naFfYAX9jNNY-&_nc_ht=scontent.fhan5-8.fna&oh=03_AdRy9UtARl867Qw8OeXP78Tx36CBDyCInU-UZKvtCPFdMQ&oe=64F2CFDF)
- Sau khi điền vào thì mình được  ![alt text](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364194345_675800214059070_4590859495344496816_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=IsgMgViLD_MAX-28wo3&_nc_ht=scontent.fhan5-8.fna&oh=03_AdQa2dUsifG3EAsQ7s2dnlKUW_mXPj4bcDVpQLTgiyqa4w&oe=64F2D10A)
- Vậy là ta đã bypass được cái mật khẩu giờ là lúc upload một file shell lên thôi  
![alt text](https://scontent.xx.fbcdn.net/v/t1.15752-9/364189478_757160232878626_4745164926183181503_n.png?_nc_cat=108&ccb=1-7&_nc_sid=aee45a&_nc_ohc=SPkoEpxl5yEAX-_xdk1&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQ_TKwWNTchA5AVkOoueYbwVF2zAtiwPJrKkfdO4cHKjQ&oe=64F2D5F2)
-Bấm vào chữ **File** ta được  ![alt text](https://scontent.xx.fbcdn.net/v/t1.15752-9/364194384_829512038761370_954235771491743125_n.png?_nc_cat=107&ccb=1-7&_nc_sid=aee45a&_nc_ohc=eXR0TDKPF4AAX_l2VAp&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQo3pRbfUzEXexz0ek_us_T47BbjMmhYdtn3cZbOcaSVA&oe=64F2E467)
