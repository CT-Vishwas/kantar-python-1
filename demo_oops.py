class Person:
    __slots__ = ["user_name","user_city"]
    def __init__(self, uname="UNKNOWN", city="UNKONWN"):
        self.user_name = uname
        self.user_city = city

    def speak():
        print("the person is speaking")

class User(Person):
    def __init__(self, uname="UNKNOWN", city="UNKONWN", salary=10000):
        super().__init__(uname, city)
        self.salary = salary

p1 = Person("vishwas", "Bangalore")
print(p1.user_name)
p1.age = 25
print(p1.age)

# print(p1.__dict__)
# p2 = Person("arjun","Chennai")
# print(p2.user_name)

# u1 = User(uname="Jane", city="NewYork", salary=25000)
# print(u1.user_city,u1.salary)