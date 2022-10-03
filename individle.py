file1=open("D:\Exercises.txt","w")
file2=open("D:\Answers.txt","w")

import random as r
number=int(input("您需要出几道题呢？"))
if number<=0:
    print("题目数量必须大于0哦！")
else:
    sign="+-"
    i=0
    while i<number:
        sign_number=r.randint(1,2)
        if sign_number==1:
            if sign[r.randint(0,1)]=="+":
                number1=r.randint(1,100)
                number2=r.randint(1,100)
                sum1=number1+number2
                if sum1<100 and number1!=number2:
                    i+=1
                    number1=str(number1)
                    number2=str(number2)
                    sum1=str(sum1)
                    i=str(i)
                    file1.writelines(["第",i,"题题目:\n",number1,"+",number2,"=","\n"])
                    file2.writelines(["第",i,"题答案:\n",sum1,"\n"])
                    i=int(i)
                else:
                    continue
            elif sign[r.randint(0,1)]=="-":
                high_number=r.randint(1,100)
                low_number=r.randint(1,100)
                if high_number<low_number:
                    high_number,low_number=low_number,high_number
                if high_number!=low_number:
                    i+=1
                    sum2=high_number-low_number
                    high_number=str(high_number)
                    low_number=str(low_number)
                    sum2=str(sum2)
                    i=str(i)
                    file1.writelines(["第",i,"题题目:\n",high_number,"-",low_number,"=\n"])
                    file2.writelines(["第",i,"题答案:\n",sum2,"\n"])
                    i=int(i)
        if sign_number==2:
            number_1=r.randint(1,100)
            number_2=r.randint(1,100)
            number_3=r.randint(1,100)
            sign1=sign[r.randint(0,1)]
            sign2=sign[r.randint(0,1)]
            if number_1<number_2:
                number_1,number_2=number_2,number_1
            if sign1=="+" and number_1+number_2<100:
                if sign2=="+" and number_1+number_2+number_3<100:
                    i+=1
                    sum3=number_1+number_2+number_3
                    number_1=str(number_1)
                    number_2=str(number_2)
                    number_3=str(number_3)
                    sum3=str(sum3)
                    i=str(i)
                    file1.writelines(["第",i,"题题目:\n",number_1,"+",number_2,"+",number_3,"=\n"])
                    file2.writelines(["第",i,"题答案:\n",sum3,"\n"])
                    i=int(i)
                elif sign2=="-" and number_1+number_2-number_3<100 and number_1+number_2-number_3>0:
                    i+=1
                    sum4=number_1+number_2-number_3
                    number_1=str(number_1)
                    number_2=str(number_2)
                    number_3=str(number_3)
                    sum4=str(sum4)
                    i=str(i)
                    file1.writelines(["第",i,"题题目:\n",number_1,"+",number_2,"-",number_3,"=\n"])
                    file2.writelines(["第",i,"题答案:\n",sum4,"\n"])
                    i=int(i)
                else:
                    continue
            elif sign1=="-" and number_1!=number_2:
                if sign2=="+" and number_1-number_2+number_3<100:
                    i+=1
                    sum5=number_1-number_2+number_3
                    number_1=str(number_1)
                    number_2=str(number_2)
                    number_3=str(number_3)
                    sum5=str(sum5)
                    i=str(i)
                    file1.writelines(["第",i,"题题目:\n",number_1,"-",number_2,"+",number_3,"=\n"])
                    file2.writelines(["第",i,"题答案:\n",sum5,"\n"])
                    i=int(i)
                elif sign2=="-" and number_1-number_2-number_3<100 and number_1-number_2-number_3>0:
                    i+=1
                    sum6=number_1-number_2-number_3
                    number_1=str(number_1)
                    number_2=str(number_2)
                    number_3=str(number_3)
                    sum6=str(sum6)
                    i=str(i)
                    file1.writelines(["第",i,"题题目:\n",number_1,"-",number_2,"-",number_3,"=\n"])
                    file2.writelines(["第",i,"题答案:\n",sum6,"\n"])
                    i=int(i)
                else:
                    continue
            else:
                continue
            
file1.close()
file2.close()
                
                    
                    
                
            
            
                    
    
    
