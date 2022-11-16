import time
while True:
    print ("You found yourself in an abandoned hut.")
    time.sleep(2)
    print ("It is a stormy night.")
    time.sleep(2)
    print ("You can see the wooden door in front of you.")
    time.sleep(2)
    q = input("You open that door?    1- Yes   2- No")
    if q == "1":
        time.sleep(2)
        print ("You open the door")
        time.sleep(2)
        print ("You encounter with a bear")
        time.sleep(2)
        q101 = input("What do you do now?    1- Back to hut   2- Fight")
        if q101 == "2":
            time.sleep(2)
            print ("you died")
            time.sleep(2)
        if q101 == "1":
            time.sleep(2)
            print ("You are running back to the hut")
            time.sleep(2)
            print ("The bear is following you!")
            time.sleep(2)
            print ("But you have done it. You could enter.")
            time.sleep(2)
    if q == "2":
        time.sleep(2)
        print ("Just after your decision, the door opens and a bear kills you")
        time.sleep(2)
        print ("But it was a dream. You woke in someone's bed")

