#Deliverable one
#Connor Critchley
# 7/24/24

#initial input
name = input("Welcome to GC minigolf! What's your name? ")
holes = int(input(f"Hi, {name}! Would you like to play 3 or 6 holes? "))
if holes != 3 and holes != 6:
    print("Sorry, that's not valid, so have 6 holes.")
    holes = 6
par = holes * 3 #initialize par to compare against
putts = 0 #initialize score

#start getting puts/score
for i in range(holes):
    putts += int(input(f"How many puts for hole {i+1}? (par:3) "))

#print end conditions
if putts < par:
    print(f"Great job, {name}! Your total score was: {putts - par}.")
elif putts == par:
    print(f"Good game, {name}. Your total score was: {putts - par}.")
else:
    print(f"Nice try, {name}... Your total score was: +{putts - par}.")