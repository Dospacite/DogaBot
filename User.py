from abc import ABC
from dataclasses import dataclass


@dataclass()
class User(ABC):

    id: str
    fullName: str
    roleId: int
    roleName: str
    professionName: str
    schoolId: str
    username: str
