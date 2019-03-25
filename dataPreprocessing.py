file = open("checkin.txt")
result=[]
#星期属性转换
def week(x):
    if x=="Mon":
        res = '1'
    elif x=="Tue":
        res = '2'
    elif x=="Wed":
        res = '3'
    elif x=="Thu":
        res = '4'
    elif x=="Fri":
        res = '5'
    elif x=="Sat":
        res = '6'
    else:
        res = '7'
    return res
def month(x):
    if x=="Jan":
        res = '01'
    elif x=="Feb":
        res = '02'
    elif x=="Mar":
        res = '03'
    elif x=="Apr":
        res = '04'
    elif x=="May":
        res = '05'
    elif x=="Jun":
        res = '06'
    elif x=="Jul":
        res = '07'
    elif x=="Aug":
        res = '08'
    elif x=="Sep":
        res = '09'
    elif x=="Oct":
        res = '10'
    elif x=="Nov":
        res = '11'
    elif x=="Dec":
        res = '12'
    return res
#改时间进制
def time(x):
    tmp = int(x.split(':')[0])+int(x.split(':')[1])/60
    tmp = str(tmp)
    return tmp
#一天分四个时间段
def quater(x):
    if x>='00:00:00' and x<='06:00:00':
        res = '0'
    elif x>'06:00:00' and x<='12:00:00':
        res = '1'
    elif x>'12:00:00' and x<='18:00:00':
        res = '2'
    else:
        res = '3'
    return res
#保留经纬度，地区，州
def location(x):
    x=x.strip('{')
    x=x.strip('}')
    x=x.split(',')
    x=[x[0],x[1],x[2],x[3]]
    return x
#去掉餐馆类别中最后一个空格
def venuetype(x):
    x=x.strip()
    x=x.strip('{')
    x=x.strip('}')
    x=x.split(',')
    l=len(x)
    res=[]
    for i in range(l-1):
        res.append(x[i])
    return res
for line in file:
    result.append(line)
num = len(result)-1
list_num = 6
matrix = [[0]*list_num for i  in range(num)]
#生成序列矩阵
for i in range(num):
    for j in range(list_num):
        matrix[i][j] = result[i+1].split('\t')[j]
final_res=[]
for i in range(num):
    tmp = matrix[i][1].split(' ')
    matrix[i][1]=float(tmp[5]+month(tmp[1])+tmp[2]+time(tmp[3]))#年月日时
    matrix[i][3]=int(week(tmp[0])+quater(tmp[3]))#时间段，共28个
    matrix[i][4]=location(matrix[i][4])
    matrix[i][5]=venuetype(matrix[i][5])
    if matrix[i][4][3]=='CA' and matrix[i][4][2]!='':#去除非CA数据
        final_res.append(matrix[i])
#地点编码
total_loc=[]
for i in range(len(final_res)):
    total_loc.append(final_res[i][2])
total_loc = set(total_loc)
loc_num = [i for i in range(len(total_loc))]
loc_dic = dict(zip(total_loc,loc_num))
for i in range(len(final_res)):
    final_res[i][2]='l'+str(loc_dic[final_res[i][2]])

#生成loc_loc二元关系
loc_loc=''
for i in range(len(final_res)-1):
    if final_res[i][0]==final_res[i+1][0]:
        if final_res[i][1]-final_res[i+1][1]<250:
            loc_loc=loc_loc+(final_res[i][2]+' '+final_res[i+1][2]+'\n')
f = open("loc_loc.txt",'w')
f.write(loc_loc)
f.close
#地点类别去重编码成字典
#total_type=[]
#for i in range(len(final_res)):
#    for j in range(len(final_res[i][5])):
#        total_type.append(final_res[i][5][j])
#total_type = set(total_type)
#type_num = [i for i in range(len(total_type))]
#type_dic = dict(zip(total_type,type_num))

#地点类别去空格
for i in range(len(final_res)):
    for j in range(len(final_res[i][5])):
        final_res[i][5][j]=final_res[i][5][j].replace(' ','')
#生成loc_type二元关系
loc_type=''
for i in range(len(final_res)):
    for j in range(len(final_res[i][5])):
        loc_type = loc_type+(final_res[i][2]+' '+final_res[i][5][j]+'\n')
f = open("loc_type.txt",'w')
f.write(loc_type)
f.close
#生成loc_time二元关系
loc_time=''
for i in range(len(final_res)):
    loc_time=loc_time+(final_res[i][2]+' '+'t'+str(final_res[i][3])+'\n')
f = open("loc_time.txt",'w')
f.write(loc_time)
f.close
#生成user_loc二元关系
user_loc=''
for i in range(len(final_res)):
    user_loc=user_loc+(final_res[i][0]+' '+final_res[i][2]+'\n')
f = open("user_loc.txt",'w')
f.write(user_loc)
f.close
#地区去重编码成字典
#total_range=[]
#for i in range(len(final_res)):
#    total_range.append(final_res[i][4][2])
#total_range=set(total_range)
#range_num=[i for i in range(len(total_range))]
#range_dic=dict(zip(total_range,range_num))

#地区除空格
for i in range(len(final_res)):
    final_res[i][4][2]=final_res[i][4][2].replace(' ','')
#生成loc_range二元关系
loc_range=''
for i in range(len(final_res)):
    loc_range=loc_range+(final_res[i][2]+' '+final_res[i][4][2]+'\n')
f = open("loc_range.txt",'w')
f.write(loc_range)
f.close

