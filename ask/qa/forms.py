from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
#        question.author = 89320
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def __init__(self, *args, **kwargs):                                        
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
