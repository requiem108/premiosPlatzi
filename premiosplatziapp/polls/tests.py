import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from .models import Question

# Create your tests here.
class QuestionModelTest(TestCase):
    def test_was_published_future(self):
       time = timezone.now() + datetime.timedelta(days=30)
       future_question = Question(question_text="¿Quien es el mejor course Director de Platzi?",pub_date=time)
       self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_past(self):
       time = timezone.now() - datetime.timedelta(hours=23)
       past_question = Question(question_text="¿Quien es el mejor course Director de Platzi?",pub_date=time)
       self.assertIs(past_question.was_published_recently(),True)

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        #si no existen preguntas, muestra un mensaje apropiado
        """If no question exist, an appropuate message is displayed """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        