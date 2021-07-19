#!/usr/bin/env python
# coding: utf-8

# ### 공공데이터에서 관련 데이터 수집 후 카페 업종 현황 확인
# 
# - 전국 카페 데이터를 모두 수집
# - 서울 지역의 점포 현황 확인
# 
# 데이터 : https://www.data.go.kr/data/15083033/fileData.do

# In[1]:


# 라이브러리를 불러옵니다.
import pandas as pd
import numpy as np


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# # 데이터 불러오기

# In[3]:


# 다운 받은 데이터 중 1개 가져오기
tmp = pd.read_csv('../data/store/소상공인시장진흥공단_상가(상권)정보_인천_202103.csv')
tmp.head()


# In[4]:


tmp.info()


# ### 파일관련 편리한 모듈
# 
# 
# - pickle
#     - 파일에 읽고 쓰는 작업을 함수를 통해 한번에 진행시켜 줌
# - glob
#     - 파일들의 리스트를 뽑을 때 사용
#         - 파일의 경로명과 기호를 이용해서 원하는 파일 경로를 생성해 낼 수있음
# - os
#     - 운영체제의 파일 관련 작업 명령에 대한 함수를 제공 함
# 

# In[10]:


# pickle 모듈
users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}

# 파일에 users data 쓰기
f=open('user.txt', 'wb')

import pickle
pickle.dump(users,f)
f.close()


# In[12]:


f = open('user.txt', 'rb')
a = pickle.load(f)
a


# In[14]:


import os

os.path.exists('user.txt')
os.path.exists('../user.txt')


# In[17]:


from glob import glob

glob('*.ipynb') # 현재 디렉터리의 *.ipynb인 파일의 파일목록 반환

glob('../data/*.csv') # 현재 디렉터리의 상위 디렉터리로 접근 후  data 디렉터리안에 있는  csv  파일 리스트 반환(경로도 같이 반환)


# In[19]:


## 해당 파일 리스트가 디렉터리인지 확인
from glob import glob
from os.path import isdir

for x in glob('../data/*') : 
    if isdir(x) : # x가 디렉터리면
        print(x, '<DIR>')
    else :
        print(x)


# In[6]:


# data 폴더에 있는 모든 csv 파일을 읽어오기

from glob import glob

# csv 목록 불러오기
file_names = glob("../data/store/*.csv")
file_names


# In[7]:


# csv 읽어와서 기존 df에 결합 : concat 함수 사용

total = pd.DataFrame() # 빈 데이터프레임 생성

# 모든 csv 병합하기
for file_name in file_names:
    temp = pd.read_csv(file_name, sep=',', encoding='utf-8')
    total = pd.concat([total, temp])


# In[8]:


total.shape


# In[20]:


total.info()


# In[21]:


# index  재설정
total.reset_index(inplace=True, drop=True)


# In[22]:


total.info()


# In[23]:


# 사용할 컬럼만 선택 : 기본 인덱싱 사용 => df[[컬럼1, 컬럼2,....]]

data = total[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명', '시도명',
             '시군구명', '행정동명']]

data


# In[25]:


data.info()
total.info()  # 필요없는 데이터면서 메모리를 많이 차지하므로 삭제해야 함


# In[26]:


# 원 소스 파일도 존재하고 필요한 데이터를 추출 했으므로   total  데이터는 삭제
del total


# In[27]:


total.head()


# In[28]:


data.info()


# In[32]:


data['상권업종대분류명'].unique()
set(data['상권업종중분류명'])
data['상권업종중분류명'].unique()

# 분석대상인 커피전문점은 중분류의 커피점/카페 로 확인


# In[35]:


# 카페 정보만 추출

df_cafe = data[data['상권업종중분류명']=='커피점/카페']

df_cafe.reset_index(inplace=True, drop=True)

print("전국 카페 매장 수 : ", len(df_cafe))

df_cafe.head()


# ### 지역별 커피 전문점

# In[36]:


set(data['시도명'])
len(set(data['시도명']))


# In[38]:


##  전체 data인 data df에서 서울시의 카페 데이터를 추출
df_seoul_cafe = data[(data['상권업종중분류명']=='커피점/카페') & (data['시도명']=='서울특별시')]
## 인덱스 정리(index 속성 이용)
range(len(df_seoul_cafe))
df_seoul_cafe.index = range(len(df_seoul_cafe))
df_seoul_cafe.info()


# In[ ]:





# In[ ]:





# In[ ]:




