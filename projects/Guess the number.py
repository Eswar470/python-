import random
def process(level,ans):
    while level>=1:
        print(f"you have {level} attempts remaining to guess the number! ")
        guess=int(input("Make a guess:"))
        if guess>ans:
            print("your Guess is too high")
        elif guess<ans:
            print("Your Guess is too low")
        else:
            print("Your Guess is right...YOU WON")
            break
        level-=1
    else:
        print(f"You are out of atempts...YOU LOSE\nThe NO is {ans}")
print("Let me think of a number between 1 to 50.")
ans=random.randint(1,50)
print(ans)
level=input("choose the level of difficulty... Type 'easy' or 'hard':").lower()
if level=='easy':
    process(10,ans)
else:
    process(5,ans)
    

