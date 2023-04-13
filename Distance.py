import csv

#Part B - Step 1: With this class I am able to take all of the distance data and convert
#it into a 2 dimensional array that I will be able to use to track distances
class distance:

    def __init__(self):
        self.distance_data = []

    #This method is where the class converts the data into the array
    #Efficiency -> O(n)
    def load_distance_data(self):

        with open('./Data/distanceCSV.csv', encoding='utf-8-sig') as file:
            reader = csv.reader(file)

            for row in reader:
                self.distance_data.append(row)
        return self.distance_data
    
    #This method takes the converted data and then uses an index to check the distance
    #between the different locations and then returns that value.
    #Efficiency -> O(n)
    def distance_between(self, row, col):
        table = self.load_distance_data()
        total = table[row][col]

        if total == '':
            total = table[col][row]
        return total

        

