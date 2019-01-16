import json as json

with open('dic.json') as dic_file:
    dic = json.load(dic_file)

    age = []
    sum = 0.0
    count = 0

    for x in dic:
        calculated = 2019-int(dic[x][-4:])+1
        age.append(calculated)
        sum += calculated
        count += 1

    age.sort()
    print('mean: ' + str(sum / count))
    if count%2==0:
        print('median: '+str((age[count//2-1]+age[(count+2)//2-1])/2.0))
    else:
        print('median: '+str(age[count+1]//2))





