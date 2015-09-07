###1
#data = ['a','b','c',['abcd','efg']] #리스트선언
#print(data[0])
##print('\n')
#print(data[-1])
#print(data[3][1])
#print(data[-1][-1])

###2
#b = [1,2,3]
#c = [3,4,5]
#d = ['life', 'is', 'too', 'short']

#print(b+c)
#print(b+d)
#print(b*3)
#print(d*3)

#f = b+c
#print(f)

###3
#guests = ['a','b','c','d']
#guests[0] = 'greenjoa'
#guests[1] = ['greenjoa1','greenjoa2']  

#print(guests[0])
#print(guests[1])
#print(guests[2])
#print(guests[3])
#print('\n')

#guests[1:3] = ['greenjoa1','greenjoa2'] 

#print(guests[0])
#print(guests[1])
#print(guests[2])
#print(guests[3])

###4
#data = ['minki0615', 'greenjoa', 'minkipang']

#data.insert(0,['minki0615','12345'])
#data.insert(1,['greenjoa','7890'])
#data.insert(2,['minkipang','abcd'])

#print(data[0])
#print(data[1])
#print(data[2])

#data1 = ['곽민기','010-2980-7869','서울시 노원구']
#data2 = ['이철헌','010-9334-0811','서울시 영등포구']
#data3 = ['최종윤','010-9892-9802','경기도 평택시']

#data[0].append(data1)
#data[1].append(data2)
#data[2].append(data3)

#print(data[0])
#print(data[1])
#print(data[2])

###5
#data = ['a','b','c',['abcd','efg']]

#for steps in data : #steps라는 변수 사용, data리스트 안에서(in)
#    print(steps)

#print('\n')

#for steps in range(4) : #리스트의 길이를 알 때, 모르면 length함수 사용
#    print(data[steps])

###6
#data = [15, 30, 27, 44, 1, 20]
#print(data)

#data.sort()
#print(data)

#data.reverse()
#print(data)

#topthree = [data[0], data[1], data[2]]
##print('top3 = ' + topthree)
#print(topthree)

###7
#data = ['a','b','c',['abcd','efg']]
#for steps in data :
#    if isinstance(steps, list) : #steps가 list의 인스턴스냐, 즉 steps가 list타입인지 확인하는 작업
#        for steps2 in steps :
#            print(steps2)
#    else :
#        print(steps)

###8
scores = [85, 63, 63, 45, 90]
num = scores.pop()  #맨 마지막꺼
print(scores)
print(num)

num = scores.pop(2) #2번째꺼
print(scores)
print(num)

scores2 = [85, 63, 63, 45, 90]
num = scores2.count(63)
print(num)  #63이 몇 개 있나 세주는 함수

scores2.extend([50,60])
print(scores2)

scores3 = [85, 63, 63, 45, 90]
scores3.append([50,60])
print(scores3)

