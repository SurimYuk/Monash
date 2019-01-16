import json as json

with open('dic.json') as dic_file:
    dic = json.load(dic_file)

    #for x in dic:
    #    print("%s: %s" % (x, dic[x]))

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

for x in range(1,13):
    if count[x]>1:
        print(month[x]+' has '+str(count[x])+' friends.')
    else:
        print(month[x] + ' has ' + str(count[x]) + ' friend.')

