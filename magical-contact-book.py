class MagicalContact:
    def __init__(self, name, email, phone_number):
        self._name = name
        self._email = email
        self._phone_number = phone_number
    def name(self):
        return self._name
def email(self):
        return self._email
def phone_number(self):
        return self._phone_number
     def email(self, email):
        self._email = email
 def phone_number(self, phone_number)
        self._phone_number = phone_number
 def describe(self):
        print(f"Name: {self._name}, Email: {self._email}, Phone: {self._phone_number}")
class Wizard(MagicalContact):
    def __init__(self, name, email, phone_number, wand, house):
        super().__init__(name, email, phone_number)
        self._wand = wand
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            print("invalid")
        self._house = house
