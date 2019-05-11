# Greg Henry
# Student ID: 001130918
# Overall space-time complexity for this project is O(29n + C), which is linear, and resolves to O(n)

import csv
import datetime

# Package class
class Package:

    total_miles = 0

    def __init__ (self, num, address, city, state, zip, delivery, weight, special_inst=''):
        self.num = num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery = delivery
        self.weight = weight
        self.special_inst = special_inst
        self.status = "Not delivered"

    # formatted print statement for packages
    def print(self):
        print("%2s %-31s %-18s %3s %6s %-10s %-25s %s" %(self.num, self.address, self.city,
            self.state, self.zip, self.delivery, self.status, self.special_inst))

    # getter functions
    def get_num(self): return self.num
    def get_address(self): return self.address
    def get_city(self): return self.city
    def get_state(self): return self.state
    def get_zip(self): return self.zip
    def get_delivery(self): return self.delivery
    def get_weight(self): return self.weight
    def get_special_inst(self): return self.special_inst
    def get_status(self): return self.status

    # setter or mutator functions
    def set_num(self, num): self.num = num
    def set_address(self, address): self.address = address
    def set_city(self, city): self.city = city
    def set_state(self, state): self.state = state
    def set_zip(self, zip): self.zip = zip
    def set_delivery(self, delivery): self.delivery = delivery
    def set_weight(self, weight): self.weight = weight
    def set_special_inst(self, special_inst): self.special_inst = special_inst
    def set_status(self, status): self.status = status

# function to find distances in the distance table
# Space-time complexity is O(2n), which is linear, and therefore resolves to O(n)
def find_distance(address1, address2):
    row = 0; column = 0
    for i in range(0, len(distance_info)):
        if address1 in distance_info[i][0]:
            row = i
            break
    for i in range(0, len(distance_info)):
        if address2 in distance_info[0][i]:
            column = i
            break
    if row > column:
        Package.total_miles += float(distance_info[row][column])
        return float(distance_info[row][column])
    else:
        Package.total_miles += float(distance_info[column][row])
        return float(distance_info[column][row])

#convert distances to time based on the 18mph truck speeds
def distance_to_time(distance):
    return float(distance * 60/18)

#print the total miles required to deliver all the packages
def print_total_miles():
    print("\nTotal Miles: %2.1f" %Package.total_miles)

# hash table initialization and functions
hash_table = [None] * 40

def hashing_function(key):
    return key % 40

def hash_insert(key, value):
    hash_key = hashing_function(key)
    hash_table[hash_key] = value

def hash_look_up(key):
    return hash_table[key]

# dictionary with wgu address
wgu = {"Address": "4001 South 700 East"}

# read csv file with package information and store in package_info array
# Space-time complexity is O(n), which is linear
package_info = []; temp_package_info = []
with open("WGUPS Package CSV File.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        package_info.append(Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# fill hashtable with Package information
# Space-time complexity is O(n), which is linear
for i in range(1, len(package_info)):
    hash_insert(i, package_info[i])

# read csv file with distances and store in distance_info array
# Space-time complexity is O(n), which is linear
distance_info = []
with open("WGUPS Distance CSV Table Modified.csv") as file:
    reader = csv.reader(file)
    for row in reader: distance_info.append(row)

# initialize trucks and set start time to 8:00 AM (based on minutes)
truck_one = []
truck_one_minutes = 480

truck_two = []
truck_two_minutes = 480

# Guiding principles -- 1. I will determine which packages need to be delivered first based on required delivery
# times; 2. I will deliver packages to the same address at the same time and will wait if a package for the
# same address is delayed; and 3. I will organize delivery routes by zip code to be efficient
#     Truck one starts with package 15 (because delivery is required by 9:00 AM) and others at same zip code 84117
# (except package 26 since 25 is at the same address and is delayed), as well as zip codes
# 84121 (package 22) and 84107 (package 24) in the south-east corner of the map.
#     Packages 13, 14, 15, 16, 19 and 20 must be together on this truck so we will also add 19 and 20 and
# all other packages in zip code 84115 as well as package 13 and all others in zip code 84104
#     There are 16 packages total on truck one
# Space-time complexity is O(6n), which is linear, and therefore resolves to O(n)
truck_one.append(package_info[15])
package_info[15].set_status("En Route Truck One")
for i in range(1, len(package_info)):
    if package_info[i].get_address() == truck_one[0].get_address() and \
            package_info[i].get_status() != "En Route Truck One":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")
for i in range(1, len(package_info)):
    if package_info[i].get_zip() == "84117" and \
            package_info[i].get_num() != "26" and \
            package_info[i].get_special_inst() != "Delayed on flight---will not arrive to depot until 9:05 am" and \
            package_info[i].get_status() != "En Route Truck One":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")
for i in range(1, len(package_info)):
    if package_info[i].get_zip() == "84121" and \
            package_info[i].get_special_inst() != "Delayed on flight---will not arrive to depot until 9:05 am" and \
            package_info[i].get_status() != "En Route Truck One":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")
for i in range(1, len(package_info)):
    if package_info[i].get_zip() == "84107" and \
            package_info[i].get_special_inst() != "Delayed on flight---will not arrive to depot until 9:05 am" and \
            package_info[i].get_status() != "En Route Truck One":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")
for i in range(1, len(package_info)):
    if package_info[i].get_zip() == "84115" and \
            package_info[i].get_special_inst() != "Delayed on flight---will not arrive to depot until 9:05 am" and \
            package_info[i].get_status() != "En Route Truck One":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")
for i in range(1, len(package_info)):
    if package_info[i].get_zip() == "84104" and \
            package_info[i].get_special_inst() != "Delayed on flight---will not arrive to depot until 9:05 am" and \
            package_info[i].get_status() != "En Route Truck One":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")

# Truck two starts by going to zip code 84111 to deliver packages 5, 37, and 38 (package 38 can only be on truck 2),
# then to 84103 (except for package #9 since it has the wrong address), 84105, and finally 84106
# Space-time complexity is O(4n), which is linear, and therefore resolves to O(n)
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84111" and package_info[i].get_status() != "En Route Truck Two":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84103" and package_info[i].get_status() != "En Route Truck Two"\
           and package_info[i].get_num() != "9":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84105" and package_info[i].get_status() != "En Route Truck Two":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84106" and package_info[i].get_status() != "En Route Truck Two":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")

# truck one delivers packages in the order they were loaded until the screenshot at 9:00
# Space-time complexity is O(n), which is linear
truck_one_minutes += distance_to_time(find_distance(wgu["Address"], truck_one[0].get_address()))
truck_one[0].set_status("Truck 1 Delivery " + str(datetime.timedelta(minutes=truck_one_minutes)))
for i in range(0, 7):
    truck_one_minutes += distance_to_time(find_distance(truck_one[i].get_address(), truck_one[i+1].get_address()))
    truck_one[i+1].set_status("Truck 1 Delivery " + str(datetime.timedelta(minutes=truck_one_minutes)))

# truck two delivers packages in the order they were loaded until the screenshot at 9:00
# Space-time complexity is O(n), which is linear
truck_two_minutes += distance_to_time(find_distance(wgu["Address"], truck_two[0].get_address()))
truck_two[0].set_status("Truck 2 Delivery " + str(datetime.timedelta(minutes=truck_two_minutes)))
for i in range(0, len(truck_two)-1):
    truck_two_minutes += distance_to_time(find_distance(truck_two[i].get_address(), truck_two[i+1].get_address()))
    truck_two[i+1].set_status("Truck 2 Delivery " + str(datetime.timedelta(minutes=truck_two_minutes)))

# screen shot at 9:00
# Space-time complexity is O(n), which is linear
print("\nState of packages at 9:00:00\n")
for i in range(0, len(package_info)):
    package_info[i].print()

# truck one deliveries between 9:00 and 10:25
# Space-time complexity is O(n), which is linear
for i in range(7, len(truck_one)-1):
    truck_one_minutes += distance_to_time(find_distance(truck_one[i].get_address(), truck_one[i+1].get_address()))
    truck_one[i+1].set_status("Truck 1 Delivery " + str(datetime.timedelta(minutes=truck_one_minutes)))

# truck one empty, returning to wgu
# Space-time complexity is constant, or O(1)
truck_one_minutes += distance_to_time(find_distance(truck_one[len(truck_one)-1].get_address(),wgu["Address"]))
truck_one = []

# truck two empty, returning to wgu
# Space-time complexity is constant, or O(1)
truck_two_minutes += distance_to_time(find_distance(truck_two[len(truck_two)-1].get_address(),wgu["Address"]))
truck_two = []

#truck two takes packages from delayed plane and delivers to 84117, 84118, 84119, and 84123
# Space-time complexity is O(4n), which is linear, and therefore resolves to O(n)
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84117" and package_info[i].get_status() == "Not delivered":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84118" and package_info[i].get_status() == "Not delivered":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84119" and package_info[i].get_status() == "Not delivered":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")
for i in range(1, len(package_info)):
   if package_info[i].get_zip() == "84123" and package_info[i].get_status() == "Not delivered":
        truck_two.append(package_info[i])
        package_info[i].set_status("En Route Truck Two")

# truck two deliveries between 9:00 and 10:25
# Space-time complexity is O(n), which is linear
truck_two_minutes += distance_to_time(find_distance(wgu["Address"], truck_two[0].get_address()))
truck_two[0].set_status("Truck 2 Delivery " + str(datetime.timedelta(minutes=truck_two_minutes)))
for i in range(0, 8):
    truck_two_minutes += distance_to_time(find_distance(truck_two[i].get_address(), truck_two[i+1].get_address()))
    truck_two[i+1].set_status("Truck 2 Delivery " + str(datetime.timedelta(minutes=truck_two_minutes)))

# update package 9 address at 10:20
# Space-time complexity is constant, or O(1)
package_info[9].set_address("410 S State St")
package_info[9].set_zip("84111")

# screen shot at 10:25
# Space-time complexity is O(n), which is linear
print("\nState of packages at 10:25:00\n")
for i in range(0, len(package_info)):
    package_info[i].print()

# truck one loading and delivering after 10:25
# Space-time complexity is O(2n), which is linear, and therefore resolves to O(n)
for i in range(1, len(package_info)):
   if package_info[i].get_status() == "Not delivered" and package_info[i].get_special_inst() != "Can only be on truck 2":
        truck_one.append(package_info[i])
        package_info[i].set_status("En Route Truck One")
truck_one_minutes += distance_to_time(find_distance(wgu["Address"], truck_one[0].get_address()))
truck_one[0].set_status("Truck 1 Delivery " + str(datetime.timedelta(minutes=truck_one_minutes)))
for i in range(0, len(truck_one)-1):
    truck_one_minutes += distance_to_time(find_distance(truck_one[i].get_address(), truck_one[i+1].get_address()))
    truck_one[i+1].set_status("Truck 1 Delivery " + str(datetime.timedelta(minutes=truck_one_minutes)))

# truck two deliveries after 10:25
# Space-time complexity is O(n), which is linear
for i in range(8, len(truck_two)-1):
    truck_two_minutes += distance_to_time(find_distance(truck_two[i].get_address(), truck_two[i+1].get_address()))
    truck_two[i+1].set_status("Truck 2 Delivery " + str(datetime.timedelta(minutes=truck_two_minutes)))

# screen shot at 12:03
# Space-time complexity is O(n), which is linear
print("\nState of packages at 12:03:00\n")
for i in range(0, len(package_info)):
    package_info[i].print()

# print the total number of miles for the packages to all be delivered
# Space-time complexity is constant, or O(1)
print_total_miles()



