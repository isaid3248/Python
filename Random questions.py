import random
import time
Points = 0
while True:
    q = ['3+7','2+5','3+1','1+7','5+1','2+3','1+1','54+56']
    a = ['10','7','4','8','6','5','2','110']
    sorunum = random.randint (0,7)
    soru = q[sorunum]
    print (soru)
    print ("Sorunun cevabı nedir?")
    answer1 = input("Cevap: ")
    if answer1 == a[sorunum]: 
        print ("Doğru cevap, tebrikler! 50 puan kazandınız. Artık diğer soruya geçebiliriz.")
        time.sleep (0.6)
        Points = Points + 50
    else:
        print ("Yanlış cevap, 20 puan bakiyenden gitti, hadi diğer soruya geçelim.")
        Points = Points - 20
        time.sleep (0.6)
    print ("puanınız: ", Points)