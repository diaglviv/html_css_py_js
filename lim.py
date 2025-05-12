people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cho Chang", "house": "Ravenclaw"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Hermione", "house": "Griffindor"},
    {"name": "Ron", "house": "Griffindor"},
    {"name": "Neville", "house": "Griffindor"},
    {"name": "Luna", "house": "Ravenclaw"},
]

people.sort(key=lambda person: person["name"])

print(people)