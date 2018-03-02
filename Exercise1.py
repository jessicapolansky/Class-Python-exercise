#Exercise 1. Enter your name and receive a salutation.
nombre = input("What should I call you? ")
print("Hello " + nombre + ".")

#Exercise 2. Energetic and informative salutation.
nOMBRE = input("TELL ME YOUR NAME AGAIN! ")
print("HELLO  {}! YOUR NAME HAS {} LETTER(S)!".format(nOMBRE.upper(), len(nOMBRE)))

#Exercise 3. Make a madlib that turns into a horrible limerick
print("Let's do a madlib!")
destination = input("Give me a location: ")
adjective = input("Give me an adjective: ")
bodyPart = input("Give me a body part: ")
job = input("Give me an occupation: ")

print("Okay here we go:")
print("There once was a dude from {0},\nWho always wore {1} clothing,\nBut one day he fell,\nAnd lost his {2},\nNow he's a {3} for life!\n".format(destination, adjective, bodyPart, job))

print("...That was terrible.")

#Exercise 4. Input number to get corresponding day of the week.
day = int(input('Day (0-6)? '))
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("That would be {}".format(daysOfWeek[day]))

#Exercise 5. Input number to determine if the corresponding day is for work or sleep.
day = int(input('Day (0-6)? '))
daysOfWeek = ["Sleep in.", "Go to work.", "Go to work.", "Go to work.", "Go to work.", "Go to work.", "Sleep in."]
print(daysOfWeek[day])

#Exercise 6. Convert C to F degrees.
temp = round(int(input("Current temp in C? ")), 2)
print("That equals {} degrees F.".format((temp * 1.8 + 32)))

#Exercise 7. Calculate tip based on billing amount and service rating.
totalAmt = float(input("How much did you spend? "))
rating = input("Quality of service: Good, fair, or bad? ").lower()
feedback = False
while (feedback == False):
    if rating == "good":
        print("Tip amount is ${0:.2f}.".format(round(totalAmt * 0.20, 2)))
        feedback = True
    elif rating == "fair":
        print("Tip amount is ${0:.2f}.".format(round(totalAmt * 0.15, 2)))
        feedback = True
    elif rating == "bad":
        print("Tip amount is ${0:.2f}.".format(round(totalAmt * 0.10, 2)))
        feedback = True
    else:
        rating = input("Invalid rating. Please enter 'good,' 'fair,' or 'bad.' >> ").lower()
        
#Exercise 8. Calculate the bill portion for multiple people.
totalAmt = float(input("How much did you spend? "))
rating = input("Quality of service: Good, fair, or bad? ").lower()
splitTip = int(input("Split how many ways? "))
feedback = False
while (feedback == False):
    if rating == "good":
        print("Tip amount is ${0:.2f}.".format(round(((totalAmt * 0.20) / splitTip), 2)))
        feedback = True
    elif rating == "fair":
        print("Tip amount is ${0:.2f}.".format(round(((totalAmt * 0.15) / splitTip), 2)))
        feedback = True
    elif rating == "bad":
        print("Tip amount is ${0:.2f}.".format(round(((totalAmt * 0.10) / splitTip), 2)))
        feedback = True
    else:
        rating = input("Invalid rating. Please enter 'good,' 'fair,' or 'bad.' >> ").lower()
        
#Exercise 9. Use a loop to print numbers 1 - 10.
i = 1
while i <= 10:
    print(i)
    i += 1

#Exercise 10. Give out 'coins' and keep a tally.
print("You have 0 coins. Would you like one?")
coins = 0
greed = input("Y/N >> ").upper()
while greed == "Y" or greed == "YES":
    coins += 1
    print("You now have {} coins. Would you like another?".format(coins))
    greed = input("Y/N >> ").upper()
print("Okay, I guess {} coins is good enough.".format(coins))
    