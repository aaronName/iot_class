# iot_class
## 專案簡介:
	這是一個可以控制車子行走方向的專案。
## 所需材料:
	Raspberry pi
 	L298N馬達驅動板
	減速直流馬達*4
   	ST-2WD智能小車底盤*2
   	車輪*4
   	4節五號電池盒*1
   	1.5V電池*4
   	方向輪*1
   	M330x螺絲4
   	M36螺絲8
   	M3螺帽*8
   	L12銅柱*4
   	塑膠殼、雙面膠、行動電源
![l298n](https://github.com/user-attachments/assets/09a8252d-c26e-4307-8d96-a9a346536354)
 ## 串聯Raspberry pi 與 L298N 馬達控制器
 	1. 將輸出A左邊的螺絲接到右後方的馬達上，輸出A右邊的螺絲接到右前方的馬達上。//馬達控制輪子
  	2. 將輸出B左邊的螺絲接到左前方的馬達上，輸出A右邊的螺絲接到左後方的馬達上。
	3. 將電池盒的正極(紅線)接到+12V電源輸入孔，電池盒的負極(黑線)接到GND電源地。
	4. 將樹莓派接地的針腳(如針腳6, 9, 14, 20, 25, 30, 34, 39等)接到GND電源地，並將樹莓派提供5V的針腳(如針腳2, 4等)接到+5V電源輸入孔。
 	5. 將IN1, IN2, IN3, IN4依序接到樹莓派的針腳11, 12, 15, 16(分別對應GPIO17, GPIO18, GPIO22, GPIO23，可根據程式碼自行更改針腳)。
 ## 如何跑程式碼
 	1. 在樹莓派裡開啟資料夾，並執行test.py檔案。
	2. 在terminal中，會顯示一個網址，點開來之後就可以看到一個簡易版的遙控頁面。(此程式碼在templates資料夾中的index.html)
	3. 點擊頁面上相對應的指令(GO, BACK, STOP, TURN RIGHT, TURN LEFT)即可讓自走車移動。
 ## 資料來源
 	1. Raspberry使用L298N操作兩個馬達: https://sites.google.com/view/zsgititit/home/%E7%A1%AC%E9%AB%94%E5%AF%A6%E4%BD%9C/raspberry-shu-mei-pai/raspberry-shi-yongl298n-cao-zuo-liang-ge-ma-da
 	2. WiFi遙控車教學: https://hackmd.io/@q4-u6PwwT3-1Z4jbOLzyGA/ryTC1S_9o
  	3. Arduino使用L298N驅動兩個馬達: https://sites.google.com/view/zsgititit/home/%E7%A1%AC%E9%AB%94%E5%AF%A6%E4%BD%9C/arduino/arduino-shi-yongl298n-qu-dong-liang-ge-ma-da
	4. Github上Readme的基本撰寫和格式寫法: https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
	5. Git版本控制: https://ithelp.ithome.com.tw/articles/10271811
