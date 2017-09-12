from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    text = forms.CharField(label='Question', widget=forms.Textarea)

    def clean(self):

        cleaned_data = super(AskForm, self).clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if not title:
            self.add_error(title,
                           forms.ValidationError("Field title can't be blank"))

        if not text:
            self.add_error(text,
                           forms.ValidationError("Field text can't be blank"))



    def save(self):

        user = User.objects.get(id=3)
        self.cleaned_data['author'] = user
        self.cleaned_data['added_at'] = datetime.now()
        question = Question(**self.cleaned_data)
        question.save()

        return question


class AnswerForm(forms.Form):
        text = forms.CharField(label='Type your answer', max_length=255)

        def __init__(self, *args, **kwargs):
            self.question = kwargs.get('question')
            super(AnswerForm, self).__init__(*args)

        def save(self):

            user = User.objects.get(id=3)
            self.cleaned_data['author'] = user
            self.cleaned_data['added_at'] = datetime.now()
            self.cleaned_data['question'] = self.question
            answer = Answer(**self.cleaned_data)
            answer.save()

            return answer
