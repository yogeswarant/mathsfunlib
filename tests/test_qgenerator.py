from mathsfunlib import qgenerator as qg
from mathsfunlib.qgenerator import QType
from mathsfunlib.qgenerator import AdditionQuestion
from mathsfunlib.qgenerator import AddSubQuestion


def test_qgenerator_types():
    questions = qg.generate_questions([6, 7], [QType.MULTIPLICATION, QType.DIVISION])
    for question in questions:
        qstring = question.get_question()
        assert not set(qstring).isdisjoint(set('x÷'))
        assert qstring.endswith('_')

    questions = qg.generate_questions([6, 7], [QType.MULTIPLICATION])
    for question in questions:
        qstring = question.get_question()
        assert set(qstring).isdisjoint(set('÷+-'))
        assert qstring.endswith('_')

    questions = qg.generate_questions([6, 7], [QType.XDIVISION])
    for question in questions:
        qstring = question.get_question()
        assert set(qstring).isdisjoint(set('+-'))
        assert not qstring.endswith('_')


def test_addition_question():
    addition_question = AdditionQuestion([1, 2, 3])
    assert addition_question.qtype == QType.ADDITION
    assert addition_question.qstring == "1 + 2 + 3 = "
    assert addition_question.answer == 6


def test_addsub_question():
    addsub_question = AddSubQuestion([1, 2, 3])
    assert addsub_question.qtype == QType.ADDSUB
    assert addsub_question.qstring == "1 + 2 + 3 = "
    assert addsub_question.answer == 6

    addsub_question = AddSubQuestion([1, -2, 3])
    assert addsub_question.qtype == QType.ADDSUB
    assert addsub_question.qstring == "1 - 2 + 3 = "
    assert addsub_question.answer == 2

    addsub_question = AddSubQuestion([5, -2, 1])
    assert addsub_question.qtype == QType.ADDSUB
    assert addsub_question.qstring == "5 - 2 + 1 = "
    assert addsub_question.answer == 4
