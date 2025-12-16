from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

u1 = User(id=1,name="vishwas",age=25)
u3 = User(id=1,name="vish",age="45")
print(u1)
print(type(u1.age))
print(u3)
print(type(u3.age))
# u2 = User(id=1,name="vishwas",age="twenty")