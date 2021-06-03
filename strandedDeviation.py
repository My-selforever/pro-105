import csv
import math

f = open('data.csv')

rf = csv.reader(f)

fileList = list(rf)
print(fileList)

l = len(fileList[0])

add = 0


for i in range(l):
    data = int(fileList[0][i])
    add +=data

mean = add/l

s = 0

for i in range(l):
    data = (int(fileList[0][i])-mean)**2
    s+=data

val=s/(l-1)

Deviation = math.sqrt(val)

print(Deviation)

print(mean,"mean")



