import csv

#Part B - Step 2: In this class I am able to take all the address data and convert it into
#an array for later use when checking the distances between different locations
class addresses:

    def __init__(self):
        self.address_data = []

    #This method is the heart of the class which reads the data
    #Efficiency -> O(n)
    def load_address_data(self):

        with open('./Data/addressCSV.csv', encoding='utf-8-sig') as file:
            reader = csv.reader(file)

            for row in reader:
                self.address_data.append(row)
        return self.address_data
    