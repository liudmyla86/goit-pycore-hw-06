from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if self.validate == value:
            super().__init__(value)
        else:
            raise ValueError (f"Phone number {value} is invalid. must be 10 digits")

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10



class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number ):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = Phone(new_number).value
                break
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.new.value] = record

    def find_record(self, name):
        return self.data.get(name)
     
    def delete_record(self, name):
        if name in self.data:
            del self.data [name] 