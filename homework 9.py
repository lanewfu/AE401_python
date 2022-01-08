a = {}
while True:
    flg = int(input('繼續輸入1離開輸入0列出請輸入2查詢單字輸入3測驗請按4'))
    if flg==0:
        break
    elif flg==1:
        eng = input('請輸入英文單字')
        ch = input('請輸入中文解釋')
        a[eng] = ch
        print(a)
    elif flg==2:
        print(a)
    elif flg==3:
        eng = input('請輸入英文單字')
        if eng in a:
            a[eng]
            print(a[eng])
        else:
            print('沒有這個東西')
    elif flg==4:
        print('題目共有',len(a),'題，一題一分')
        sum = 0;
        for k,v in a.items():
            print('題目為',k)
            ans = input('輸入你的答案')
            if v ==ans:
                print('答對了+1分')
                sum+=1
            else:
                print('答錯了，不扣分')
        print('你獲得分數為',sum,'總分為',len(a),'分')