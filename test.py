from dataclasses import dataclass

@dataclass
class person:
    name: str
    age: int
    city: str   
person1 = person("Tom", 25, "New York")
print(person1.city)
