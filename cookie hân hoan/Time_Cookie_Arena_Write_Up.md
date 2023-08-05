# Time

![Task](https://scontent.fhan5-2.fna.fbcdn.net/v/t1.15752-9/364397617_1308534343368004_2757974093169274383_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=FfzZiGsFCZQAX8z9ag8&_nc_ht=scontent.fhan5-2.fna&oh=03_AdTTtOggBj1jXQjcqRMuiRiS9muJ1TLKtuZN0a0Jl0EQJw&oe=64F556A0)

Chúng ta cũng được cung cấp source code để làm bài nữa mình có phân tích source code mọi người có thể xem ở [đây](https://github.com/khacminh03/CTF-Write-Up/blob/main/cookie%20h%C3%A2n%20hoan/Time_cookie_arena_code_analyze.docx)

## Recon
- Đầu tiên khi vào trang web ta có thể thấy 
![first function](https://scontent.fhan15-2.fna.fbcdn.net/v/t1.15752-9/364399779_983047146360966_2341224856252512007_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=SEGmK_sxf7kAX9LaDhv&_nc_ht=scontent.fhan15-2.fna&oh=03_AdSGEPZYIBc3YNQRyoweqsROotjBkTuhBSCwB1dp90cX2A&oe=64F55352)
- Khi bấm vào phần **What's the date?** thì ta được
![second function](https://scontent.fhan5-10.fna.fbcdn.net/v/t1.15752-9/364399259_512507744373167_3032747864021954477_n.png?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_ohc=VfKLR29DZQIAX-tRruO&_nc_ht=scontent.fhan5-10.fna&oh=03_AdTWt2SjQHU0SlguNg1P0bQ_CtBdLps-lZ4C-Dclat6rbQ&oe=64F58821)
- Như vậy ta có thể thấy được rằng có hai nơi để ta có thể tấn công đó chính là phần format của date hoặc là time

## Exploit
- Do đề bài là command injection nên là việc ưu tiên của chúng ta là tìm đến những phần mà có những hàm như [exec()](https://www.php.net/manual/en/function.exec.php) hoặc là [shell_exec()](https://www.php.net/manual/en/function.shell-exec.php) cả hai đều là những hàm cho phép thực thi câu lệnh của hệ điều hành
- Sau khi đảo qua các file thì mình để ý ở file **TimeModel.php** 
![TimeModel.php](https://scontent.fhan15-1.fna.fbcdn.net/v/t1.15752-9/364630073_801688951614705_8004183364970877404_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_ohc=wi5z4XFUgwYAX_vWtof&_nc_ht=scontent.fhan15-1.fna&oh=03_AdSsgnWStzQwwX28HFYLK6sRRKsktfYUtJgXPQd0A2HV8Q&oe=64F55A3F)
- Từ đoạn code trên có thể thấy được biến hàm **_construct** được chuyền vào tham số **$format** với định dạng là **date + '$format'** lưu ở biến **$command**
- Ở hàm **getTime()** biến **$time** sẽ thực thi biến command và ngay lập tức ta có thể thấy được lỗ hổng đó chính là không filter nên là ta có thể dễ dàng triển khai payload mà không lo bị filter quá nhiều
- Nhưng làm thế nào để có thể escape được dấu ngoặc khi mà nó sẽ bị lưu dưới định dạng là **date + '$format'** sau một hồi vắt óc ra để mà nghĩ thì mình có một ý tưởng như này ta sẽ sử dụng payload như sau **date +'$format + '; os command + '**
- Bằng việc sử dụng payload trên ta có thể chèn được os command vào trong hệ thống chẳng hạn như bạn muốn thực thi lệnh **ls** đi thì với payload trên nó sẽ thành **date + '2023-08-05'; ls''**
- Sau khi đã có hướng đi giờ là lúc bắt đầu exploit bài này các bạn không nhất thiết phải mở Burp Suite lên mà chỉ cần dùng mỗi url là đủ rồi mình sẽ sử dụng lệnh cat /*flag.txt

## Flag
![Flag](https://scontent.fhan5-11.fna.fbcdn.net/v/t1.15752-9/364436773_800488901755956_7236136658289762713_n.png?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_ohc=-m8OE_P1Y3MAX_QVwfT&_nc_ht=scontent.fhan5-11.fna&oh=03_AdT2DCwDRpJs0IbY2eV5qlBbq6LbTd2OrNxX-bME0t_bLg&oe=64F58FFB)
