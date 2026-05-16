## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR line_count() FUNCTION GOES HERE ###

### END OF MARKER


### YOUR CODE FOR character_count() FUNCTION GOES HERE ###

### END OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###

### END OF MARKER




if __name__ == '__main__':
    print(line_count('.', eassy.txt))
    print(line_count('.', easyy.txt, true))


    print(character_count('.', eassy.txt))
    print(character_count('.', eassy.txt, True))


    move_lines('eassy.txt', 'out.txt', 3)

    pass