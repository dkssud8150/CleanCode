# 컨텍스트 매니저
import contextlib

## 데코레이터 클래스 생성
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        print("system stop for DB update")
    
    def __exit__(self, ext_type, ex_value, ex_traceback):
        print("system start for DB update")

@dbhandler_decorator()
def offline_backup():
    print("pg_dump database")


## 데코레이터 함수로 생성
@contextlib.contextmanager
def DBHandler():
    print("system stop for DB")
    yield
    print("system start for DB")

def db_backup():
    print("database backup")

with DBHandler():
    db_backup()



# 프로퍼티 객체
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


# 컨테인 객체
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


class DynamicAttributes:
    def __init__(self):
        pass

    def __getattr__(self, attr):
        pass

    def __setattr__(self, attr):
        if attr in dir(self):
            pass