from django.test import TestCase
from qa.models import Question

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(title='title', text='text', rating='1', author=None, likes=None)

    def test(self):
        self.assertEqual(True, True)
