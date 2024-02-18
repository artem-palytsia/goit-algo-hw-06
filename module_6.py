from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def validate(self):
        return True  # Базовий метод, буде перевизначено у підкласах

class Name(Field):
    def validate(self):
        return bool(self.value.strip())  # Перевіряємо, чи ім'я не порожнє

class Phone(Field):
    def validate(self):
        # Перевіряємо, чи має номер телефону правильний формат (10 цифр)
        return len(str(self.value)) == 10 and str(self.value).isdigit()

    def __init__(self, value):
        super().__init__(value)
        if not self.validate():
            raise ValueError("Invalid phone number format")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
