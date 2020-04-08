from collections import Counter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

file = open("example.txt", encoding="utf8")
file = file.readlines()
file = str(file)

txt = file

numbers = []
performance = []

x = 0
while x != len(txt):
    try:
        numbers.append(int(txt[x]))
        x +=1
    except:
        x += 1
        
numbers.sort()
print(len(numbers))
a = dict(Counter(numbers))

print (a) 
m = 0
while m != 10:
    performance.append(numbers.count(m))
    m += 1

nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
y_pos = nums
print(performance)

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, nums)
plt.ylabel('Usage')
plt.title('Numbers Used')

plt.show()
    

