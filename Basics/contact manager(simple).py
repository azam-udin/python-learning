# Simple contact manager
def add_contact(name, phone, filename="contacts.txt"):
    """Add a contact to the file"""
    with open(filename, "a") as file:
        file.write(f"{name},{phone}\n")
    print(f"Contact {name} added successfully!")

def view_contacts(filename="contacts.txt"):
    """View all contacts"""
    try:
        with open(filename, "r") as file:
            print("\nContacts:")
            print("-" * 30)
            for line in file:
                name, phone = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found. File doesn't exist yet.")

# Usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
view_contacts()