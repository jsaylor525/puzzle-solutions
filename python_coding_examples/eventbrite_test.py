list_of_cities = [
    "Nashville",
    "Nashville",
    "Minneapolis",
    "Albuquerque",
    "New York",
    "Miami",
    "Paris",
    "Minneapolis",
    "Nashville"
]

def count_duplicates(list_of_cities):
    # initialize count to zero 
    count = 0    

    # make a copy of the list so that the original list is not modified
    copy_of_list = list_of_cities[:]
    
    # pop an item out of the list to check if still exists in the list,
    # if so this means we have a duplicate. For the duplicate event we need to 
    # increment the count and remove any further matching duplicates so we don't
    # miscount.
    for city in  copy_of_list:
        copy_of_list.remove(city)

        if city in copy_of_list:
            count += 1
            while city in copy_of_list:                
                copy_of_list.remove(city)
    return count


if __name__ == '__main__':
    
    print(list_of_cities)
    
    count = count_duplicates(list_of_cities)
    
    print(list_of_cities)

    
    if count == 2:
        print("Correct {}".format(count))
    else:
        print("No bueno {}".format(count))
