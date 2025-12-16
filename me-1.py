def f():
    return True

def gen_name_age(name_list, age_list):
    for name, age in zip(name, age):
        yield name, age

