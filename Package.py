import csv
from Hash_Table import hash_table

#Part 2 of this project. I need to create a way to store the package information
#into individual package objects

class package:

    def __init__(self, id, address, city, state, zip, delivery_time, note, size, status, time_delivered, time_departed):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_time = delivery_time
        self.status = status
        self.note = note
        self.size = size
        self.time_delivered = time_delivered
        self.time_departed = time_departed
    
    def get_id(self):
        return self.id
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip(self):
        return self.zip
    
    def get_delivery_time(self):
        return self.delivery_time
    
    def get_status(self):
        return self.status
    
    def get_note(self):
        return self.note
    
    def get_size(self):
        return self.size
    
    def get_time_delivered(self):
        return self.time_delivered
    
    def get_time_departed(self):
        return self.time_departed

#This method converts the package data into individual package objects and then puts
#the objects into my custom hash table. It returns the hashtable.
#Efficiency -> O(n)
def load_package_data():

    table = hash_table()

    with open('./Data/packageCSV.csv', encoding='utf-8-sig') as file:
        reader = csv.reader(file)

        for row in reader:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            delivery_time = row[5]
            size = row[6]
            note = row[7]
            status = 'At Hub'
            time_delivered = ''
            time_departed = ''

            new_package = package(id, address, city, state, zip, delivery_time, note, size, status, time_delivered, time_departed)

            table.add(id, new_package)

    return table

