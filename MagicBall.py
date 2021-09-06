import random
ans1 = "It is certain."
ans2 = "It is decidely So!"
ans3 = "Without a doubt."
ans4 = "Yes! defintely."
ans5 = "You may rely on it."
ans6 = "As I see it YES!"
ans7 = "Most likely :) "
ans8 = "Outlook Good"
ans9 = "YES!!"
ans10 = "Signs point to a yes!"
ans11 = "Reply hazy, Try asking again :( "
ans12 = "Ask again later!"
ans13 = "Better not tell you now. \n ps: result can be both positive and negative! "
ans14 = "Cannot predict now! Keep your fingers crossed. "
ans15 = "Concentrate and ask again."
ans16 = "Don't count on it."
ans17 = "My reply is NO."
ans18 = "My sources say NO."
ans19 = "Outlook not so good!"
ans20 = "Doubtful!\n But remember anything can change!"

def play():
    name=input("Hello! Welcome to the magic Ball. What is your good name?")
    input(name+", What is your question to the magic ball? ")
    choice=random.randint(1,20)

    if choice==1:
        answer=ans1
    elif choice==2:
        answer=ans2
    elif choice==3:
        answer=ans3
    elif choice==4:
        answer=ans4
    elif choice==5:
        answer=ans5
    elif choice==6:
        answer=ans6
    elif choice==7:
        answer=ans7
    elif choice==8:
        answer=ans8
    elif choice==9:
        answer=ans9
    elif choice==10:
        answer=ans10
    elif choice==11:
        answer=ans11
    elif choice==12:
        answer=ans12
    elif choice==13:
        answer=ans13
    elif choice==14:
        answer=ans14
    elif choice==15:
        answer=ans15
    elif choice==16:
        answer=ans16
    elif choice==17:
        answer=ans17
    elif choice==18:
        answer=ans18
    elif choice==19:
        answer=ans19
    else:
        answer=ans20

    print("Magic 8 ball: "+answer+"\nAlso, remember no matter what the luck says, HARDWORK and DETERMINATION can always change your future.")

play()
while input("Do you want to ask another question? 'yes' or 'no' ").lower()=='yes':
    play()



