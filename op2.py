class Cricket:
    def __init__(self,player,score):
       self.__player = player
       self.__score = score

    def info(self):
        print(f"Cricket - Player:{self.__player}, Score:{self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")  

        else:
            print("Score cannot be negative.")      

class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    
    def info(self):
        print(f"Football - Player:{self.__player}, Score:{self.__score}")
    
    def play(self):
        print(f"{self.__player} hits a goal!!")
    
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")  
    
        else:
            print("Score cannot be negative.")  

cricket = Cricket("Virat", 100)          
football = Football("Ronaldo", 5)

print("--- Scoreboard ---")
for sport in (cricket,football):
    sport.info()
    sport.play()
    print()

print("--- Change Attempted ---")
cricket.__score = 567
print(f"get_score() still shows: {cricket.get_score()}") 

print("--- Updated Score ---")
cricket.set_score(200)
football.set_score(7)
