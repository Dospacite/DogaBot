from abc import ABC
from dataclasses import dataclass


@dataclass()
class Group(ABC):

    corporationId: str
    corporationName: str
    schoolId: str
    schoolName: str
    roleId: int
    roleName: str
    classroom: int
    sharedGroupId: int
    sharedGroupName: str
