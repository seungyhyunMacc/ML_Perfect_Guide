## np.sort()는 원행렬 그대로 유지한채 행렬 반환
## ndarray.sort()는 원행렬 자체를 정렬한 형태로 변환, 반환값은 None

## np.sort()나 ndarray.sort()는 모두 기본적으로 오름차순, [::-1]을 쓰면 내림차순 가능

## np.argsort()는 원본 행렬 정렬 시 정렬된 원본 행렬 인덱스 반환 ---> [3(0) 1(1) 9(2) 5(3)] ---> [1(1) 3(0) 5(3) 9(2)] ---> 1, 0, 3, 2

## np.dot(A, B) --> 행렬 내적
## np.transpose(A) --> 전치 행렬
import numpy as np
org_array = np.array([ 3, 1, 9, 5]) 
print('원본 행렬:', org_array)

# np.sort( )로 정렬 
sort_array1 = np.sort(org_array)         
print ('np.sort( ) 호출 후 반환된 정렬 행렬:', sort_array1) 
print('np.sort( ) 호출 후 원본 행렬:', org_array)

# ndarray.sort( )로 정렬
sort_array2 = org_array.sort()
org_array.sort()
print('org_array.sort( ) 호출 후 반환된 행렬:', sort_array2)
print('org_array.sort( ) 호출 후 원본 행렬:', org_array)

sort_array1_desc = np.sort(org_array)[::-1]
print ('내림차순으로 정렬:', sort_array1_desc) 


array2d = np.array([[8, 12], 
                   [7, 1 ]])

sort_array2d_axis0 = np.sort(array2d, axis=0)
print('로우 방향으로 정렬:\n', sort_array2d_axis0)

sort_array2d_axis1 = np.sort(array2d, axis=1)
print('컬럼 방향으로 정렬:\n', sort_array2d_axis1)

#### argsort ####
org_array = np.array([ 3, 1, 9, 5]) 
print(np.sort(org_array))

sort_indices = np.argsort(org_array)
print(type(sort_indices))
print('행렬 정렬 시 원본 행렬의 인덱스:', sort_indices)

org_array = np.array([ 3, 1, 9, 5]) 
print(np.sort(org_array)[::-1]) ## 내림차순

sort_indices_desc = np.argsort(org_array)[::-1]
print('행렬 내림차순 정렬 시 원본 행렬의 인덱스:', sort_indices_desc)

## key-value 형태의 데이터를 John=78, Mike=95, Sarah=84, Kate=98, Samuel=88을 ndarray로 만들고 argsort()를 이용하여 key값을 정렬
name_array=np.array(['John', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array=np.array([78, 95, 84, 98, 88])

# score_array의 정렬된 값에 해당하는 원본 행렬 위치 인덱스 반환하고 이를 이용하여 name_array에서 name값 추출.  
sort_indices = np.argsort(score_array)
print("sort indices:", sort_indices)

name_array_sort = name_array[sort_indices]

score_array_sort = score_array[sort_indices]
print(name_array_sort)
print(score_array_sort)

