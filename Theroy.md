# 파이썬 문법 정리

# zip() 함수

zip() 함수는 2개 이상의 시퀀스를 짧은 길이를 기준으로 1 : 1 대응하는 새로운 튜플 시퀀스를 만들어 준다. 다음과 같이 a,b,c 리스트를 정의하고 zip(a,b)를 실행했다고 해보자.

```python
a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]
zip(a,b)
>> <zib object at 0x105b6d9b0>
```

위와 같은 결과로 출력되는데 이는 zip()함수가 제너레이터를 리턴하기 때문에 발생한다.

떄문에이러한 제너레이터에서 실제 결과값을 출력하고자 한다면 list()등과 같이 한번 더 묶어줘야 한다.

```python
list(zip(a,b))
[(1, 2), (2, 3), (3, 4), (4, 5)]
list(zip(a,b,c))
[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

또한 zip()의 결과 자체는 리스트 시퀀스가 아닌 튜플 시퀀스로 값을 변경하기 불가능한 불변(immutable) 객체이다.

이처럼 zip()은 여러 시퀀스에서 동일한 인덱스의 아이템을 순서대로 추출하여 튜플로 만들어주는 역할을 한다.

# 아스테리스크(\*)

파이썬에는 `아스테리스크(*)`혹은 별표라고 부르는 `*`가 존재한다. 이는 C의 포인터 변수와 혼동될 수 있으나 파이썬에는 포인터가 존재하지 않는다.

파이썬에서 아스테리스크(\*)가 하는 동작은 `언팩(Unpack)`이다. 말그대로 시퀀스 언패킹 연산자(Sequence Unpacking Operator)로 문자 그대로 시퀀스를 풀어 해치는 연산자를 의미하며, 튜플이나 리스트를 언패킹하는 데 사용한다.

언패킹을 하고 안하고의 차이가 어떤 결과를 가져오는지 예제를 통해 알아보자.

```python
nums = [1,1,1,2,2,3]
collections.Counter(nums).most_common(k)
>> [(1,3),(2,2)]
# 언패킹 진행했을 경우
list(zip(*collections.Counter(nums).most_common(k)))
>> [(1,2),(3,2)]
# 언패킹 하지않았을 때
list(zip(collections.Counter(nums).most_common(k)))
>> [((1,3),),((2,2),)]
```

위의 형태로 언패킹을 하지 않을 경우 엉뚱한 결과가 나온다.

또한 이러한 방법의 사용도 가능하다.

```python
fruits = ['lemon', 'pear'. 'watermelon', 'tomato']
# 위의 형태를 리스트의 형태가 아닌 문자열의 나열로 출력하고 싶은 경우 다양한 방법이 존재한다.
# for문을 사용하면서 print(~,end=' ')를 사용하던가 리스트의 인덱스에 접근하는 방식도 있지만
# 다음과 같은 방법도 가능하다.
print(*fruits)
>> lemon pear watermelon tomato
```

이외에도 \*는 활용도가 많다. 함수의 파라미터로 사용되는 경우 역으로 패킹(Packing)도 가능하다.

```python
def f(*params):
    print(parmas)

f('a','b','c')
>> ('a','b','c')
```

위의 형태로 하나의 파라미터를 받는 함수에 3개의 파라미터를 전달했지만, params 변수 하나로 패킹되어 처리된다.

이는 python3에서 print() 함수의 기본 동작 원리이기도 하다.

또한 다음과 같이 변수의 할당에도 이용이 가능하다.

```python
a, *b = [1,2,3,4]
a
>>> 1
b
>>> [2,3,4]

*a, b = [1,2,3,4]
a
>>> [1,2,3]
b
>>> 4
```

변수의 할당 도한 \*로 묶어서 처리가 가능하다.

마지막으로 \*\* 의 형태로 두개를 사용하는 경우도 있다. C의 더블포인터와는 전혀 다르다.

파이썬에서 \* 1개는 튜플 또는 리스트의 시퀀스 언패킹이었으면 \*\* 2개는 키/값 페어를 언패킹 하는데 이용된다.

```python
date_info = {'year' : '2020', 'month' : '01', 'day' : '7'}
new_info = {**date_info, 'day' : '14'}
new_info
>>> {'year' : '2020', 'month' : '01', 'day' : '14'}
```

이처럼 모든 요소를 언패킹할 수 있으며 여기서 동일한 키값('day')을 가지는 value값은 '14'로 업데이트또한 시도돼었다.

# dict.fromkeys() 딕셔너리 생성 메소드

> dict.fromkeys(seq,value)

- 딕셔너리를 생서할 때 편리하게 사용할 수 있는 메소드.seq 옵션 값에 문자열을 입력할 수도 있다.

- seq: 생성하려는 dictionary의 키(key)의 목록

- value: 생성하려는 dictionary의 값(value)

```python3
seq = ('name', 'age', 'sex')

dict_1 = dict.fromkeys(seq)
print(dict_1)

dict_2 = dict.fromkeys(seq, 10)
print(dict_2)

## result ##
{'age':None, 'name':None, 'sex':None}
{'age':10, 'name':10, 'sex':10}
```

# phython Operator.itemgetter 모듈
operator.itemgetter 모듈은 주로 sorted와 같은 함수의 key 매개변수에 적용되어 다중 수준의 정렬을 가능하게 해주는 모듈이다.

```python
# EX
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
```

이와 같은 형태일 때
```python
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

# 1번 값인 나이를 기준으로 정렬된다.
result = sorted(students, key=itemgetter(1))
print(result)
```
