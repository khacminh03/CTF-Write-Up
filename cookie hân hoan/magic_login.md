# Magic Login

Đầu tiên khi mở challenge lên thì mình có thể thấy rằng có hai chỗ để điền username và password:
![Magic Login](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364194964_825922548924350_3022196504351440967_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_ohc=xBc4s4zb5QQAX8SMXaY&_nc_ht=scontent.fhan5-8.fna&oh=03_AdQqgCHKY43L2T3HCu34Lq7T3TYqVjvkAu6SEE7heH8Zzg&oe=64F2D63A)

# Recon
Đầu tiên, khi mở challenge lên, ta có thể thấy có hai chỗ để điền username và password.

![Magic Login Form](https://scontent.xx.fbcdn.net/v/t1.15752-9/364186693_6413974692014236_2513235090293403284_n.png?_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_ohc=6w_tCgA_wkAAX_ASJFb&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRYAHDeM3LED5XGbhHdDIcr4az8vqhpzHg1ThgyJXkqnQ&oe=64F2B692)

Thử ctrl+U để xem mã nguồn của nó.

![Source Code](https://scontent.xx.fbcdn.net/v/t1.15752-9/360034135_809648154002457_4970670844088211554_n.png?stp=dst-png_p206x206&_nc_cat=104&ccb=1-7&_nc_sid=aee45a&_nc_ohc=aGY-f32Lr-cAX8Ellz7&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTXe6HnTrL9Tzunk98MqckTdBYYeKwrdCb4pi7ICY9yIw&oe=64F2BC77)

Hừm, giờ thì ta có thể hiểu đoạn code trên như sau:
- Đầu tiên, người dùng sẽ nhập vào password và username được gửi đi dưới dạng POST.
- Kiểm tra xem dữ liệu đã được chuyển đi hay chưa với hàm [isset](https://www.php.net/manual/en/function.isset.php).
- Nếu như có data trong POST, ta sẽ lưu username vào trong biến **usr** với hàm [mysql_real_escape_string](https://www.php.net/manual/en/function.mysql-real-escape-string.php). Hàm này có tác dụng để chống SQL injection.
- Lưu password vào biến **pas** và hash với sha256, một loại hàm băm.
- Nếu như **pas** bằng "0", chuyển hướng đến trang **upload.php**.
- Nếu không, điều hướng lại về trang **login_page.php**.

# Exploit
- Bằng việc đọc source code, ta có thể thấy rằng phải tấn công vào biến **pas**. Để có thể tấn công vào biến **pas**, khi mà mọi ký tự ta điền vào đều bị hash bởi sha256 và việc có được một số 0 gần như là bất khả thi.
- Nhưng ta có thể thấy họ sử dụng **==** để so sánh trong khi ở PHP có tới hai loại so sánh đó chính là === và ==. Việc sử dụng == có thể dẫn đến [php type juggling](https://viblo.asia/p/php-type-juggling-924lJPYWKPM).
- Khái quát một chút thì khi mà sử dụng ==, PHP sẽ đưa cả hai đối tượng so sánh về cùng một loại kiểu so sánh, trong khi === sẽ chắc chắn kiểm tra cả kiểu dữ liệu và giá trị so sánh.
- Như vậy ta có thể rút ra được, thứ nhất, ta cần phải có một giá trị mà khi bị hash bởi sha256, PHP sẽ hiểu nhầm và đưa về thành "0".
- Bằng việc nhìn bảng dưới đây, bạn cũng có thể hiểu rằng ta cần tìm giá trị gì:

![PHP Type Juggling](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364192780_3564544020499843_7472861504372139481_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_ohc=eRiNojkZ_KQAX9I9G4i&_nc_ht=scontent.fhan5-8.fna&oh=03_AdRyYZMfNOqXKYBPpak-cpnKZHrdwnHFu_zyZDs2AGVlmQ&oe=64F2B8D3)

- Vậy là ta cần một giá trị mà khi hash ra có 0e ở đầu. Giờ là lúc tra gg.
- Mình tra với cú pháp **php type juggling sha256** và ngay lập tức tìm thấy trang [payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings) và thấy một thứ:

![PHP Type Juggling Payload](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364192832_179996771635988_511217825745725636_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=isT3S7naFfYAX9jNNY-&_nc_ht=scontent.fhan5-8.fna&oh=03_AdRy9UtARl867Qw8OeXP78Tx36CBDyCInU-UZKvtCPFdMQ&oe=64F2CFDF)

- Sau khi điền vào thì mình được:

![Bypassed Login](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364194345_675800214059070_4590859495344496816_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=IsgMgViLD_MAX-28wo3&_nc_ht=scontent.fhan5-8.fna&oh=03_AdQa2dUsifG3EAsQ7s2dnlKUW_mXPj4bcDVpQLTgiyqa4w&oe=64F2D10A)

- Vậy là ta đã bypass được cái mật khẩu. Giờ là lúc upload một file shell lên thôi.

![Upload Shell](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/364189478_757160232878626_4745164926183181503_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=SPkoEpxl5yEAX_cWIg6&_nc_ht=scontent.fhan5-8.fna&oh=03_AdRagU9Y_hfdM3-_OF543dqX_Sgyu31mnCW1WAg9YIXl6g&oe=64F2D5F2)

Bấm vào chữ **File** ta được:

![File Page](https://scontent.xx.fbcdn.net/v/t1.15752-9/364194384_829512038761370_954235771491743125_n.png?_nc_cat=107&ccb=1-7&_nc_sid=aee45a&_nc_ohc=eXR0TDKPF4AAX_l2VAp&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQo3pRbfUzEXexz0ek_us_T47BbjMmhYdtn3cZbOcaSVA&oe=64F2E467)

