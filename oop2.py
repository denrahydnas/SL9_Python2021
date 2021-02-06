class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)

#creates sub-item with various attributes
class Weapon(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power
        
class Inventory:
    #initialize list
    def __init__(self):
        self.slots = []
    #add item to list
    def add(self, item):
        self.slots.append(item)
    #count items in list
    def __len__(self):
        return len(self.slots)
    #searches list for item (bool) - in terminal, can be asked "'item' in listname"
    def __contains__(self, item):
        return item in self.slots
    #send results out of iterable w/o stopping process
    def __iter__(self):
        yield from self.slots