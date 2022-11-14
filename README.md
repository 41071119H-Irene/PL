# 111-1 師大科技系程式語言
***
 #### 授課教師： [蔡芸琤 Tsai, Yun-Cheng 老師](https://github.com/pecu?tab=repositories)
 #### 姓名：張乃云
 #### 系級：科技系2年級
***
# 目錄  

+ [**課程筆記**](https://github.com/41071119H-Irene/PL#pencil%E8%AA%B2%E7%A8%8B%E7%AD%86%E8%A8%98)
+ [**作業連結**](https://github.com/41071119H-Irene/PL#%E4%BD%9C%E6%A5%AD%E9%80%A3%E7%B5%90)
+ [**專題連結**](https://github.com/41071119H-Irene/PL#%EF%B8%8F%E5%B0%88%E9%A1%8C%E9%80%A3%E7%B5%90)

## :pencil:課程筆記
### week 1: Introduction
 * 生產力創新週期
 ![image](https://user-images.githubusercontent.com/112916890/190286800-1c6c537f-3b8c-494e-ac89-fd8eec616966.png)
 *  #### Why Coding?
   * 掌握電腦運作的邏輯>>運算思維
   * 動手解決問題的能力
 * 上課簡報: [1/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vS_11f3KIeNeqmInAKfHaDzOTxK_ff05aI3H3hanLX1qI6Z8iHhbOfqEUgl3Gzx3s1pYtjIZcdzECSP/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://www.youtube.com/watch?v=LiPvUoV-Dy4&feature=youtu.be)
 
### week 2: Basic Python 01
 * 資料型態:
   * int: 整數
   * float: 浮點數(包含小數點)
   * str: 字串 要加 "" 或 ''
   * bool: True/False
 * [開發者論壇(GeekforGeek)](https://www.geeksforgeeks.org/python-programming-language/)
 * [語法查詢工具(StackOverflow)](https://stackoverflow.co/)
 * [今日範例(領域:法律)](https://github.com/pecu/LawTech/tree/main/Learning-Materials/C1_Python_%E5%9F%BA%E7%A4%8E_01)
 * 上課簡報: [2/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vQa2_6HxpBPDUjViqvd82AqQfnywwWwETU60fLexCe7ADD8A7kHkpGjkmO6kCSYyw-AFrSCfG3THXiA/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=502948)
 
 ### week 3: Basic Python 02
 * [示範資料](https://github.com/pecu/PL/blob/main/Python02.ipynb)
 * [練習資料](https://github.com/pecu/LawTech/tree/main/Learning-Materials/C1_Python_%E5%9F%BA%E7%A4%8E_02)
 * 語法整理
    * List(ls) 串列 [,]
        * 最常見的數據形式，具順序
        * 印出資料裡面不同的元素，並聚集在一起
        * 有工具可以處理資料(.append()、del[]、.split())
    * Tuple 元組(,)
        * 安全版串列: 不能更動元素
        * 可放不同類型的資料
        * 具順序性
        * 兩邊數量不一樣的時候取較短的為主
           * zip 打包
           * *zip (unzip)解壓縮
    * Set 集合 {,}
        * 無順序，不可重複
        * 邏輯因子
           * '&' : 交集 s1.intersection(s2)
           * '|': 聯集 s1.union(s2)
           * '-' : 差集 s1.difference(s2)
           * '^' : 對稱差集(聯集-交集) s1.symmetric_difference(s2)
    * dict 字典 {key:value,ket:value}
        * 以鍵值方式儲存，元素不可重複
        * 可以放不同型態的資料
 * 上課簡報: [3/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vSAw9A5Eu_lHKzShkG8CacnBGk4xauhztCRro8AaxmllMd-gGR3iZpgeV2q8Yz4Fm7CRgfW7fmZSnTJ/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=508174)
 
 ### week 4: Basic Python 03
 * Dictionary
    * 較複雜的資料結構，但很好查詢
 * [課程練習](https://github.com/41071119H-Irene/PL/blob/main/Week4_Python_03.ipynb)
 * [練習資料](https://github.com/pecu/LawTech/tree/main/Learning-Materials/C2_Python_%E5%9F%BA%E7%A4%8E_03%2604)
 
  * 上課簡報: [4/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vRR3pc8mhMsa4xByYW6vKqtJiJCsAaeLLCvmRVf3RquXZDwY3yk0H9vcF3CGwkVh5ypqe5Yto0-E88d/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=512297)

### week 5: Basic Python 04
 * Json形式的資料-> 巢狀資料級
 * [Json Parser](http://json.parser.online.fr/)
 * [課程範例](https://github.com/pecu/PL/blob/main/HW2.ipynb)
 * [練習資料](https://github.com/pecu/PL/blob/main/Python03.ipynb)
 * 上課簡報: [5/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vRB9etAYcIULZFrawJ1_e1g_0jHvTSZMIBxzCbGMVSwaO92n-lf-T-4Ye9U6M0r25hqugHUI8smMPOZ/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=516152)

### week 6: Python 資料正則化(Regular Express)
 * 電腦標準符號表示(非結構化資料很需要!)
 * <爬蟲的前導>
 * [正規化文章](http://perso.ens-lyon.fr/lise.vaudor/strings-et-expressions-regulieres/?fbclid=IwAR0IHvNKp43Qrfo0TqpolYPpMUfViSrCBDY8SmBveKm01yZ6PzHPxspVaNI)
 * [課程範例](https://github.com/pecu/LawTech/blob/main/Learning-Materials/C3_Python_%E8%B3%87%E6%96%99%E6%AD%A3%E8%A6%8F%E5%8C%96/python_%E8%B3%87%E6%96%99%E6%AD%A3%E5%89%87%E5%8C%96_code.ipynb)
 * [課堂練習](https://github.com/pecu/LawTech/blob/main/Learning-Materials/C3_Python_%E8%B3%87%E6%96%99%E6%AD%A3%E8%A6%8F%E5%8C%96/python_%E7%AB%B6%E8%B3%BD%E7%A9%BA%E7%99%BD%E8%80%83%E9%A1%8C.ipynb)
 * [巢狀檢索檢查視覺化](https://jsoncrack.com/editor)
 * [視覺化模擬器-regExr](https://regexr.com/)
 * 上課簡報: [6/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vSKqly4jm5pdKscVPAGZvHkc-bfGa3X0P5SYGTIv0HoOTLfV94L7UVWcWnchhdRUTTsEYVqlyQ0wi23/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=518934)

### Week 7: Python 網路爬蟲
 * [PPT爬蟲教學影片](https://youtu.be/9Z9xKWfNo7k)
 * 上課簡報: [7/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vSIQhAt8wK9K6tgOx9xCsg8cVjZSXgH8Q-whPekB0Zi68fCTwJvmQ_XeJAfrLdohB_jMDn_mblxWCtC/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=522340)

### Week 8: Python PYTHON 資料彙整、資料視覺化
 * 資料彙整(pandas 套件)
     * 套件介紹
     * 初步欄位處理(觀察資料、文字切割處理、dataframe新增欄位)
     * loc、iloc函數介紹(+練習題)
     * str.contains函數解紹(+練習題)
     * 欄位處理
     * apply、lambda函數介紹(+練習題)
 * 資料視覺化
     * [Plotly](https://plotly.com/python/)
 * [課程資料]([https://youtu.be/9Z9xKWfNo7k](https://github.com/pecu/LawTech/tree/main/Learning-Materials/C5_Python_%E8%B3%87%E6%96%99%E5%BD%99%E6%95%B4%26%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96))
 * 上課簡報: [8/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vR0lsj6suoMW-s48VLVaWeXB2vXwcPmvX2jKpXOCuZuEry3VMyAlapumD20gt1DUPiMIT6krRjZba3P/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://moodle3.ntnu.edu.tw/mod/page/view.php?id=525096)
 
 ### Week 9: PYTHON 文字探勘
 * [文字探勘教學](https://www.youtube.com/watch?v=HGPPoaBxyb0&feature=emb_imp_woyt)
 * [練習資料](https://github.com/pecu/LawTech/tree/main/2021LawTech/Learning-Materials/C6_Python_%E6%96%87%E5%AD%97%E6%8E%A2%E5%8B%98)
 * 上課簡報: [9/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vS-XoNDMEDtxpfenW3dO9rkpeGKX0TbF2IfBP-Q7g4mbUft--2lynYvZ9MPej10k0xKub2ekj-mD_DY/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播](https://www.youtube.com/watch?v=YYoZXoOftK0)
 ### Week 10: 鱸魚 - 矽谷觀察家縮矽谷
 ### Week 11: Python 文本共現網路分析/如何開創自己的路 
 * [TradingTrain鎚圈-技術分析交易訓練首選品牌](https://www.tdtn.tw/)
 * 上課簡報: [11/16 程式語言](https://docs.google.com/presentation/d/e/2PACX-1vQkAyFp8CqGYo1cb58Sv3Ba-glwkMsqbcQ-G5BFsLVm_wmRNCIpGWgiATFoV_MSUJRy7NsmNXtOP9qo/pub?start=false&loop=false&delayms=3000&slide=id.p)  [上課直播]()

## 🙌作業連結
> ### Week2
>> #### [Python_01練習](https://github.com/41071119H-Irene/PL/blob/main/Week2_python_01.ipynb)
> ### Week3
>> #### [Python_02練習](https://github.com/41071119H-Irene/PL/blob/main/Week3_python_02.ipynb)
>> #### [作業一-課程缺席尋找器兼資料處理的使用](https://github.com/41071119H-Irene/PL/blob/main/Week3_Homework_01.ipynb)
> ### Week4
>> #### [Python_03練習](https://github.com/41071119H-Irene/PL/blob/main/Week4_Python_03.ipynb)
> ### Week5
>> #### [Python_04練習](https://github.com/41071119H-Irene/PL/blob/main/Week5_Python04.ipynb)
>> #### [作業二-資料變字典](https://github.com/41071119H-Irene/PL/blob/main/Week5_Python04(HW2).ipynb)
> ### Week6
>> #### [Python 規則正規化](https://github.com/41071119H-Irene/PL/blob/main/Week6_Python%20Regular%20Express.ipynb)
> ### Week7
>> #### [作業三-爬蟲套件(PTT新竹版標題)](https://github.com/41071119H-Irene/PL/tree/main/HW3%20python%20crawl)
> ### Week9
>> #### [作業四-文字探勘Medium](https://medium.com/@irene9227/文字探勘的強大-從google評論分析於師大附近最受歡迎的飲料店並深入探討此飲料店為何受歡迎-c1e8b27a7158)
>> #### [作業四-文字探勘程式碼](https://github.com/41071119H-Irene/PL/blob/main/Week9_HW4_Drinks.ipynb)

## 📽️專題連結
### 主題
### 想解決的問題
### 
