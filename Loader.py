import Truck
import Package

class loader:


    def __init__(self):
        self.first_truck = Truck.truck(0, 8.0, 0)
        self.second_truck = Truck.truck(0, 9.17, 0)
        self.third_truck = Truck.truck(0, 11.0, 0)

    #This method loads up the 3 trucks in accordance to the predefined rules
    #Efficiency -> O(n)
    def load_packages(self):

        package_list = Package.load_package_data()

        #Loading first truck
        self.first_truck.load_truck(package_list.search(1))
        self.first_truck.load_truck(package_list.search(13))
        self.first_truck.load_truck(package_list.search(14))
        self.first_truck.load_truck(package_list.search(15))
        self.second_truck.load_truck(package_list.search(19)) 
        self.first_truck.load_truck(package_list.search(16))
        self.first_truck.load_truck(package_list.search(20))
        self.first_truck.load_truck(package_list.search(29))
        self.first_truck.load_truck(package_list.search(30))
        self.first_truck.load_truck(package_list.search(31))
        self.first_truck.load_truck(package_list.search(34))
        self.first_truck.load_truck(package_list.search(37))
        self.first_truck.load_truck(package_list.search(40))


        #Loading second truck
        self.second_truck.load_truck(package_list.search(3))
        self.second_truck.load_truck(package_list.search(6))
        self.second_truck.load_truck(package_list.search(18))
        self.second_truck.load_truck(package_list.search(28))
        self.second_truck.load_truck(package_list.search(32))
        self.second_truck.load_truck(package_list.search(36))
        self.second_truck.load_truck(package_list.search(38)) 
        self.second_truck.load_truck(package_list.search(10)) 
        self.second_truck.load_truck(package_list.search(12)) 
        self.second_truck.load_truck(package_list.search(22)) 
        self.second_truck.load_truck(package_list.search(24)) 
        self.second_truck.load_truck(package_list.search(33)) 
        self.first_truck.load_truck(package_list.search(25))


        #Loading third truck
        self.third_truck.load_truck(package_list.search(2))
        self.third_truck.load_truck(package_list.search(4))
        self.third_truck.load_truck(package_list.search(5))
        self.third_truck.load_truck(package_list.search(7))
        self.third_truck.load_truck(package_list.search(8))
        self.third_truck.load_truck(package_list.search(9))
        self.third_truck.load_truck(package_list.search(11))
        self.third_truck.load_truck(package_list.search(17))
        self.third_truck.load_truck(package_list.search(21))
        self.third_truck.load_truck(package_list.search(23))
        self.third_truck.load_truck(package_list.search(26))
        self.third_truck.load_truck(package_list.search(27))
        self.third_truck.load_truck(package_list.search(35))
        self.third_truck.load_truck(package_list.search(39))

    def get_first_truck(self):
        return self.first_truck
    
    def get_second_truck(self):
        return self.second_truck
    
    def get_third_truck(self):
        return self.third_truck
