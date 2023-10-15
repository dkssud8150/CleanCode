# 모듈(파일이름)은 스네이크케이스(snake_case)
from modules.some_module import some_func, someClass

from some_module.user import User
from some_module.user_name import UserName

def get_user_name(user: User) -> UserName:
    """
        Description:
            유저의 객체를 통해 유저의 이름을 알아내는 함수
        Param:
            some_module.user.User 클래스의 객체를 파라미터로 받음
        Return:
            some_module.user_name.UserName 객체를 반환
    """

    user_name = User.user_name
    
    return user_name

