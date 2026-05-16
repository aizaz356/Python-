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


# line_count tests

def test_line_count_s_1():
    assert line_count('.', 'eassy.txt') == 32                   # count all lines

def test_line_count_s_2():
    assert line_count('.', 'eassy.txt', True) == 20             # count only non-empty lines(ignore empty/blank lines)

def test_line_count_s_3():
    try:
        line_count('.', 'missing.txt') == 32
        assert False, "Hoq are you reading a missing file?"
    except IOError:
        pass

# character_count tests

def test_character_count_s_1():
    assert character_count('.', 'eassy.txt') == 2632                                   # count all chracters, it includes: > all leters(a, b, c, ...) > spaces > new lines \n > punctuation

def test_character_count_s_2():
    assert character_count('.', 'eassy.txt', True) == 2178                             # Ignore spaces and Ignre new lines


# move_line tests

def test_move_lines_s_1():
    move_lines('eassy.txt', 'out.txt', 3)                     # 'out.txt is the new file   , 3 means Copy first three lines
    with open('out.txt', 'r') as f:                          # open means open  new file and 'r' means read
        assert f.read() == """Write a title that summarizes the specific problem\n\nThe title is the first thing potential answerers will see."""


def test_move_lines_s_2():
    move_lines('eassy.txt', 'out.txt', 1)                   # 'out.txt is the new file   , 1 means Copy first line
    with open('out.txt', 'r') as f:                         # open means open  new file and 'r' means read
        assert f.read() == """Write a title that summarizes the specific problem"""