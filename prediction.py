import numpy as np
file1 = open("loc_loc_res.txt")
file2 = open("loc_range_res.txt")
file3 = open("loc_time_res.txt")
file4 = open("loc_type_res.txt")
relation1=[]
relation2=[]
relation3=[]
relation4=[]
for line in file1:
    line = line.strip()
    line = line.split(' ')
    relation1.append(line)
num = len(relation1)
relation1 = relation1[1:num]
for line in file2:
    line = line.strip()
    line = line.split(' ')
    relation2.append(line)
num = len(relation2)
relation2 = relation2[1:num]
for line in file3:
    line = line.strip()
    line = line.split(' ')
    relation3.append(line)
num = len(relation3)
relation3 = relation3[1:num]
for line in file4:
    line = line.strip()
    line = line.split(' ')
    relation4.append(line)
num = len(relation4)
relation4 = relation4[1:num]
correct_num=0
totalnum=600
k=15
for i in range(600):
    for j in range(len(total_loc)):
        position=len(finaltest[i])-1
        preference[i].dot(dict_all['l'+str(j)])+dict_time[finaltest[i][position][3]].dot()
        
        
        
correct_num=0
totalnum=600
k=15
topk=[]
testscore={}
for i in range(600):
    position=len(finaltest[i])-1
    for j in range(len(total_loc)):
        location=dict_all['l'+str(j)]
        typenum=len(finaltest[i][position][5])
        score = preference[i].dot(location)+dict_time[finaltest[i][position][3]].dot(location)+dict_range[finaltest[i][position][4][2]].dot(location)
        for k in range(typenum):
            if finaltest[i][position][5][k] in dict_type.keys():
                score =score+dict_type[finaltest[i][position][5][k]].dot(location)
        testscore['l'+str(j)]=score
    listing = zip(testscore.values(),testscore.keys())
    listing = sorted(listing)
    for l in range(k):
        topk.append(listing[k][1])
    if finaltest[i][position][2] in topk:
        correct_num = correct_num+1
print(correct_num/totalnum)           
correct_num=0
totalnum=600
k=15
topk=[]
testscore={}
for i in range(600):
    position=len(finaltest[i])-1
    for j in range(len(total_loc)):
        location=dict_all['l'+str(j)]
        typenum=len(finaltest[i][position][5])
        score = preference[i].dot(location)+dict_time[finaltest[i][position][3]].dot(location)+dict_range[finaltest[i][position][4][2]].dot(location)
        for k in range(typenum):
            if finaltest[i][position][5][k] in dict_type.keys():
                score =score+dict_type[finaltest[i][position][5][k]].dot(location)
        testscore['l'+str(j)]=score
    listing = zip(testscore.values(),testscore.keys())
    listing = sorted(listing)
    for l in range(k):
        topk.append(listing[k][1])
    if finaltest[i][position][2] in topk:
        correct_num = correct_num+1
print(correct_num/totalnum)  


a=final_res[0][0]
b=0
test=[]
for i in range(4163):
    test.append([])
for i in range(len(final_res)):
    if final_res[i][0]==a:
        test[b].append(final_res[i])
    else:
        a=final_res[i][0]
        b=b+1
        test[b].append(final_res[i])
        
        
finaltest=[]
for i in range(len(test)):
    if len(test[i])>5:
        finaltest.append(test[i])
preference=[]
for i in range(len(finaltest)):
    preference.append(np.ones(100)*0)
for i in range(len(finaltest)):
    placenum = len(finaltest[i])
    for j in range(placenum):
        preference[i]=preference[i]+np.exp(finaltest[i][placenum-1][1]-finaltest[i][j][1])*dict_all[finaltest[i][j][2]]