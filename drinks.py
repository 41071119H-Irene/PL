# 抓取留言

#引入函式庫
import json

import requests
from pandas import json_normalize
import pandas as pd
# 超連結
url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758629526904009!2y3122492267182977036!2m1!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1snpZwY-zWDsHbhwPLmarYDQ!7e81'
    
# 發送get請求
text = requests.get(url).text
# 取代掉特殊字元，這個字元是為了資訊安全而設定的喔。
pretext = ')]}\''
text = text.replace(pretext,'')

# 把字串讀取成json
soup = json.loads(text)
# 取出包含留言的List 。
conlist = soup[2]

temp = []
# 逐筆抓出
for i in conlist:
    temp.append(i[3])
df = pd.DataFrame(temp)

df['seg'] = ""
df.head()
print(df.head())