import math 
import csv

with open('PRO-105_2.csv')as f :
    reader = csv.reader(f)
    lists = list(reader)

length = len(lists)

def mean(lists) : 
    total = []
    for i in range(len(lists)) :
        num = lists[i][i] 
        total.append(float(num))
    
    half_mean = sum(total)

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
