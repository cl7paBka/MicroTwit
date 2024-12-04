from typing import Optional, List
from pydantic import BaseModel


# Абстрактный класс, который наследуется UserProfile'ом
class BasicUserInfo(BaseModel):
    id: int
    name: str


class UserProfile(BasicUserInfo):
    followers: Optional[List[BasicUserInfo]] = None
    following: Optional[List[BasicUserInfo]] = None
