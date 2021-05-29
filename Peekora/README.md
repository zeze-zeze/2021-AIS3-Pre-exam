# REVERSE - Peekora
## 轉成 Assembly
可以用 [pickletools](https://docs.python.org/3/library/pickletools.html) 把 .pkl 逆回 symbolic disassembly

## 讀程式
opcode 可以在網路上找到[教學](https://intoli.com/blog/dangerous-pickles/)

例如下面這一段的意思就是 flag[6] = 'A'
```
208: (    MARK
209: g        GET        1
212: (        MARK
213: g            GET        1
216: (            MARK
217: g                GET        0
220: S                STRING     '__getitem__'
235: t                TUPLE      (MARK at 216)
236: R            REDUCE
237: (            MARK
238: I                INT        6
241: t                TUPLE      (MARK at 237)
242: R            REDUCE
243: S            STRING     '__eq__'
253: t            TUPLE      (MARK at 212)
254: R        REDUCE
255: (        MARK
256: V            UNICODE    'A'
259: t            TUPLE      (MARK at 255)
260: R        REDUCE
261: t        TUPLE      (MARK at 208)
262: R    REDUCE
```

其中還有 memory 的機制，可以把字元存下來當變數使用，以下這段就是把 flag[9] 放到 3 這個變數中
```
327: g    GET        1
330: (    MARK
331: g        GET        0
334: S        STRING     '__getitem__'
349: t        TUPLE      (MARK at 330)
350: R    REDUCE
351: (    MARK
352: I        INT        9
355: t        TUPLE      (MARK at 351)
356: R    REDUCE
357: p    PUT        3
```

要取出來就用 GET，以下這段就是讓 flag[14] = 3 這個變數，跟上一段加起來就是 flag[14] = flag[9]
```
423: g    GET        2
426: (    MARK
427: g        GET        1
430: (        MARK
431: g            GET        1
434: (            MARK
435: g                GET        0
438: S                STRING     '__getitem__'
453: t                TUPLE      (MARK at 434)
454: R            REDUCE
455: (            MARK
456: I                INT        14
460: t                TUPLE      (MARK at 455)
461: R            REDUCE
462: S            STRING     '__eq__'
472: t            TUPLE      (MARK at 430)
473: R        REDUCE
474: (        MARK
475: g            GET        3
478: t            TUPLE      (MARK at 474)
479: R        REDUCE
480: t        TUPLE      (MARK at 426)
481: R    REDUCE
```

如此這般看完就可以拿到 flag 了
* flag: `AIS3{dAmwjzphIj}`
