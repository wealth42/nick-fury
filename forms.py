from django import forms
from django.forms.widgets import RadioSelect


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        # print(question.get_answers_list())
        choice_list = [x for x in question.get_answers_list()]
        print(choice_list)
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


