import Loader
import Addresses
import Distance
import math
import Hash_Table

class deliver:

    def __init__(self):
        pass

    #This method is the core componenet of this application. It loads the truck and then
    #delivers the packages based on the restrictions.
    #Efficiency -> O(n^4)
    def truck_one_deliver_packages(self):
        
        loader = Loader.loader()
        obj = Addresses.addresses()
        addresses = obj.load_address_data()    #Efficiency -> O(n)
        checker = Distance.distance()   

        loader.load_packages()                 #Efficiency -> O(n)
        first_truck = loader.get_first_truck() #Efficiency -> O(1)

        #Update the time departed for each package
        for package in first_truck.packages:
            package.time_departed = first_truck.time

        for i in range(0, len(first_truck.packages)):

            #Check to make sure that there is more than a single package in the truck
            count = 0
            for package in first_truck.packages:
                if package.status != 'Delivered':
                    count = count + 1
            if count == 1:
                for package in first_truck.packages:
                    if package.status != 'Delivered':
                        for addy in addresses:
                            if addy[2] == package.address:

                                #Get distance
                                distance = 0
                                distance = checker.distance_between(int(addy[0]), int(first_truck.current_location))
                                deliver_time = (float(distance) / 18)

                                #Update truck time
                                first_truck.time = first_truck.time + float(deliver_time)


                                #Update the trucks milage
                                first_truck.milage = first_truck.milage + float(distance)


                                #Update truck location and package status
                                first_truck.current_location = addy[0]
                                package.status = 'Delivered'
                                package.time_delivered = first_truck.time
                                return first_truck

            #First we need to get the address of the next closest location
            best_address = first_truck.get_closest_destination()  #Efficiency -> O(n^2)
            
            #Then we need to figure out which index that location is so we can judge the distance
            #and also set our new truck destination
            location = 0
            for addy in addresses:
                if addy[2] == best_address:
                    location = addy[0]
                    break

            #Get distance
            distance = 0
            distance = checker.distance_between(int(location), int(first_truck.current_location))
            deliver_time = (float(distance) / 18)

            #Update truck time
            first_truck.time = first_truck.time + float(deliver_time)


            #Update the trucks milage
            first_truck.milage = first_truck.milage + float(distance)



            #update the status of the target package        
            for package in first_truck.packages:
                if package.address == best_address:
                    package.status = 'Delivered'
                    package.time_delivered = first_truck.time
            
            #Update the trucks current position
            first_truck.current_location = location
            
        return first_truck



    #This method is the core componenet of this application. It loads the truck and then
    #delivers the packages based on the restrictions.
    #Efficiency -> O(n^4)
    def truck_two_deliver_packages(self):
        
        loader = Loader.loader()
        obj = Addresses.addresses()
        addresses = obj.load_address_data()
        checker = Distance.distance()

        loader.load_packages()
        second_truck = loader.get_second_truck()

        #Update the time departed for each package
        for package in second_truck.packages:
            package.time_departed = second_truck.time

        for i in range(0, len(second_truck.packages)):

            #Check to make sure that there is more than a single package in the truck
            count = 0
            for package in second_truck.packages:
                if package.status != 'Delivered':
                    count = count + 1
            if count == 1:
                for package in second_truck.packages:
                    if package.status != 'Delivered':
                        for addy in addresses:
                            if addy[2] == package.address:
                                
                                #Get distance
                                distance = 0
                                distance = checker.distance_between(int(addy[0]), int(second_truck.current_location))
                                deliver_time = (float(distance) / 18)

                                #Update truck time
                                second_truck.time = second_truck.time + float(deliver_time)


                                #Update the trucks milage
                                second_truck.milage = second_truck.milage + float(distance)


                                #Update truck location and package status
                                second_truck.current_location = addy[0]
                                package.status = 'Delivered'
                                package.time_delivered = second_truck.time
                                return second_truck

            #First we need to get the address of the next closest location
            best_address = second_truck.get_closest_destination()
            
            #Then we need to figure out which index that location is so we can judge the distance
            #and also set our new truck destination
            location = 0
            for addy in addresses:
                if addy[2] == best_address:
                    location = addy[0]
                    break

            #Get distance
            distance = 0
            distance = checker.distance_between(int(location), int(second_truck.current_location))
            deliver_time = (float(distance) / 18)

            #Update truck time
            second_truck.time = second_truck.time + float(deliver_time)


            #Update the trucks milage
            second_truck.milage = second_truck.milage + float(distance)



            #update the status of the target package        
            for package in second_truck.packages:
                if package.address == best_address:
                    package.status = 'Delivered'
                    package.time_delivered = second_truck.time
            
            #Update the trucks current position
            second_truck.current_location = location
        
        return second_truck
    


    #This method is the core componenet of this application. It loads the truck and then
    #delivers the packages based on the restrictions.
    #Efficiency -> O(n^4)
    def truck_three_deliver_packages(self):
        
        loader = Loader.loader()
        obj = Addresses.addresses()
        addresses = obj.load_address_data()
        checker = Distance.distance()

        loader.load_packages()
        third_truck = loader.get_third_truck()

        #Update the time departed for each package
        for package in third_truck.packages:
            package.time_departed = third_truck.time

        for i in range(0, len(third_truck.packages)):

            #Check to make sure that there is more than a single package in the truck
            count = 0
            for package in third_truck.packages:
                if package.status != 'Delivered':
                    count = count + 1
            if count == 1:
                for package in third_truck.packages:
                    if package.status != 'Delivered':
                        for addy in addresses:
                            if addy[2] == package.address:
                                
                                #Get distance
                                distance = 0
                                distance = checker.distance_between(int(addy[0]), int(third_truck.current_location))
                                deliver_time = (float(distance) / 18)

                                #Update truck time
                                third_truck.time = third_truck.time + float(deliver_time)


                                #Update the trucks milage
                                third_truck.milage = third_truck.milage + float(distance)

                                #Update truck location and package status
                                third_truck.current_location = addy[0]
                                package.status = 'Delivered'
                                package.time_delivered = third_truck.time
                                return third_truck

            #First we need to get the address of the next closest location
            best_address = third_truck.get_closest_destination()
            
            #Then we need to figure out which index that location is so we can judge the distance
            #and also set our new truck destination
            location = 0
            for addy in addresses:
                if addy[2] == best_address:
                    location = addy[0]
                    break

            #Get distance
            distance = 0
            distance = checker.distance_between(int(location), int(third_truck.current_location))
            deliver_time = (float(distance) / 18)

            #Update truck time
            third_truck.time = third_truck.time + float(deliver_time)


            #Update the trucks milage
            third_truck.milage = third_truck.milage + float(distance)



            #update the status of the target package        
            for package in third_truck.packages:
                if package.address == best_address:
                    package.status = 'Delivered'
                    package.time_delivered = third_truck.time
            
            #Update the trucks current position
            third_truck.current_location = location
        
        
    #This method is used after all of the trucks have driven their routes and recorded
    #the time it took and each individual package delivery time. This re-adds all the 
    #packages back into a dictionary so that I can manipulate their data for the CLI
    #Efficiency -> O(n^4)
    def store_delivered_packages(self):

        truck_one = self.truck_one_deliver_packages()      #Efficiency -> O(n^4)
        truck_two = self.truck_two_deliver_packages()      #Efficiency -> O(n^4)
        truck_three = self.truck_three_deliver_packages()  #Efficiency -> O(n^4)


        map = Hash_Table.hash_table()

        for package in truck_one.packages:
            map.add(package.id, package)
        for package in truck_two.packages:
            map.add(package.id, package)
        for package in truck_three.packages:
            map.add(package.id, package)

        map.add('truck_one', truck_one)
        map.add('truck_two', truck_two)
        map.add('truck_three', truck_three)
        return map


        