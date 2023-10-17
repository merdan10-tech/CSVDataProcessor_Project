# This is a container for all information in the file
database = []

# Opening an attached file 'input.csv', where all data is stored.
used_data = open("input.csv", "r")

# Skipping the header of the file
next(used_data)

# Loop is used to read lines and save that data
for line in used_data.readlines():

    # This is used to remove any spaces or keywords from the list
    line.strip()

    # Removes commas from the line
    linelist = line.split(",")

    # Gets data from list and puts it into a dictionary
    person = {
        "FirstName": linelist[0],
        "MiddleInitial": linelist[1],
        "LastName": linelist[2],
        "Address": linelist[3],
        "City": linelist[4],
        "State": linelist[5],
        "Zip": linelist[6],
        "Box": linelist[7]
    }
    # Converts into float and adds this data into dictionary
    rates = [float(linelist[8]), float(linelist[9]), float(linelist[10])]
    person["Prices"] = rates

    # Adds the value into the dictionary
    database.append(person)

# Loop is used to determine which rate to use in dictionary
for item in database:
    if item["Box"] == "A":
        cost = item["Prices"][0]
    elif item["Box"] == "B":
        cost = item["Prices"][1]
    elif item["Box"] == "C":
        cost = item["Prices"][2]

    #Printining our info from dictionary
    print(item["FirstName"], item["MiddleInitial"], item["LastName"], item["Address"]
      + "\n" + item["City"] + ", " + item["State"], item["Zip"] + "\n" + "$", cost, "\n")



    
    
    
    


