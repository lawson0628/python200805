dic={}

print('歡迎進入系統')
while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')
    sel=int(input('請輸入你要選的選項：'))
    
    if sel==6:
        print('下次見 要多背單字喔')
        break
    
    elif sel<1 or sel>6:
        print('輸入錯誤')
        
    if sel==1:
        while True:
            a=input('請輸入單字')
            if a=='0':
                break
            b=input('請輸入單字解釋或中文')
            dic[a]=b
            
    elif sel==2:
        print(dic)
   
    elif sel==3:
        c=input('請輸入要翻成中文的字 (按０離開)')
        if c==0:
            break
        elif c in dic:
            print('這個字的意思是',dic[c])
        else:
            print('查無此字')
        
    elif sel==4:
        d=input('請輸入要翻成英文的字 (按０離開)')
        for k,v in dic.items():
            if d==0:
                break
            elif v==d:
                print('這個字是',k)
                break
        else:
            print('查無此字')
            
    elif sel==5:
        for k,v in dic.items():
            print(v)
            e=input('請作答')
            if k==e:
                print('答對了')
            elif e==0:
                break
            else:
                print('答錯了 該死 居然不好好背單字')
            
            