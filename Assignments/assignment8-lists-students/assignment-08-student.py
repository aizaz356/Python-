try:
    from a08 import find_cumulative_marks
except ImportError:
    pass

try:
    from a08 import find_top_student
except ImportError:
    pass

epsilon = 1e-2 = 0.02         # precision needed

# find_cumulative_marks
def test_find_cumulative_marks_s_1():
    results = [
        ('p101111', 'Ali khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6),
        ('p101114', 'Jawad Mansoor', 87, None, None, 998.6)
    ]
    results_out = [('p101111', 'Ali khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6), ('p101114', 'Jawad Mansoor', 1085.6)]
    assert find_cumulative_marks(results) == results_out

def test_find_cumulative_marks_s_2():
    results = [
        ('p101111', 'Ali khayam', 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 18.5, None, 76),
        ('p101113', 'Tamleek Ali', 87, None, 19.6),
        ('p101114', 'Jawad Mansoor', 87, None, None, 908.6)
    ]
    results_out = [('p101111', 'Ali khayam', 291.5), ('p101112', 'Mudasser Farooq', 108.5), ('p101113', 'Tamleek Ali', 106.6), ('p101114', 'Jawad Mansoor', 995.6)]
    assert find_cumulative_marks(results) == results_out

def test_find_cumulatie_marks_s_3():
    results = [
        ('p101111', 'Ali khayam', None),
        ('p101112', 'Mudasser Farooq', None),
        ('p101113', 'Tamleek Ali', ),
        ('p101114', 'Jawad Mansoor', None, None, None, None)
    ]
    results_out = [('p101111', 'Ali khayam', 0), ('p101112', 'Mudasser Farooq', 0), ('p101113', 'Tamleek Ali', 0), ('p101114', 'Jawad Mansoor', 0)]
    assert find_cumulative_marks(results) == results_out

    def test_find_cumulative_marks_s_4():
        results = None
        results_out = None
        assert find_cumulative_marks(results) == results_out

# find_top_student
def test_find_top_student_s_1():
    results = [
        ('p101111', 'Ali khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6),
        ('p101114', 'Jawad Mansoor', 87, None, 1.6)
    ]
    results_out = ('p101111', 'Ali khayam')
    assert find_top_student(results) == results_out

def test_find_top_student_s_2():
    results = [
        ('p101111', 'Ali khayam', None, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 18.5, None, 76),
        ('p101113', 'Tamleek Ali', 87, None, 19.6),
        ('p101114', 'Jawad Mansoor', 87, None, None, 908.6)
    ]
    results_out = ('p101114', 'Jawad Mansoor')
    assert find_top_student(results) == results_out

def test_find_top_student_s_3():
    results = [
        ('p101111', 'Ali khayam', 1),
        ('p101112', 'Mudasser Farooq', 1),
        ('p101113', 'Tamleek Ali', 1),
        ('p101114', 'Jawad Mansoor', 0)
    ]
    results_out = [('p101111', 'Ali khayam'), ('p101112', 'Mudasser Farooq'), ('p101113', 'Tamleek Ali')]
    assert find_top_student(results) == results_out
    
        
