from colorama import Fore
import Deliver
import math


#This is the class that wraps everying up and delivers the final results to the user
class cli:

    def __init__(self):
        pass
    
    #This method delivers all of the delivery data about the packages to the user
    #Efficiency -> O(n^4)
    def get_all(self):
        start = Deliver.deliver()
        container = start.store_delivered_packages()   #Efficiency -> O(n^4)

        for i in range(1, 41):
            hours = math.floor(float(container.search(i).time_delivered))
            minutes = math.ceil((float(container.search(i).time_delivered) * 60) % 60)
            if minutes < 10:
                minutes = '0' + str(minutes)
            print('Package ID: ' + str(i) + ', Address: ' + container.search(i).address + ', Delivered at: ' + str(hours) + ":" + str(minutes))
        print("First truck milage: " + str(container.search('truck_one').milage))
        print("Second truck milage: " + str(container.search('truck_two').milage))
        print("Third truck milage: " + str(container.search('truck_three').milage))


    #This method is used to check a specific delivery time of a package against an inputed
    #time
    #Efficiency -> O(n^4)
    def check_package(self, id, time):
        start = Deliver.deliver()
        container = start.store_delivered_packages()    #Efficiency -> O(n^4)

        package = container.search(int(id))

        #Need to conver the inputed time into a fraction of hours
        hour = ''
        minutes =  ''
        switch = 0
        for char in time:
            if char == ':':
                switch = 1
                continue
            if switch == 0:
                hour = hour + str(char)
            if switch == 1:
                minutes = minutes + str(char)
        minutes = int(minutes) / 60
        updated_minutes = ''
        for char in str(minutes):
            if char == '.':
                switch = 0
                continue
            if switch == 0:
                updated_minutes = updated_minutes + str(char)
        hours = str(hour) + '.' + str(updated_minutes)
    
            

        if float(hours) < package.time_departed:
            print('At ' + str(time) + ' the package was at the hub.')
            return

        if float(hours) > package.time_departed and float(hours) < package.time_delivered:
            print('At ' + str(time) + ' the package was in route.')
            return

        if float(hours) > package.time_delivered:
            print('At ' + str(time) + " the package was at it's destination.")
            return
    
    #This method returns the status of all the packages based on a specific time
    #Efficiency -> O(n^4)
    def get_all_time(self, time):

        start = Deliver.deliver()
        container = start.store_delivered_packages()    #Efficiency -> O(n^4)

        #Need to conver the inputed time into a fraction of hours
        hour = ''
        minutes =  ''
        switch = 0
        for char in time:
            if char == ':':
                switch = 1
                continue
            if switch == 0:
                hour = hour + str(char)
            if switch == 1:
                minutes = minutes + str(char)
        minutes = int(minutes) / 60
        updated_minutes = ''
        for char in str(minutes):
            if char == '.':
                switch = 0
                continue
            if switch == 0:
                updated_minutes = updated_minutes + str(char)
        hours = str(hour) + '.' + str(updated_minutes)

        for i in range(1, 41):
            package = container.search(i)

            if float(hours) < package.time_departed:
                print('Package ID: ' + str(package.id) + ', Address: ' + package.address + ', At hub')
                continue

            if float(hours) > package.time_departed and float(hours) < package.time_delivered:
                print('Package ID: ' + str(package.id) + ', Address: ' + package.address + ', In route')
                continue

            if float(hours) > package.time_delivered:
                print('Package ID: ' + str(package.id) + ', Address: ' + package.address + ', Delivered')
                continue
    
    #This method is the enterance to the entire program and specifies the enterance to the user
    #Efficiency -> O(n^4)
    def run_program(self):
        exit = 0
        while exit == 0:
            print(Fore.CYAN + '*' * 50)
            print(Fore.CYAN + '1. Print All Package Status and Total Mileage')
            print(Fore.CYAN + '2. Get a Single Package Status with a Time')
            print(Fore.CYAN + '3. Get All Package Status with a Time')
            print(Fore.CYAN + '4. Exit Program')
            print(' ')
            pick = input(Fore.YELLOW + 'Input Desired Option Number >>>')

            if pick == '1':
                self.get_all()
                continue

            if pick == '2':
                pick_id = input(Fore.YELLOW + 'Input package ID (1-40) >>>')
                pick_time = input(Fore.YELLOW + 'Input time in the format of HH:MM >>>')
                print(' ')
                self.check_package(pick_id, pick_time)
                continue

            if pick == '3':
                pick_time = input(Fore.YELLOW + 'Input time in the format of HH:MM >>>')
                self.get_all_time(pick_time)
                continue

            if pick == '4':
                exit = 1
                continue