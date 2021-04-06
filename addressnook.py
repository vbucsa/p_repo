contactList = {}

class Person:
    def __init__(self, name, email, tel):
        self.name = name
        self.email = email
        self.tel = tel
def Add(Person):
    name = input("Name: ")
    email = input("Email: ")
    tel = input("Telephone number: ")
    contactList[f'{name}'] = [f'{email}', f'{tel}']

def List():
    for word in contactList.items():
        print(f'Name: {word}; Email: {word}; Tel. number: {word}')

def Delete():
    del_contact = input('Delete contact: ')
    if del_contact in contactList: 
        del contactList[f'{del_contact}']
        print(f'Contact {del_contact} has been deleted')

def Modify():
    List()
    select_contact = input('Select a contact: ')
    # if contactList.has_key(select_contact):

while True:
    command = input('Enter a command: Add / List / Delete / Modify: ')
    print()
    if command == 'Exit':
        break
    elif command == 'List':
        List()
    elif command == 'Add':
        Add(Person)
    elif command == 'Delete':
        Delete()
    elif command == 'Modify':
        Modify()



    


