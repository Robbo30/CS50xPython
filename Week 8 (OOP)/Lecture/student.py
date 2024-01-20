class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return (f"{self.name} from {self.house}")
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)
    
    @property
    def name(self):
             return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House Name")
        self._house = house
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russel":
                return "🐶"
            case _:
                return "Nothing happend"


def main():
    student = Student.get()
    print(f"{student.name} from {student.house}!")
    print(f"Expecto Patronum!  .... {student.charm()}")


if __name__ == "__main__":
    main()

