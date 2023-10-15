### 주석

‘주석은 코드로 아이디어를 제대로 표현하지 못했음을 나타내는 것이다’

- 주석이 좋지 않은 이유
    - 주석은 초보자로 하여금 읽기 어렵게 한다. 코드에 포함되어 있기 때문이다.
    - 개발자는 주석을 업데이트하는 것을 깜빡하는 경우가 많아, 현재 버전과 일치하지 않는 경우가 많다.

---

### 함수 이름과 파라미터 이름

함수 이름과 파라미터 이름은 충분히 설명적으로 작성한다.

```python
def if_way_is_exist_go_home_or_go_near_sauna():
	'''
	'''
	pass
```

---

### Docstring

docstring은 각 함수나 클래스에 추가할 수 있는 설명 문서이다.

docstring은 함수, 모듈, 클래스 선언부 아래에 멀티라인 주석(””” “””) 을 붙임으로써 추가할 수 있다. 함수, 클래스의 경우 들여쓰기는 필수이다.

1. 함수
    
    ```python
    def some_func():
    		""" some Function """
    ```
    
2. 클래스
    
    ```python
    def SomeClass():
    		""" Some Class """
    ```
    
3. 모듈
    
    ```python
    # some_module.py
    """ some Module """
    ```
    

함수, 클래스, 모듈에 적용되어 있는 docstring을 확인하고 싶으면 `__doc__` 을 통해 호출할 수 있다.

```python
some_func.__doc__
SomeClass.__doc__
some_module.__doc__
```

docstring일 필요한 이유는 파이썬이 동적 타이핑을 하기 떄문이다. 즉, 파이썬은 파라미터 타입이나 반환 타입 체크를 강요하지 않는다.

따라서 docstring에 함수,클래스,모듈의 설명 을 작성하고, 입력 인자 파라미터의 설명, 반환 설명 을 작성해둔다.

```python
def get_user_name(user):
		"""
			Description:
				유저의 객체를 통해 유저의 이름을 알아내는 함수.
			Param:
				some_module.user.User 클래스의 객체를 파라미터로 받음.
			Return:
				some_module.user_name.UserName 객체를 반환
		"""
		...
		return user_name
```

```python
>>> get_user_name??

```

- docstring 예시

```python
def data_from_response(response: dict) -> dict:
		""" response에 문제가 없다면 reponse의 payload를 반환

		- response 예제::
		{
		    "status": 200, # <int>
				"timestamp": "..." # 현재 시간의 ISO 포맷 문자열
        "payload": {"data": { ... }} # 반환하려는 사전 데이터
		}
		
		- 발생 가능한 예외:
			- HTTP status가 200이 아닌 경우 ValueError 발생
		"""
```

---

PEP-8

1. 들여쓰기는 공백 4개로 지정한다.
2. 한줄의 최대 글자는 79자로 제한한다.
3. 최상위 함수와 클래스 정의 사이에는 두줄씩 띄운다.
4. 파일은 UTF-8 또는 아스키(ASCII)로 인코딩한다.
5. 한 import 문에는 모듈 하나만 불러온다.
6. 소괄호나, 중괄호, 대괄호 사이에는 추가로 공백을 주지 않고, 쉼표 안에도 공백을 주지 않는다.
7. 클래스 이름만 카멜케이스(CamelCase)를 따른다.
8. 예외명은 Error로 끝낸다.
9. 함수 이름은 스네이크케이스(snake_case)를 따른다.
10. 비공개인 속성이나 메서드 이름은 밑줄 문자로 시작하자.
11. None을 비교할 때는 is를 사용한다.
12. 예외 처리문인 try는 필요한 것만 최소한으로 작성한다.
13. 접두사나 접미사 검사 시 startswith()와 endswith()를 사용한다.
14. 불린(boolean) 값은 ==으로 비교하지 않는다.

pep-8 자동 검사 라이브러리

```python
pip install pep8
```

```python
> pep8 hello.py
```

---

### Annotation

타입에 대한 힌트를 활성화시켜주는 역할을 수행한다.

```python
def get_user_name(user: User) -> UserName:
		"""

		"""
		return user_name
```

타입의 힌트를 준다고 해서 에러가 발생하거나 문제가 발생하지 않는다.

- Annotation 확인
    
    ```python
    >>> get_user_name.__annotations__
    ```