def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

def PrintList(the_list):
    for element in the_list:
        print(element)

PrintList(['1', 1, 'the man', "abc"])