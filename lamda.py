people = [
    {"name":"John", "house":"Blue"},
    {"name":"Robert", "house":"Red"},
    {"name":"Aby", "house":"Purple"}
]

#def f(person):
#    return person["name"]

#people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)