# Suck It cookie arena

![](https://hackmd.io/_uploads/ryBBMxc2n.png)

## Recon
Ngay khi ta vừa vào ta có thể thấy một form để ta có thể điền tên của chúng ta vào

![](https://hackmd.io/_uploads/Hyvcfg923.png)

Ta có một vài user như sau

![](https://hackmd.io/_uploads/HJPTGgc2n.png)

Dựa vào đề bài ta có thể hiểu rằng mục tiêu duy nhất của chúng ta chính là người yêu của admin mà thôi

![](https://hackmd.io/_uploads/ry17Qx523.png)

Vậy là ta có thể thấy được nếu như không phải admin thì ta khó mà có thể nhận được flag nhưng làm thế nào để có thể trở thành admin đây mình để ý ở những chỗ khác nữa như là cookie hay userID hoặc là sessionID của người dùng có bị để lại trên trang web hay không những thứ này có thể giúp ta giả danh admin và hỗ trợ xâm nhập bằng việc bấm F12 vào đi vào trong local storage ta có thể thấy được một thứ như sau

![](https://scontent.fhan5-11.fna.fbcdn.net/v/t1.15752-9/367664530_1020808419103090_4433182304748664888_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=uIFs4va-4cEAX9fTrf9&_nc_oc=AQmXBXBaenQAjoKc4DqCZOq5L0W3thyUn0H_nADya5Yf5ZDdhTH3U6muvfzU7REVUnM&_nc_ht=scontent.fhan5-11.fna&oh=03_AdSI1KyPojEP8PlRqjmiLopEpXfaQIqPadRxhf8zLpy7Kg&oe=6503EF82)


Bằng việc kiểm tra trên burp suite ta cũng có thể thấy được

![](https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/367541526_1020839832246798_2697642732906250726_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_ohc=KMAJQ3VqqfQAX8sMjBb&_nc_ht=scontent.fhan5-8.fna&oh=03_AdRH2KSEltNRyHcrvaVtkqF7VSCfmqc0_gRxWH_veDBJoA&oe=6503F487)

Vậy là ta đã biết trang web đang lưu trữ sessionID của người dùng vậy thì giờ làm thế nào để có được sessionID của admin đây

## Exploit

Ta đến với việc phân tích source code được cung cấp sẵn để ý ở phần "force disconnect" ta có thể thấy được rằng

![](https://scontent.fhan5-9.fna.fbcdn.net/v/t1.15752-9/367539092_1508514069959055_7317403375801494682_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_ohc=Gd2A5SjaSKQAX9eWmbo&_nc_ht=scontent.fhan5-9.fna&oh=03_AdTjkfLbeHPXbDyDXcKvV4BiIsO8wKZr2ItPOBYyz1nxPA&oe=6503D6C7)

Thứ nhất là họ không phân quyền rõ ràng ta có thể thấy được rằng ai cũng có thể kick mọi người kể cả là user thông thường cùng với đó sau khi kick ra thì nó sẽ in ra userID của người đã bị kick vậy sẽ thế nào nếu như ta kick admin và lấy userID của admin để có thể giả danh người đấy

Nghĩ vậy mình liền thực hiện việc gọi event "force disconnect" ta sẽ chuyền vào đó với payload là

```bash=
42["force disconnect","ADMIN","574a94b04f303f5663e833b883cd2b23"]
```
Sau khi chạy thử payload như vậy ta đã có được sessionID của admin như sau

![](https://scontent.fhan5-11.fna.fbcdn.net/v/t1.15752-9/367612130_820815466120319_7493298921646128339_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_ohc=Tn3B_f77ZFoAX8srGNf&_nc_ht=scontent.fhan5-11.fna&oh=03_AdRjakfD5J4Hj-0lL6Ce8JLCrTdO6LsD1_patl3GWUnXuA&oe=6503F178)

Vậy là ta đã có sessionID của admin giờ chính là lúc mà ta thay đổi giá trị sessionID của chúng ta mà thôi

Vào trong local Storage và thay đổi sessionID của chính mình

![](https://scontent.fhan5-2.fna.fbcdn.net/v/t1.15752-9/365844286_772218434588753_7411851499380242790_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=A5fONxPsvBwAX_HB4Zv&_nc_ht=scontent.fhan5-2.fna&oh=03_AdQWgTBDJ0bq-LGaZFBJ1wYuHwiT1qYuLQMBgEv6nBJyDA&oe=65040492)

# Flag

![](https://scontent.fhan5-11.fna.fbcdn.net/v/t1.15752-9/366005883_865214761626560_9205414927878720230_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=9cnxxAmhh_4AX-n161g&_nc_ht=scontent.fhan5-11.fna&oh=03_AdQVgoH8dZlH-GWJ1c02OjgcUAPji4LUvrb3X0Bs2H56uA&oe=6503DB10)





