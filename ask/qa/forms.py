from django import forms

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
