import httpx
import time
import random
from fake_useragent import UserAgent

url = input("网址  :")

k= int(input("次数："))


p=str(input("代理："))


with httpx.Client(proxies=p) as client:
    pass


user_agent = UserAgent()
req_header = {
'User-Agent':user_agent.random
}

start_time = time.time()

while k>0 :
    k=k-1
    r=httpx.get(url,headers=req_header)
    print(r)

end_time = time.time()
print(f'it cost {round(end_time - start_time, 4)}s.')