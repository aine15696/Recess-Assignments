
def checker(rating):
    if(rating<1):
        print("Invalid answer")
        return 0
    elif(rating<3):
        print("Hold your head up, you are not alone in this. Call 0700000000 talk to somebody.")
        return 1
    elif(rating<5):
        print("Today might seem tough, but keep pushing. If you need support, call 0700000000")
        return 1
    elif(rating == 5):
        print("Focus on the positives, that's how we go up.")
    elif(rating<10):
        print("Savour the good times. They hold us up. Let's celebrate with you, call 0700000000")
        return 1
    else:
        print("Invalid choice")
        return 0
    
loop = 0
while(loop == 0):
    loop = checker(int(input("This is a simple mental health survey. How would you rate your health on a scale of 1-10: ")))

print("\nThank you for participating in this survey")