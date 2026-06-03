class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            current_person = Person.people[person["name"]]
            wife_person = Person.people[person["wife"]]
            current_person.wife = wife_person

        elif person.get("husband"):
            current_person = Person.people[person["name"]]
            husband_person = Person.people[person["husband"]]
            current_person.husband = husband_person

    return result
