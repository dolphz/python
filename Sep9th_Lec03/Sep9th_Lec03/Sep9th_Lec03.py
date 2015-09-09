####1 dictionary 자료형 알아보기
#dic = {'name':'minki','phone':'01029807869','birth':'0615'}
#print(dic)
#print(dic['name'])

#dic2 = {1:'hi',2:'hello'}
#print(dic2)
#print(dic2[1])
#print(dic2[2])

#k = dic.keys()
#print('\n*** 키 반환, 리스트 변환 ***')
#print(k)
#l = list(k)
#print(l)

#b = dic.items() #key-value 쌍으로 얻기
#print(b)

#dic.clear() #다 지우기
#print(dic)



####2 영화별점 예제
#minkiscore = {'베테랑':'5.0', '암살':'4.7', '타짜':'4.9', '추격자':'5.0'}
#hyogunscore = {'베테랑':'4.6', '암살':'4.9', '타짜':'4.1', '추격자':'5.0'}

#movie = {'minki':minkiscore,'hyogun':hyogunscore}
#print(movie) #전체인원 평점현황
#print('\n')
#print('* 곽민기 영화 평점 : ' + minkiscore) #곽민기 평점현황
#print('* 김효건 영화 평점 : ' + hyogunscore) #김효건 평점현황

#print('\n')
#murder = minkiscore.get('암살')
#print('* 곽민기 암살 평점 : ' + murder) #곽민기의 암살 평점

#--------------------영화별점예제 추가
#moviescore = {'곽민기':{'베테랑':'5.0', '암살':'4.7', '타짜':'4.9', '추격자':'5.0'},
#              '김효건':{'베테랑':'4.6', '암살':'4.9', '타짜':'4.1', '추격자':'5.0'}}

#print(moviescore)
#print(moviescore.get('곽민기'))
#print(moviescore.get('김효건'))
#print(moviescore.get('곽민기').get('타짜'))
#print(moviescore['곽민기']['타짜'])



####3 if문 사용
#answer = input('택배를 보내시겠습니까? : yes/no?')

#mainanswer = answer.lower()
##answer.lower()만 하면 answer의 값은 그대로 유지되고 answer가 lower된 것만 반환되서 어디에도 저장되지 않음

#if mainanswer == 'yes' :
#    print('1000원입니다.')

#elif mainanswer == 'no' :
#    print('안녕히 가세요')

#else :
#    print('다시 입력하세요')

#print("좋은 하루 되세요")



####4 for문 사용해서 구구단 짜기
#print('구구단을 외자! 구구단을 외자!')
#print('') #한 줄 띄기, \n으로하면 두 줄 띄어짐

#for i in range(2,10,1):
#    print('- %d단 -' % i)
#    for j in range(1,10,1):
#        print('%d * %d = %d' % (i,j,i*j))
#    print('') #한 단 끝날때마다 줄바꿈하기


####5 Turtle(그리기 라이브러리) 사용
#import turtle
#nSides = 8  #nSides 값에 따라 다각형의 꼭지점 수가 결정된다.
#for i in range(nSides):
#    turtle.forward(100)
#    turtle.right(360/nSides) #네모그리는 작업

#    for j in range(nSides):
#        turtle.forward(50)
#        turtle.right(360/nSides)



###6 while문