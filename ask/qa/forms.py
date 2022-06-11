from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

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


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)        

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user
