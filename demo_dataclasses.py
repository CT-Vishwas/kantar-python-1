from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    city: str
    age: int

# __init__
# __repr__
# __eq__

u1 = User(1,"vishwas","pune","25")
print(u1)
print(u1.city)