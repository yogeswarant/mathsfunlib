from mathsfunlib import qgenerator as qg
from mathsfunlib.qgenerator import QType


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
