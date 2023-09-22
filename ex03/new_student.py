import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    """Generate login from name and surname"""
    return f"{name[0]}{surname}"


@dataclass
class Student:
    """Student class"""
    id: str = field(default_factory=generate_id, init=False)
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)

    def __post_init__(self):
        """__post_init__ function"""
        self.login = generate_login(self.name, self.surname)
