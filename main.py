class Person:
    def __init__(self, name, birth_year, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.mother = mother
        self.father = father

    def __str__(self):
        return f"{self.name} ({self.birth_year})"
        
class FamilyTree:
    def __init__(self):
        self.people = []

    def add_person(self, name, birth_year, mother=None, father=None):
        person = Person(name, birth_year, mother, father)
        self.people.append(person)

    def get_person(self, name):
        for person in self.people:
            if person.name == name:
                return person
        return None

    def display(self):
        for person in self.people:
            mother_name = person.mother.name if person.mother else "unknown"
            father_name = person.father.name if person.father else "unknown"
            print(f"{person.name} ({person.birth_year}), mother: {mother_name}, father: {father_name}")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for person in self.people:
                mother_name = person.mother.name if person.mother else "unknown"
                father_name = person.father.name if person.father else "unknown"
                f.write(f"{person.name},{person.birth_year},{mother_name},{father_name}\n")

    def load_from_file(self, filename):
        self.people = []
        with open(filename, "r") as f:
            for line in f:
                name, birth_year, mother_name, father_name = line.strip().split(",")
                mother = self.get_person(mother_name) if mother_name != "unknown" else None
                father = self.get_person(father_name) if father_name != "unknown" else None
                self.add_person(name, int(birth_year), mother, father)

# Example usage:
tree = FamilyTree()
tree.add_person("Alice", 1980)
tree.add_person("Bob", 1985, tree.get_person("Alice"))
tree.add_person("Charlie", 2010, tree.get_person("Bob"), tree.get_person("Alice"))
tree.display()
tree.save_to_file("family_tree.csv")
tree.load_from_file("family_tree.csv")
tree.display()
