class Phone:
    def __init__(self):
        self.__contacts = {}  # Private dictionary to store contacts
    
    def add_contact(self, name, number):
        """Add a new contact"""
        if name not in self.__contacts:
            self.__contacts[name] = number
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists.")
    
    def remove_contact(self, name):
        """Remove a contact"""
        if name in self.__contacts:
            del self.__contacts[name]
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found.")
    
    def make_call(self, name):
        """Make a call to a contact"""
        if name in self.__contacts:
            print(f"Calling {name} at {self.__contacts[name]}...")
        else:
            print(f"Contact '{name}' not found.")

class Camera:
    def take_pic(self):
        """Take a picture"""
        print("The picture was taken successfully")

class Smartphone(Phone, Camera):
    def __init__(self):
        Phone.__init__(self)
        Camera.__init__(self)
        print("Smartphone initialized")
    
    def use_all_features(self):
        """Demonstrate all features"""
        self.add_contact("Mom", "123-456-7890")
        self.add_contact("Dad", "987-654-3210")
        self.make_call("Mom")
        self.make_call("Unknown")
        self.take_pic()

# Example usage
if __name__ == "__main__":
    my_phone = Smartphone()
    my_phone.use_all_features()
    
    # Test individual methods
    my_phone.add_contact("Friend", "555-1234")
    my_phone.make_call("Friend")
    my_phone.remove_contact("Dad")
    my_phone.take_pic()