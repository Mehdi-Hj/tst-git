def f():
    return True

def gen_name_age(name_list, age_list):
    for name, age in zip(name, age):
        yield name, age
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info():
        return self.name, self.age
