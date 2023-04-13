import Addresses
import Distance
import Package

#Part 3: I needed to create a truck object to store packages and to manipulate
#later on
class truck:

    def __init__(self, current_location, time, milage):
        self.current_location = current_location
        self.packages = []
        self.time = time
        self.milage = milage

    def load_truck(self, package):
        self.packages.append(package)

    #Efficiency -> O(n^2)
    def get_closest_destination(self):
            
        #get list of addresses
        obj = Addresses.addresses()
        addresses = obj.load_address_data()    #Efficiency -> O(n)

        #get array of distances
        distances_obj = Distance.distance()

        addy_options = []
        addy_conversions = []
        distances = []

        #Get addresses of all the different packages
        for package in self.packages:
            if package.status != 'Delivered':
                addy_options.append(package.address)

        #Make sure there are multiple packages to still deliver
        if len(addy_options) == 1:
            return addy_options[0]
        
        for option in addy_options:
            for addy in addresses:
                if addy[2] == option:
                    addy_conversions.append(addy[0])
                    break

        for addy in addy_conversions:
            distances.append(distances_obj.distance_between(int(self.current_location), int(addy)))

        best = 0
            
        for i in range(0, len(distances)):
            if float(distances[i]) < float(distances[best]):
                best = i
        return addy_options[best]