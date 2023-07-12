# KBC (Upgraded version) :
print("\n*****| Welcome to the new KBC game |*****")
name = input("\nEnter your name to start the game : ")
print()

# Variable initialization :
Q1 = ["1] Which is the largest planet of our solar system ?","Mercury","Jupiter","Earth","Neptune","b","Jupiter"]
Q2 = ["2] Where is Statue of Liberty present ?","UK","Hawaii","Britain","New York","d","New York"]
Q3 = ["3] Which among these is the  odd one out :","One","Two","Four","Six","c","Four"]
Q4 = ["4] Who Built The Taj mahal ?","Akbar","Aurangzeb","Shah Jahan","Babur","c","Shah Jahan"]
Q5 = ["5] Where is Nile river situated ?","Africa","Australia","China","India","a","Africa"]
Q6 = ["6] What game studio makes the Red Dead Redemption series? ","Gameloft","Unisoft","Rockstar","SuperCell","c","Rockstar"]
Q7 = ["7] Which planet in the Milky Way is the hottest? ","Venus","Mercury","Mars","Pluto","a","Venus"]
Q8 = ["8] How many dots appear on a dice?","6","20","19","21","d","21"]
Q9 = ["9] What sports car company manufactures the 911?","Bugati","Ferrari","Lamborgini","Porche","d","Porche"]
Q10 = ["10] What is the result of (100+0*10)","1000","100","0","None of the above","b","100"]
Q11 = ["11] In what country was Elon Musk born?","Sweden","Scottland","South Africa","New York","c","South Africa"]
Q12 = ["12] How many hearts does an octopus have?","3","8","1","2","a","3"]
Q13 = ["13] What is the name of Google's A.I.?","ChatGPT","Siri","GoogleAI","Bard","d","Bard"]
Q14 = ["14] which among these is the odd one out :","Python","Data science","English","Binary","b","Data Science"]
Q15 = ["15] What software company is headquartered in Redmond, Washington?","MicroSoft","Facebook","Google","YouTube","a","Micro Soft"]
game = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15]
level = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money,prize = 0,0

# Program Logic :
for ques in range(len(game)):
    print("_________________________________________________________________________________________")
    print(f"\nYour question for Rs.{level[ques]} is on your computer screen :\n")
    print(game[ques][0])
    print("A:",game[ques][1],"  B:",game[ques][2])
    print("C:",game[ques][3],"  D:",game[ques][4])
    ans = input("Enter your answer : ")
    if ans.lower()==game[ques][5] or ans.capitalize()==game[ques][6]:
        print(f"\nSHI JAWAB! \nYe gye Rs.{level[ques]} apke Bank Account me ")
        prize=level[ques]
        if ques==4 or ques==9 or ques==14:
            money=level[ques]
    elif ans.capitalize()=="Quit" or ans.lower()=="q":
        money=prize
        break
    else:
        print("\nGALAT JAWAB !")
        break
prize=money
# Final Conclusion :
if prize==10000000:
    print(f"\nCongrats {name} ! Aap bangye h CRORE-PATI !!!\nKya kijega itni dhanrashi ka !")
elif prize==0:
    print(f"\nYou won {prize}\nItne pese kaha leke jayenge {name} ji !")
else :
    print(f"\n{name},you won Rs.{prize} !\nBetter luck next time.")

# Stats file :
newChoice = input("\nDo you wanna know the previous stats? ")
print()
if newChoice.lower() == "yes":
    try:
        stats = open("KBCstats.txt","r")
        stats.close()
    except FileNotFoundError:
        stats = open("KBCstats.txt","w")
        stats.close()
        print("No Previous Data Found !")
        
    stats = open("KBCstats.txt","r")
    data = stats.read()
    print(data)
    stats.close()
stats = open("KBCstats.txt","a")
stats.write(f"\n{name} won Rs.{prize}")
stats.close()

print("\n\nGame finished......")