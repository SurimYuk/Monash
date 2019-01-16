import json as json
import matplotlib.pyplot as plt

with open('dic.json') as dic_file:
    dic = json.load(dic_file)

    month = ['','January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for x in dic:
        for y in range(1,13):
            if y<10:
                if dic[x].find('/0'+str(y)+'/')>0:
                    count[y]+=1
            else:
                if dic[x].find('/' + str(y) + '/') > 0:
                    count[y] += 1

month = month[1:14]
count = count[1:14]

plt.figure(figsize=(13,5))
plt.bar(month, count)
plt.xlabel("month")
plt.ylabel("count")
plt.title("how many friends are in each month")
plt.show()


