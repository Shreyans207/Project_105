import math 
import csv

with open('PRO-105_2.csv')as f :
    reader = csv.reader(f)
    lists = list(reader)

length = len(lists)
total2 = []

def mean(lists) : 

    for i in lists[0] :
        num = i 
        total2.append(num)

    half_mean = sum(total2)
    
    mean = half_mean/length
    return mean

sigma_1 = [] 

for i in lists : 
    number = int(i[1])
    diff = number - mean(lists)
    squared = diff*diff
    sigma_1.append(squared)

summation = sum(sigma_1)
result = summation/length

st_deviation = math.sqrt(result)
print(mean(lists))
