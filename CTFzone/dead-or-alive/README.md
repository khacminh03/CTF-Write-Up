# Dead or alive
![](https://hackmd.io/_uploads/H15EtDL22.png)
## Recon
![](https://hackmd.io/_uploads/HkPvFPIn2.png)
Ngay khi mở challenge lên ta có thể thấy được một trang web cực đẹp ở đây nhưng cái chúng ta cần quan tâm nhất chính là việc điền thông tin ban đầu khi mà mình thử điền các thông tin như trên rồi bấm submit thì mình được

![](https://hackmd.io/_uploads/B1t6KDU22.png)

Cũng hay đấy nhưng khi mình đưa vào trong burp suite và thử kiểm tra các request thì đáng chú ý nhất là có tới 3 request dạng POST được gửi đi

![](https://hackmd.io/_uploads/r1bXcwL33.png)
Ta có thể thấy được các dữ liệu được chuyển đi dưới dạng json nhưng ở hàm setSymptoms ta có thể thấy

![](https://hackmd.io/_uploads/SyFK9vI3n.png)
Symptoms là rỗng vậy tại sao mình không thử setSymptoms theo ý muốn nhỉ
## Exploit
Mình quyết định thử symptoms = "dead" để xem hệ thống có hoạt động như ý không và kết qủa thật kỳ lạ
![](https://hackmd.io/_uploads/ryN1swLh2.png)

Nó updated thành công vậy lần này khi mình thử đi qua chỗ getDiagnosis để nhìn xem mình được gì rồi thì thấy 
![](https://hackmd.io/_uploads/SJkvjv8h3.png)

## Flag
![](https://hackmd.io/_uploads/Hk9DjwL3n.png)
