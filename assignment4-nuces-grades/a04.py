## IMPORTS GO HERE 

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 78:
        return  'B'
    elif marks >= 66:
        return 'C'
    elif marks >= 54:
        return 'D'
    else:
        return 'F'
#### END OF MARKER ####

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(*grades):
    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    total = 0
    for g in grades:
        if g not in grade_points:
            return "Invalid grade: {}".format(g)
        total += grade_points[g]

    return total / len(grades)
#### END OF MARKER ####

if __name__ == '__main__':
    print(get_grade(50))
    print(calculate_sgpa('A', 'B', 'nothing'))
