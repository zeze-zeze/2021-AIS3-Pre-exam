# REVERSE - COLORS
## 找到原始碼
看個網頁原始碼，底下有個 js 檔案，載下來後用 Javascript Beautifier 整理一下，發現是有混淆過的 js

## 理解程式邏輯
先把一些混淆的部分，還有被 base64 encode 的部分還原回去，可以得到下面這個原始碼
```
if (_0x23e75c['key'] === "Backspace" && _0x179193 == 0xa) _0x1e21d9["textContent"] = _0x1e21d9['textContent']["substr"](0x0, _0x1e21d9['textContent']["length"] - 0x1);
else {
    if (_0x23e75c['key'] === "ArrowUp" && !(_0x179193 >> 0x1)) return _0x179193 += 0x1;
    else {
        if (_0x23e75c[recur(0x1e5)] === 'ArrowDown' && !(_0x179193 >> 0x2)) return _0x179193 += 0x1;
        else {
            if (_0x23e75c[recur(0x1e5)] === "ArrowLeft" && (_0x179193 == 0x4 || _0x179193 == 0x6)) return _0x179193 += 0x1;
            else {
                if (_0x23e75c[recur(0x1e5)] === 'ArrowRight' && (_0x179193 == 0x5 || _0x179193 == 0x7)) return _0x179193 += 0x1;
                else {
                    if (_0x23e75c[recur(0x1e5)] === 'b' && _0x179193 == 0x8) return _0x179193 += 0x1;
                    else {
                        if (_0x23e75c['key'] === 'a' && _0x179193 == 0x9) return document["getElementByTagName"]("body")[0x0]['innerHTML'] += atob(_0x54579e), _0x1e21d9 = document["getElementById"](input), _0x1e21d9["innerHTML"] = '', document["getElementById"]('output')["innerHTML"] = atob(_0x78ed5a)["match"](/(.{1,3})/g)["map"](_0x5efa9e => _0x9f530c(_0x5efa9e[0x0], _0x5efa9e[0x1], _0x5efa9e[0x2]))["join"](''), _0x179193 += 0x1;
                        else {
                            if (_0x23e75c["key"]["length"] == 0x1 && _0x179193 == 0xa) _0x1e21d9["textContent"] += String['fromCharCode'](_0x23e75c["key"]["charCodeAt"]());
                            else return;
                        }
                    }
                }
            }
        }
    }
}
```

可以知道按「上上下下左右左右 b a」會顯示出很多 encode 過的東西，然後就要想辦法 decode

## Decode
看看其中的一段原始碼
```
function _0xce93(_0x1b497a) {
    const recur = recur;
    if (!_0x1b497a["length"]) return '';
    let _0x4d62de = '',
        _0x23f867 = '',
        _0x5395cb = 0x0;
    for (let _0x6e40b4 = 0x0; _0x6e40b4 < _0x1b497a["length"]; _0x6e40b4++) _0x4d62de += _0x1b497a[recur(0x1dc)](_0x6e40b4)['toString'](0x2)[recur(0x1c6)](0x8, '0');
    _0x5395cb = _0x4d62de[recur(0x1d0)] % _0x317b6e / 0x2 - 0x1;
    if (_0x5395cb != -0x1) _0x4d62de += '0' [recur(0x1c8)](_0x317b6e - _0x4d62de[recur(0x1d0)] % _0x317b6e);
    _0x4d62de = _0x4d62de[recur(0x1e4)](/(.{1,10})/g);
    for (let _0x13c6bb of _0x4d62de) {
        let _0x192141 = parseInt(_0x13c6bb, 0x2);
        _0x23f867 += _0x9f530c(_0x192141 >> 0x6 & 0x7, _0x192141 >> 0x9, atob(_0x24fcac)[_0x192141 & 0x3f]);
    }
    for (; _0x5395cb > 0x0; _0x5395cb--) {
        _0x23f867 += _0x9f530c(_0x5395cb % _0x2a3765, 0x0, '=');
    }
    return _0x23f867;
}
```

這部分是產生網頁 html 的 \<span\> 的 class 的 rX cY 還有中間的字元產生的邏輯，最左邊 1 bit 是 r，接下來 3 bit 是 c，剩下是從 `AlS3{BasE64_i5+b0rNIng~\\Qwo/-xH8WzCj7vFD2eyVktqOL1GhKYufmZdJpX9}` 中取出第剩下的 bit 的 index 的字元

## 寫程式
所以就把網頁原始碼的 cX 跟 rY 還有中間的字元記下來後逆回去就是 flag 了
```
import string

table = 'AlS3{BasE64_i5+b0rNIng~\\Qwo/-xH8WzCj7vFD2eyVktqOL1GhKYufmZdJpX9}'
encoded = 'BgiJ6\\w1Aj\\1guikl7xiXKIhXKil6fo65Kn87B-8warzK==='
flag = '' # 5 * n + 1
index = []
for e in encoded:
    for i in range(len(table)):
        if e == table[i]:
            index.append(i)

print(index)

cs = [4, 2, 3, 5, 6, 0, 3, 4, 3, 4, 4, 4, 3, 7, 3, 1, 3, 4, 6, 5, 5, 1, 1, 4, 5, 0, 4, 5, 7, 7, 4, 1, 5, 7, 1, 5, 7, 4, 5, 1, 4, 3, 1, 4, 7, 3, 2, 1]

rs = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]

assert len(cs) == len(encoded) and len(rs) == len(encoded)

bits = ''
for i in range(len(index)):
    b = index[i] + (cs[i] << 6) + (rs[i] << 9)
    bits += bin(b)[2:].rjust(10, '0')

flag = ''
for i in range(0, len(bits), 8):
    flag += chr(int(bits[i:i+8], 2))
print(flag)
```

* flag: `AIS3{base1024_15_c0l0RFuL_GAM3_CL3Ar_thIS_IS_y0Ur_FlaG!}`
