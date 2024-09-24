# dictionaries.py
# This was really fun and I will treasure this time together with my peers

def demo():
    """
    Demonstrate basic distionary stuff
    """

    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary) 

    # Iterate over the dictionary by key

    for key in myDictionary.keys():
        print(key)

    # Iterate by value

    for item in myDictionary.items():
        print(item)

    # Iterate by value

    for value in myDictionary.values():
        print(value)

    # Add a key/value pair to the dictionary

    myDictionary["Michigan State"] = "Spartans"

    print(len(myDictionary))

    # Cause an expection. Add the try / accept logic to handle
    try:
        print(my.Dictionary["Ohio State"])
    except:
        #we end up here if an expection is thrown in the try block
        print("Ohio State is an invalid key")

    # Remove Xavier by key and print the entire dictionary

    del myDictionary["Xavier"]
    print(myDictionary)
    
    # Create another dictionary called new teams. 
    # Add several key / value pairs
    # Combine that with myDictionary and print the results

    newTeams = {"Ohio State":"Buckeyes", "Indiana":"Hoosiers", "Purdue":"Boilermakers"}
    myDictionary.update(newTeams)
    print(myDictionary)




    