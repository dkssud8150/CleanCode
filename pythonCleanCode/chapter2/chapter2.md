### pythonic

```python
nums = (1, 1, 2, 3, 5, 8, 13, 21)

>>> nums[2:4]
(2, 3)

>>> nums[::2]
(1, 2, 5, 13)
```

이러한 파이썬의 인덱싱과 슬라이시은 `__getitem__` 매직 메서드로 동작한다. `__getitem__`은 `myobject[key]` 와 같은 형태를 사용할 때 사용되는 메서드로, `__getitem`과 `__len__`을 사용하여 시퀀스나 이터러블 객체를 만들지 않고 키를 통해 객체의 특정 요소를 가져올 수 있다.


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
        
        def __exit(self, ext_type, ex_value, ex_traceback):
            start_database()

    @dbhandler_decorator()
    def offline_backup():
        run("pg_dump database")
    ```

    - 이렇게 컨텍스트 관리자를 데코레이터로 지정하게 되면, offline_backup 함수를 호출만 하더라도 컨텍스트 관리자 안에서 자동으로 실행된다.