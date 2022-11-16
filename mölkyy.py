
def jeu():
    
    final_score=0
    def new_score(score):
        final_score=0
        while final_score!=50:
            score=int(input("enter your score  "))
            if score<0 or score>12:
                print("please enter a valid number")
                final_score=final_score-score  
            final_score=final_score+score
            if final_score==50:
                print("you won")
                exit()              
            if final_score>50:
                final_score=25
            print("your score: ", final_score)

    while final_score!=50:    
        
        new_score(0)
jeu()