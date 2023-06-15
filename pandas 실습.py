
#pandas 복기

import pandas as pd
import numpy as np

data= np.arange(0,50,10)
print(data)

a = pd.Series(data, index=['a','b','c','d','e'])
print(a)

#명시적 인덱스
b=pd.Series(data)
b

#암시적 인덱스
a['b']
a.loc['b']  #명시한 인덱스
a.iloc[1]   #순서

#분리형 인덱스
a[a>15]

#--------------------------------
#집계함수

a.add(100)      #덧셈
a.sub(100)      #뺼셈
a.mul(100)      #곱하기
a.div(100)      #나누기
a.mod(100)      #나머지

a.min()
a.max()
a.sum()
a.mean()
a.median()
a.std()     #표준편차
a.str()     #분산



rawData = np.random.randint(50,100,size=(4,3))
rawData

df = pd.DataFrame(rawData, 
                  index=['1반','2반','1반','2반'],
                  columns=['국','영','수'])

df['국']
# df[0] -> error

df['평균'] = round((df['국'] + df['영'] + df['수']) /3,2)
df

#삭제
df['na'] = np.nan
del df['na']

df[df.평균 > 80]
df = df.drop(['평균'], axis= 'columns')



#-----------------------------------------
#결측값 처리

df = df.astype('Float64')
df['수'][2]  = np.nan


#행, 열 단위 삭제
df.dropna(axis=0)      #row삭제     #원본 수정 x
# df.dropna(axis=0, inplace=True)   #원본 수정 O

df.dropna(axis=1)      #col 삭제         

#대체
# 왜 난 mean 이랑 hello는 안들어가는거야ㅜㅜㅜ
df.fillna('hello')
df.fillna(0)
df.fillna(df.mean) 

df.mean


#-----------------------------------------
#multiIndex

df .T  #행렬전환

df.index = [['1학년','1학년','2학년','2학년'],['1반','2반','1반','2반']]
df.columns=[['언어','언어','수리'],['국','영','수']]

df['언어']
df.iloc[0]
df.loc['1학년'].loc['1반']



#-----------------------------
#데이터 사전분석

df.info()
df.head()
df.tail()
df.dtypes
df.describe()       #기초 대표값 반환 
df.isnull().sum()


#값의 연결

a=pd.DataFrame(np.arange(1,10).reshape(3,3))
a

b=pd.Series(np.arange(10,40,10))
b

#옆에 추가 : pd         .   concat
#밑에 추가 : (df이름)   .   append

pd.concat([a,b], axis=1, ignore_index=True)
a.append(b, ignore_index=True)