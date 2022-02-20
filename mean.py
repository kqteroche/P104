import csv
with open('hw.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range (len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total = 0
for e in new_data:
    total += e

mean=total/n
print ("the mean is: " + str(mean))