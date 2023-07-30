import requests
import logging
import os
from urllib.request import urlopen #request someting from a server
from bs4 import BeautifulSoup #to scrap something from xml, html pages, if not present in our pakage then instal it using pip instal bs4

save_dir = "\Images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

query="Shri Hari"
url=f"https://www.google.com/search?q={query}&rlz=1C1CHZL_enIN850IN884&tbm=isch&sxsrf=AB5stBg6sUyNgUHeQM-7fq-yVit5Z7zjJQ:1690737984328&source=lnms&sa=X&ved=2ahUKEwj799rn-baAAxVXafUHHcBnCGgQ_AUoAnoECAIQBA&biw=1366&bih=625"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")
image_tags=soup.find_all("img")
del image_tags[0]
image_tags
len(image_tags)
for i in image_tags:
  image_url=i['src']
  image_data=requests.get(image_url).content
  with open(os.path.join(save_dir,f"{query}_{image_tags.index(i)}.jpg"),"wb") as f:
            f.write(image_data)