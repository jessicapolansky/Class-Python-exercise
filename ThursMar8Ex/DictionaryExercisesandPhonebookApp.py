#1st Dictionary Exercise. I went ahead and modified it to do the Phonebook App exercise too.
import pickle

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
} 

def retrieveNum():
    nameNum = input("Whose number? (Enter Name) ")
    print("Found entry for {}: {}".format(nameNum, phonebook_dict[nameNum]))

def addNum():
    newName = input("Name? ")
    newPhone = input("Phone number? ")
    newEntry = {newName: newPhone}
    phonebook_dict.update(newEntry)
    print("Entry stored for {}".format(newEntry))
    
def delNum():
    killPhone = input("Who should I delete? ")
    del phonebook_dict[killPhone]
    print("Deleted entry for {}.".format(killPhone))
    
def changNum():
    oldNum = input("Whose number should I change? (Enter Name) ")
    newNum = input("What's the new phone number? ")
    phonebook_dict[oldNum] = newNum
    print("All set! {}: {}".format(oldNum, phonebook_dict[oldNum]))
    
def showAll():
    print(phonebook_dict)

selectDict = input("""Please make a selection from 1 - 5:
1. Print a phone number/Look up an entry.
2. Set an entry.
3. Delete an entry.
4. Change a phone number.
5. Display all phone entries.
6. Save entries.
7. Load saved entries.
8. Quit\n""")
selection = True
while selection:
    if selectDict == '1':
        retrieveNum()
        selectDict = input("Make another selection. ")
    elif selectDict == '2':
        addNum()
        selectDict = input("Make another selection. ")
    elif selectDict == '3':
        delNum()
        selectDict = input("Make another selection. ")
    elif selectDict == '4':
        changNum()
        selectDict = input("Make another selection. ")
    elif selectDict == '5':
        showAll()
        selectDict = input("Make another selection. ")
    elif selectDict == '6':
        myfile = open('phonebook_dict.pickle', 'wb')
        pickle.dump(phonebook_dict, myfile)
        myfile.close()
        selectDict = input("Make another selection. ")
    elif selectDict == '7':
        myfile = open('phonebook_dict.pickle', 'rb')
        phonebook_dict = pickle.load(myfile)
        print(phonebook_dict)
        selectDict = input("Make another selection. ")
    elif selectDict == '8':
        print("Closing the phonebook.")
        selection = False
    else:
        print("Invalid selection. Closing the phonebook.")
        selection = False

# #2nd Dictionary Exercise
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])
