### pythonic

```python
nums = (1, 1, 2, 3, 5, 8, 13, 21)

>>> nums[2:4]
(2, 3)

>>> nums[::2]
(1, 2, 5, 13)
```

이러한 파이썬의 인덱싱과 슬라이시은 `__getitem__` 매직 메서드로 동작한다. `__getitem__`은 `myobject[key]` 와 같은 형태를 사용할 때 사용되는 메서드로, `__getitem`과 `__len__`을 사용하여 시퀀스나 이터러블 객체를 만들지 않고 키를 통해 객체의 특정 요소를 가져올 수 있다.

&nbsp;

---

### context manager

컨텍스트 관리는 리소스 관리와 코드 분리를 수행한다.

- 리소스 관리는 with문을 사용하여 할당된 리소스를 사용 끝날 때 해제해주는 용도이다.
    
    ```python
    with open(file_name) as fd:
        process_file(fd)
    ```

- 코드 분리는 주요 동작 전후에 작업을 실행하려고 할 때나 독립적으로 코드를 분리해야 할 때 사용한다.

    ```python
    import contextlib

    class dbhandler_decorator(contextlib.ContextDecorator):
        def __enter__(self):
            stop_database()
        
        def __exit__(self, ext_type, ex_value, ex_traceback):
            start_database()

    @dbhandler_decorator()
    def offline_backup():
        run("pg_dump database")
    ```

    - 이렇게 컨텍스트 관리자를 데코레이터로 지정하게 되면, offline_backup 함수를 호출만 하더라도 컨텍스트 관리자 안에서 자동으로 실행된다.

&nbsp;

---

### Property

`@property` 데코레이터는 일반적인 `getter`의 역할과 같으며, `@<property>.setter` 데코레이터는 `setter`와 같은 역할이다.

`getter`, `setter`는 타 언어에서 객체의 속성에 대한 접근을 제어할 때 사용된다.

```python
class User:
    def __init__(self, username) -> None:
        self.username = username
        self._email = None
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError("유효한 이메일이 아닙니다.")
        
        self._email = new_email
```

```bash
>>> user = User("clean_user")
>>> user.email = "clean_user"
유효한 이메일이 아닙니다.
>>> user.email = "clean_user@example.com"
'clean_user@example.com'
```

프로퍼티의 장점은 명령-쿼리 분리 원칙을 따르기에 용이하다. 

`@property` 데코레이터는 응답하기 위한 query이며, `@<property>.setter` 데코레이터는 무언가를 하기 위한 command 이다.

&nbsp;

일반적인 프로그래밍 언어는 public, private, protected 세가지 프로퍼티를 가지지만, 파이썬은 모든 프로퍼티와 함수가 public이다. 따라서 호출자는 모든 객체의 속성을 호출할 수 있다. 그래서 밑줄을 사용하여 타 언어처럼 private 과 같은 용도로 사용되기도 한다. 밑줄을 사용한다고 해서 호출하지 못하는 것은 아니다.

&nbsp;

---

### 이터러블 객체

이터러블과 이터레이터가 있는데, 이터러블은 `__iter__` 매직 메서드를 구현한 객체고, 이터레이터는 `__next__` 매직 메서드를 구현한 객체이다.

객체가 반복 가능한지를 확인하기 위해서 객체에 `__iter__`, `__next__` 중 하나를 포함하는지 체크하고, `__len__`, `__getitem__` 메서드를 모두 가졌는지 확인해보면 된다.

```python
_subject = [1,2,3,4,5,6]

assert all([m in dir(_subject) for m in ["__iter__","__next__"]])
assert any([m in dir(_subject) for m in ["__len__","__getitem__"]])
```

&nbsp;

```python
from datetime import timedelta, date

class DateIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        print("iter 실행")
        return self

    def __next__(self):
        print("next 실행", end=" ")
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today
    
for day in DateIterable(date(2023, 1, 1), date(2023, 1, 12)):
    print(day)

"""
iter 실행
next 실행 2023-01-01
next 실행 2023-01-02
next 실행 2023-01-03
next 실행 2023-01-04
next 실행 2023-01-05
next 실행 2023-01-06
next 실행 2023-01-07
next 실행 2023-01-08
next 실행 2023-01-09
next 실행 2023-01-10
next 실행 2023-01-11
next 실행 
"""
```

for문을 실횅하면 `__iter__` 메서드를 처음에 간 후, `__next__`로 넘어가고, for문안으로 들어가서 코드가 진행된다.

&nbsp;

```python
iter(DateIterable(date(2023, 1, 1), date(2023, 1, 2)))

"""
iter 실행

<__main__.DateIterable at 0x17669b77ad0>
"""
```

iter함수는 객체 내부에 `__iter__`를 먼저 찾고, 정의되어 있지 않으면 `__getitem__`을 찾고 없으면 TypeError를 발생시킨다.

&nbsp;

---

### 컨테이너 객체

`__contains__()`는 일반적으로 `Boolean` 값을 반환하도록 구현하는 데, 해당 키워드는 `in` 키워드가 발견될 때 호출된다.

```python
# 컨테이너 객체
class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height

class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.limit = Boundaries(width, height) # 의도가 직관적으로 파악됨

        self.grid = self.make_grid()

    def __contains__(self, coord):
        return coord in self.limit

    def make_grid(self):
        import copy
        grid = [[0] * self.width] * self.height
        self.arr = copy.deepcopy(grid)

# Usage
def mark_coordinate(grid, coord):
    if coord in grid:
        x, y = coord
        grid.arr[y][x] = -1
        print(grid.arr)
    
>>> grid = Grid(3,3)
>>> mark_coordinate(grid, (2,2))
[[0, 0, -1], [0, 0, -1], [0, 0, -1]]

>>> assert (4,4) in grid
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AssertionError
```

`in`절을 통해 직관적으로 `Grid`안에 있는지 체크한다는 것을 직관적으로 볼 수 있다.

&nbsp;

---

### __getattr__

`my_car.name`을 호출하면 객체 사전에서 `name`을 찾아서 `__getattribute__`을 호출하여 객체에 없을 경우 속성 이름을 파라미터로 전달하여 `__getattr__(name)`을 호출한다. 이를 통해 속성이 있으면 반환하고, 없으면 새로운 속성을 만들어낼 수 있다.

```python
class DynamicAttributes:
    def __init__(self):
        pass

    def __getattr__(self, attr):
        pass

    def __setattr__(self, attr):
        if attr in dir(self):
            pass

```