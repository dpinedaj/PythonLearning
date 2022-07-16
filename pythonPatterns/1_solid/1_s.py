# Single responsability principle
# A class should have just one responsability




class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
        
    def add_entry(self, entry):
        self.count += 1
        self.entries.append(f"{self.count}: {entry}")
        
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self):
        return '\n'.join(self.entries)

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry("I cried today")
j.add_entry("I ate a bug.")
print(f"Journal entries: \n{j}")

file = 'test.txt'
PersistenceManager.save_to_file(j, file)
                