# where-are-the-cookies
![Task](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/364622127_306223381765243_8511137178455976808_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=Ub_Ej9OXGUsAX_mKxTr&_nc_ht=scontent.fhan2-3.fna&oh=03_AdTiVQp5snw8lQZ8eDxjAFpOe_KUZEgN5WEVVuc8CX1Iug&oe=64F5D97A)

## Recon
- Ngay khi vừa mới mở đề bài thì ta có
![First page](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/364627230_2367809206732847_3474583458200614512_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=wkqU2ANWCuAAX8lPKpc&_nc_oc=AQl1Les031aUdHzO8LjbbHX6lCnt0w7OqzquoU3AV24GA0Zr7Dgpc5Svevs1rfY5MEAWRtkkFxWmER-eQk5jY13k&_nc_ht=scontent.fhan2-3.fna&oh=03_AdTQmbof_cGaRZk2JLb7TxXAgkcWf2ekM2CN65JT2ga30g&oe=64F5C562)
- Do đề bài yêu cầu sử dụng đến cookie nên mình sẽ **F12** và bấm vào **application** để xem các cookie hiện tại ta có như sau
![cookie](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/364677612_167934432974752_5671879333032443357_n.png?_nc_cat=101&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=bb6XGroxQwkAX_mm5Hc&_nc_ht=scontent.fhan2-3.fna&oh=03_AdQM9SHJbhffStdE5h4Tl79djXE4m7yOgUJNaBYMPnxklw&oe=64F5C693)
- Khi ta bấm vào đó thì ta có hai cookie nhưng cả hai cái này đều không có giá trị gì quá nhiều nên mình sẽ đi theo một hướng khác đó chính là tìm các subdomain bị ẩn công cụ mình sử dụng ở đây là [dirsearch](https://www.kali.org/tools/dirsearch/)
- Sử dụng lệnh
```bash
dirsearch -u https://ch29511127626.ch.eng.run/
```
- Kết quả khi chạy
![Result](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/359754911_133492429801265_758271144220332388_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=66ne3V2f7EMAX9RgK7D&_nc_ht=scontent.fhan2-5.fna&oh=03_AdSEtP8faN3Z5Ker52oHD4Lx9XUjbvD4zR2G6jDbjYmzfA&oe=64F5E20C)
## Exploit
- Giờ ta đã biết rằng trang web đang có một file robots.txt đang mở file robots.txt
- Sau khi truy cập vào file robots.txt ta được
![Result with robots.txt](https://scontent.fhan2-5.fna.fbcdn.net/v/t1.15752-9/364534659_304616138637236_6876599798604413206_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=PGa2-pcC3lMAX8PYW3G&_nc_ht=scontent.fhan2-5.fna&oh=03_AdRIeCz46FM8UqEE0sBGt1a52mPmPFy2MSmQIyIRaymM9g&oe=64F5E777)
- Truy cập vào trong trang **/cookiesaretotallynothere**
![Result](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/364545482_839430440663807_7410763271374129603_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=MO37WjQUhHwAX_mgX9I&_nc_ht=scontent.fhan2-4.fna&oh=03_AdSwEbbXNftAo-ThHwuq3GmicET4VZcNDyQLR38rB-L4Hw&oe=64F5EF6F)
- Lại F12 lên để tìm cookie ta có thể thấy
![Cookie](https://scontent.fhan2-4.fna.fbcdn.net/v/t1.15752-9/364639363_203200412429274_6395145242425343333_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=v4jH1PtfPvIAX899o79&_nc_ht=scontent.fhan2-4.fna&oh=03_AdQR9rXIMNxzefNFe_OKUb21p_QsyZV8OgpmlLfYkx4ZmA&oe=64F5DF5F)
- Sử dụng base64 để decode ta biết được rằng chữ **bm8==** tương đương với chữ **no**
- Vậy thì giờ chỉ cần đổi thành chữ **yes** ở dạng base64 thôi như vậy nó sẽ thành **eWVz**
## Flag
![Flag](https://scontent.fhan2-3.fna.fbcdn.net/v/t1.15752-9/364677608_1948957145491671_5573175702605852607_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_ohc=OCc_Qbvl98UAX-HIusn&_nc_ht=scontent.fhan2-3.fna&oh=03_AdRWXFzCVOSmqsXyn2D33c3ndJ6-6E21NCoO3O6VioT6Sw&oe=64F5C12E)