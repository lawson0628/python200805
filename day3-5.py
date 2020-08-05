while True:
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
   
    sel=int(input('請輸入你要選的選項：'))
    if sel==1:
        a=int(input('請輸入一個數'))
        b=int(input('請輸入一個數'))
        print(a,'+',b,'=',a+b)
    
    elif sel==2:
        a=int(input('請輸入一個數'))
        b=int(input('請輸入一個數'))
        print(a,'-',b,'=',a-b)
        
    elif sel==3:
        a=int(input('請輸入一個數'))
        b=int(input('請輸入一個數'))
        print(a,'x',b,'=',a*b)
        
    elif sel==4:
        a=int(input('請輸入一個數'))
        b=int(input('請輸入一個數'))
        print(a,'÷',b,'=',a/b)
    else:
        break
        
        
         

