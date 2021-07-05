print ("Welcome to your test")
name = input("Name:  ")
while True:
    
    print ("Soru 1: Fransa'nın nüfusu kaçtır?")
    print ("A: 66,99 milyon")
    print ("B: 74,88 milyon")
    print ("C: 81,77 milyon")
    print ("D: 54,55 milyon")
    cevap = input("Cevabınız:  ")

    if cevap == ("A" and "a"):
        print ("Doğru cevap tebrikler ! " + name)
        break
    
    elif cevap == ("B" and "b"): 
        print ("Yanlış cevap " + name)

    elif cevap == ("C" and "c"):
        print ("YANLIŞ CEVAP " + name)
    
    elif cevap == ("D" and "d"):
        print ("yanlış " + name)

    else:
        print("lütfen geçerli bir cevap giriniz " + name)
