from mathsfunlib import qgenerator as qg
from mathsfunlib.qgenerator import QType
from mathsfunlib.qgenerator import AdditionQuestion
from mathsfunlib.qgenerator import AddSubQuestion
from mathsfunlib.qgenerator import AQGenerator
from mathsfunlib.qgenerator import ASQGenerator


def test_qgenerator_types():
    questions = qg.generate_questions(10, [QType.MULTIPLICATION, QType.DIVISION], [6, 7], None)
    for question in questions:
        qstring = question.get_question()
        assert not set(qstring).isdisjoint(set('x÷'))
        assert qstring.endswith('_')

    questions = qg.generate_questions(20, [QType.MULTIPLICATION], [6, 7], None)
    for question in questions:
        qstring = question.get_question()
        assert set(qstring).isdisjoint(set('÷+-'))
        assert qstring.endswith('_')

    questions = qg.generate_questions(30, [QType.XDIVISION], [6, 7], None)
    for question in questions:
        qstring = question.get_question()
        assert set(qstring).isdisjoint(set('+-'))
        assert not qstring.endswith('_')

    questions = qg.generate_questions(40, [QType.ADDITION], None, '3x3')
    for question in questions:
        qstring = question.get_question()
        assert set(qstring).isdisjoint(set('x÷-'))
        assert qstring.endswith('_')


def test_addition_question():
    addition_question = AdditionQuestion([1, 2, 3])
    assert addition_question.qtype == QType.ADDITION
    assert addition_question.qstring == "1 + 2 + 3 = _"
    assert addition_question.answer == 6


def test_addsub_question():
    addsub_question = AddSubQuestion([1, 2, 3])
    assert addsub_question.qtype == QType.ADDSUB
    assert addsub_question.qstring == "1 + 2 + 3 = _"
    assert addsub_question.answer == 6

    addsub_question = AddSubQuestion([1, -2, 3])
    assert addsub_question.qtype == QType.ADDSUB
    assert addsub_question.qstring == "1 - 2 + 3 = _"
    assert addsub_question.answer == 2

    addsub_question = AddSubQuestion([5, -2, 1])
    assert addsub_question.qtype == QType.ADDSUB
    assert addsub_question.qstring == "5 - 2 + 1 = _"
    assert addsub_question.answer == 4


def test_aquestion_generator():
    d = 5
    r = 5
    qg = AQGenerator(r, d)
    q = qg.get()
    boundary = int(d * '9')
    assert all(
        (0 < n < boundary) for n in q.numbers), f"{q.numbers} not in range {d}d {r}r"
    assert len(q.numbers) <= r, f"Row count is greater than {r}"


def test_asquestion_generator():
    d = 5
    r = 5
    qg = ASQGenerator(r, d)
    q = qg.get()
    boundary = int(d * '9')
    assert all(
        (-boundary < n < boundary) for n in q.numbers), f"{q.numbers} not in range {d}d {r}r"
    assert len(q.numbers) <= r, f"Row count is greater than {r}"

