try:
    from a10 import line_count
except ImportError:
    pass

try:
    from a10 import character_count
except ImportError:
    pass

try:
    from a10 import move_lines
except ImportError:
    pass


input_file = "dummy file.txt"


def setup_module(module):
    with open(input_file, 'w') as f:
        f.write("""This is a test file and \nhas has some very interesting bits \nOf course, the students never see this file\n so we can put whatever we want to pull in it.\n\nAnd more... """)

# line_count tests

def test_line_count_i_1():
    assert line_count('.', input_file, True) == 5           # '.' means current folder(location of file) and input_file is dummy.txt



def test_line_count_i_2():
    try:
        line_count('.', 'missing.txt', True) == 32
        assert False, "How are you reading a missing file?"     # missing file > show error  
    except IOError:                                             #IOError is the error that is shown when file is missing, IO stands for input output
        pass                                                


# character_count tests

def test_character_count_i_():
    assert character_count('.', input_file) == 161               # This includes: > all leters(a, b, c, ...) > spaces > new lines \n   so, 160 characters in total


def test_character_count_i_2():
    assert character_count('.', input_file, True) == 125         # This includes: > all leters(a, b, c, ...) > spaces > new lines \n   but True means Do special counting(ignore something) and it does not include the spaces and new lines that are at the beginning and end of the file. so, ignore spaces and ignore new lines so, 124 characters in total


# move_lines tests

def test_move_lines_i_1():
    move_lines(input_file, 'out-i.txt', 3)                     # 'out-i.txt is the new file   , 3 means Copy first three lines
    with open('out-i.txt', 'r') as f:                          # open means open  new file and 'r' means read
        assert f.read() == """This is a test file and \nhas has some very interesting bits \nOf course, the students never see this file"""


def test_move_lines_i_2():
    move_lines(input_file, 'out-i.txt', 1)                    # 'out-i.txt is the new file   , 1 means Copy first line
    with open('out-i.txt', 'r') as f:                         # open means open  new file and 'r' means read
        assert f.read() == """This is a test file and"""