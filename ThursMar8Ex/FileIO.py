#Exercise 1. 
file_name1 = input("What file should I read? ")
file_handle1 = open(file_name1, 'r')
contents1 = file_handle1.read()
file_handle1.close()
print(contents1)

#Exercise 2.
file_name2 = input("What file do you want to write? ")
file_handle2 = open(file_name2, 'w')
contents2 = input("What should it say? ")
file_handle2.write(contents2)
file_handle2 = open(file_name2, 'r')
newcontents2 = file_handle2.read()
file_handle2.close()
print(newcontents2)

#Exercise 3.
file_name3 = input("What file should I study? ")
file_handle3 = open(file_name3, 'r')
contents3 = file_handle3.read()
file_handle3.close()
counter = {}
def letter_histogram(word):
    for letter in word:
        occurences = counter.get(letter, 0)
        counter[letter] = occurences + 1
    print(counter)
letter_histogram(contents3)

def word_histogram(paragraph):
    words = ""
    word_list = []
    word_count = {}
    for i in range(len(paragraph)):
        if paragraph[i] == " ":
            word_list.append(words)
            words = ""

        elif i == len(paragraph)-1:
            words = words + paragraph[i]
            word_list.append(words)

        else:
            words = words + paragraph[i]

    for j in range(len(word_list)):
        word_count[word_list[j]] = word_count.get(word_list[j],0)
        word_count[word_list[j]] = word_count[word_list[j]] + 1
    print(word_count)
word_histogram(contents3)

#Exercise 4.
import json
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import matplotlib.pyplot as plot

with open('Input.json', 'r') as fh:
  data = json.load(fh)
  
i = 0
j = 0
for i in data:
    xs = data[i]
for j in data:
    ys = data[j]
print(xs, ys)
plot.plot(xs, ys)
pyplot.savefig('IOEx4.png')
pyplot.close()

# #Bonus Crash test. I'm commenting this out because you should be careful with this!! It is MEANT to crash.
# #1. Mine kept running for 10+ minutes without breaking, but I could see the uptick in memory used.
# #2. No errors...apparently my computer is able to handle to overload of the memory.
# #3. I expected it to crash, period! I guess I should be more cruel to my computer...
# import io
# file_handleB = io.StringIO()
# while True:
#     file_handleB.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
#     contents = file_handleB.getvalue()
#     print(len(contents))
