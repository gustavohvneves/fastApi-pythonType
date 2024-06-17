from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    
    return f"Hello {name}"

def get_full_name(first_name:str, last_name:str):
    full_name=first_name.title()+" "+last_name.title()
    return full_name

def get_name_with_age(name:str, age:int):
    name_with_age = name + "is this old: "+ str(age)
    return name_with_age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

def process_items(items: list[str]):
    for item in items:
        print(item)

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

print(get_full_name("john","doe"))
print(say_hello("joker"))