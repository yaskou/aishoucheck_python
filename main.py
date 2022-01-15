original=input("2人の名前をひらがなで入力:")
original=original.replace(" ","")
original=original.replace("　","")
change_count=0
def change_number(change_number):
    global original
    global change_count
    original=original.replace(original[change_count],change_number,1)
    change_count=change_count+1
while change_count<len(original):
    if original[change_count] in "あかさたなはまやらわがざだばぱゃ":
        change_number(str(1))
    elif original[change_count] in "いきしちにひみりぎじぢびぴ":
        change_number(str(2))
    elif original[change_count] in "うくすつぬふむゆるをぐずづっぶぷゅ":
        change_number(str(3))
    elif original[change_count] in "えけせてねへめれげぜでべぺ":
        change_number(str(4))
    elif original[change_count] in "おこそとのほもよろんごぞどぼぽょ":
        change_number(str(5))
    else: change_number(str(0))
original=original.replace("0","")    

def factorial(n):
    count_=1
    answer=1
    while count_<=n:
        answer=answer*count_
        count_=count_+1
    return answer    

def nCr(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))
     
change_count=0
pascal_number_1=0
pascal_number_2=0
while change_count<=len(original)-2:
    nCr_=nCr(len(original)-2,change_count)
    pascal_number_1=pascal_number_1+nCr_*int(original[change_count])
    pascal_number_2=pascal_number_2+nCr_*int(original[change_count+1])
    change_count=change_count+1
pascal_number_1=str(pascal_number_1)
pascal_number_2=str(pascal_number_2)    
if pascal_number_1[len(pascal_number_1)-1]=="0" and pascal_number_2[len(pascal_number_2)-1]=="0":
    input("0%か100%かはあなた自身で決めてください\n何かのキーを押すと終了します")
else: input(pascal_number_1[len(pascal_number_1)-1]+pascal_number_2[len(pascal_number_2)-1]+"%です\n何かのキーを押すと終了します")    