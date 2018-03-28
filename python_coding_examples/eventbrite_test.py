list_of_cities = [
    "Miami",
    "Nashville",
    "Hong Kong",
    "Nashville",
    "Minneapolis",
    "Albuquerque",
    "New York",
    "Miami",
    "Paris",
    # "Minneapolis",
    "Nashville"
]

# Questions I could asked
# * should the function expect only lists?
# * does the orignal list need to remain unchanged? const
# * should the function log any additional data

def count_duplicates(list_of_cities):    
    # initialize count to zero 
    count = 0    
    
    # Create bin of duplicates, so we can identify unique new duplicates
    list_of_dups = []
    
    # Iterate through list, also track index so we can search the reminder of the list
    for i, city in enumerate(list_of_cities):
        # Check if the current city is in the end slice of the list, and is unique
        if city in list_of_cities[i+1:] and city not in list_of_dups:
            # Increment the count to indicate a unique duplicate was found
            count += 1 
            # Place the current unique item in a bin so we don't count it again
            list_of_dups.append(city)
            
    # Print out what dupicates were found for debug
    print("Duplicates found: {}".format(list_of_dups))
    
    return count


if __name__ == '__main__':
    
    count = count_duplicates(list_of_cities)
    
    if count == 2:
        print("Correct {}".format(count))
    else:
        print("No bueno {}".format(count))
