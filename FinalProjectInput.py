"""
Sufiaan Shaikh - 1859029
CIS-2348-18349
Final Project
"""
#Part 1

import csv

import datetime

items = {} # Dictionary to store items
with open('ManufacturerList.csv', 'r') as csv_file: # Manufactur List will be stored in to items dict
    ml_reader = csv.reader(csv_file, delimiter=',')
    for line in ml_reader:
        item_id = line[0]
        items[item_id] = {}
        name = line[1]
        item_type = line[2]
        damaged = line[3]
        items[item_id]['manufacturer'] = name.strip()
        items[item_id]['item_type'] = item_type.strip()
        items[item_id]['damaged'] = damaged

with open('PriceList.csv', 'r') as csv_file: # Arranging data from PriceList.csv to a List
    pl_reader = csv.reader(csv_file, delimiter=',')
    price_list = []
    for line1 in pl_reader:
        price_list.append(line1)
    for line2 in price_list:
        item_id = line2[0]
        amount = line2[1]
        items[item_id]['price'] = amount

with open('ServiceDatesList.csv', 'r') as csv_file: # Putting data of ServiceDateList.csv to item dictionary
    sdl_reader = csv.reader(csv_file, delimiter=',')
    for line in sdl_reader:
        item_id = line[0]
        service_date = line[1]
        items[item_id]['service_date'] = service_date

full_inventory = [] #
with open('FullInventory.csv', 'w') as file:
    full_inventory_write = csv.writer(file)
    temp = []
    for k, v in items.items():
        a = k
        b = (items[k]['manufacturer'])
        c = (items[k]['item_type'])
        d = (items[k]['price'])
        e = (items[k]['service_date'])
        f = (items[k]['damaged'])
        temp = [a, b, c, d, e, f]
        full_inventory.append(temp)

    for i in range(len(full_inventory)): # bubblesort to sort inventory
        for j in range(len(full_inventory)-i-1):
            if full_inventory[j][1] > full_inventory[j + 1][1]:
                temp = full_inventory[j]
                full_inventory[j] = full_inventory[j+1]
                full_inventory[j+1] = temp
    for i in range(len(full_inventory)):
        full_inventory_write.writerow(full_inventory[i])

item_type_list = [] # to sort item types
for k, v in items.items():
    item_type = (items[k]['item_type'])
    item_type_list.append(item_type)
unique_item = [] # storing new unique item to list
for i in item_type_list:
    if i not in unique_item:
        unique_item.append(i)

inventory_list = []
final_list = []
for k, v in items.items():
    a = k
    b = (items[k]['manufacturer'])
    c = (items[k]['price'])
    d = (items[k]['service_date'])
    e = (items[k]['damaged'])
    f = (items[k]['item_type'])
    inventory_list = [a, b, c, d, e, f]
    final_list.append(inventory_list)

for i in range(len(final_list)): # bubblesort
    for j in range(len(final_list) - i - 1):
        if int(final_list[j][0]) > int(final_list[j + 1][0]):
            temp = final_list[j]
            final_list[j] = final_list[j + 1]
            final_list[j + 1] = temp

for i in unique_item:
    inventory_list = []
    with open(str(i) + '_Inventory.csv', 'w') as file:
        write = csv.writer(file)
        Main_list = []
        for j in final_list: # making loop for each unique items
            if j[5] == i:
                a = j[0]
                b = j[1]
                c = j[2]
                d = j[3]
                e = j[4]
                inventory_list = [a, b, c, d, e]
                Main_list.append(inventory_list) # appending all unique items
                write.writerow(inventory_list)

with open('PastServiceDateInventory.csv', 'w') as file: # write a past service date inventory file, sort it using bubble sort and store data to psd_list
    psd_inventory_write = csv.writer(file)

    psd_list = []
    for k, v in items.items():
        e = (items[k]['service_date'])
        first = e.find("/", 0, 3)
        second = e.find("/", 3, 6)

        month = e[0:first]
        day = e[first + 1: second]
        year = e[second + 1:]
        item_date = datetime.date(int(year), int(month), int(day)) # using datetime modue to compare real time date
        current_date = datetime.date.today()
        if item_date < current_date:
            a = k
            b = (items[k]['manufacturer'])
            c = (items[k]['item_type'])
            d = (items[k]['price'])
            f = (items[k]['damaged'])
            past_service_date_il = [a, b, c, d, item_date, f]
            psd_list.append(past_service_date_il)

    for i in range(len(psd_list)):  # bubblesort
        for j in range(len(psd_list) - i - 1):
            if (psd_list[j][4]) > (psd_list[j + 1][4]):
                t = psd_list[j]
                psd_list[j] = psd_list[j + 1]
                psd_list[j + 1] = t

    for i in range(0, len(psd_list)):
        psd_inventory_write.writerow(psd_list[i])

with open('DamagedInventory.csv', 'w') as file: # writing file for damaged item
    damage_write = csv.writer(file)
    damaged_item = [] #to store all damaged item
    for k, v in items.items():
        if items[k]['damaged'] == 'damaged':
            a = k
            b = (items[k]['manufacturer'])
            c = (items[k]['item_type'])
            d = (items[k]['price'])
            e = (items[k]['service_date'])
            temp = [a, b, c, d, e]
            damaged_item.append(temp)

    for i in range(len(damaged_item)):  # bubblesort
        for j in range(len(damaged_item) - i - 1):
            if int(damaged_item[j][3]) < int(damaged_item[j + 1][3]):
                t = damaged_item[j]
                damaged_item[j] = damaged_item[j + 1]
                damaged_item[j + 1] = t

    for i in range(len(damaged_item)):
        damage_write.writerow(damaged_item[i])

csv_file.close()
file.close()

#Part 2 starts from here

item_types = []
manufacturer_list = []

for item in items:
    listed_manufacturer = items[item]['manufacturer']

    listed_type = items[item]['item_type']

    if listed_type not in item_types:
        item_types.append(listed_type)
    if listed_manufacturer not in item_types:
        manufacturer_list.append(listed_manufacturer)


#print(item_types)
#print(manufacturer_list)
#print(items)

user_input = None
while user_input != 'q':
    user_input = input("\n Please enter an item manufacturer and item type or 'q' to quit:\n")

    if user_input == 'q':
        break

    else:
        input_manufacturer = None
        input_types = None
        user_input = user_input.split()

        flag = False
        for word in user_input:
            if word in manufacturer_list:
                if input_manufacturer:
                    flag = True
                else:
                    input_manufacturer = word
                    print(input_manufacturer)
            elif word in item_types:
                if input_types:
                    flag = True
                else:
                    input_types = word
                    print(input_types)

        if not input_manufacturer or not input_types or flag:
            print("No such item in inventory")

        else:
            keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

            asked_item = []  # get the item what user inputs
            similar_item = {}  # to suggest same item with different manufacturer

            for item in keys:
                if items[item]['item_type'] == input_types:
                    current_day = datetime.date.today()
                    service_date = items[item]['service_date']
                    service_expiration = datetime.datetime.strptime(service_date, "%m/%d/%Y").date()
                    expired = service_expiration < current_date

                    if items[item]['manufacturer'] == input_manufacturer:
                        if not expired and not items[item]['damaged']:
                            asked_item.append((item, items[item]))

                    else:
                        if not expired and not items[item]['damaged']:
                            similar_item[item] = items[item]

            if asked_item:
                item = asked_item[0]
                item_id = item[0]
                manufacturer_name = item[1]['manufacturer']
                item_type = item[1]['item_type']
                price = item[1]['price']

                print("Your item is:", item_id,",", manufacturer_name, ",", item_type,",", "$" + price)
                if similar_item:
                    matched_price = price
                    same_item = None
                    nearest_price = None

                    for item in similar_item:
                        if nearest_price is None:
                            same_item = similar_item[item]
                            nearest_price = abs(int(matched_price) - int(similar_item[item]['price']))
                            item_id = item
                            manufacturer_name = similar_item[item]['manufacturer']
                            item_type = similar_item[item]['item_type']
                            price = similar_item[item]['price']
                            continue

                        price_difference = abs(int(matched_price) - int(similar_item[item]['price']))

                        if price_difference < nearest_price:
                            same_item = item
                            nearest_price = price_difference
                            item_id = item
                            manufacturer_name = similar_item[item]['manufacturer']
                            item_type = similar_item[item]['item_type']
                            price = similar_item[item]['price']

                    print("You may, also, consider:", item_id, ",", manufacturer_name, ",", item_type, ",", "$"+price)

            else:
                print("No such item in inventory")

# Try Apple phone, Samsung phone, Lenovo tower, etc. as input
