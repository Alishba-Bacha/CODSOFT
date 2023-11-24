# CONTACT BOOK:
#Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.

print("\n****WELCOME TO CONTACT BOOK****")
contacts = []

# Function to add a new contact
def addContact(name, phone, email, address):
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print( "Contact added successfully.")
    return ""

# Function to view the contact list
def viewContactList():
    if not contacts:
        return "Contact list is empty."
    else:
        print("s.No, Name    Contact")
        for index, contact in enumerate(contacts):
            print(f"{index + 1}.   {contact['name']},    {contact['phone']}")
        return ""

# Function to search for a contact
def searchContact(query):
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)
    for index, contact in enumerate(results):
            print(f"{index + 1}.   {contact['name']},    {contact['phone']}")
            return " "
    
    return results

# Function to update a contact
def updateContact(name, newPhone, newEmail, newAddress):
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = newPhone
            contact['email'] = newEmail
            contact['address'] = newAddress
            print("Contact updated successfully.")
            return "Updated"
        else:
            print("Contact not found.")
    return ""

# Function to delete a contact
def deleteContact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print( "Contact deleted successfully.")
        else:
            print("Contact not found.")
    return " "

while(True):
    print("\n1: Add Contact ")
    print("2: view Contact")
    print("3: Search Contact")
    print("4: Update Contact")
    print("5: Delete Contact")
    choice = int(input("\nEnter operation you want to perform: '1', '2','3','4','5': "))

    if choice == 1:
        name1 = input("Enter name: ")
        phone1 = input("Enter phone number: ")
        email1 = input("Enter email: ")
        address1 = input("Enter address: ")
        addContact(name1, phone1, email1, address1)

    elif choice == 2:
        viewContactList()
    
    elif choice == 3:
        search_num = input("Enter name or contact number to search for a contact: ")
        searchContact(search_num)
    elif choice == 4:
        name1 = input("Enter name of contact to update his/her details : ")
        phone1 = input("Enter phone number: ")
        email1 = input("Enter email: ")
        address1 = input("Enter address: ")
        updateContact(name1, phone1, email1, address1)
    elif choice == 5:
        name1 = input("Enter name to delete the contact: ")
        deleteContact(name1)
    else:
        print("choice not found")

                   
