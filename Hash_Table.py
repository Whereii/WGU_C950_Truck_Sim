#This is the first step in the process of building this project.
#In this step I needed to create my own custom hash class to use throught the
#rest of the program.

class hash_table:
    
    #Initialize a new array with 10 empty elements
    #fficiency -> O(1)
    def __init__(self):
        self.size = 10
        self.table = []
        for i in range(self.size):
            self.table.append([])

    #Insert item into hash-table
    #Efficiency -> O(1)
    def add(self, key, value):
        #Find location in table to store the data
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        #Check to see if the table already contains the key and if so then update it
        for key_check in container_list:
            if key_check[0] == key:
                key_check[1] = value
                return True
            
        #If the table does not contain the key then we need to add it
        new_pair = [key, value]
        container_list.append(new_pair)
        return True
    

    #Search the table for key and return the value
    #Efficiency -> O(n)
    def search(self, key):
        hash_key = hash(key) % len(self.table)
        target_container = self.table[hash_key]

        for item in target_container:
            if item[0] == key:
                return item[1]
        return None
    
    #Remove item from table with the matching key
    #Efficiency -> O(n)
    def remove(self, key):
        hash_key = hash(key) % len(self.table)
        target_container = self.table[hash_key]

        for item in target_container:
            if item[0] == key:
                target_container.remove([item[0], item[1]])


