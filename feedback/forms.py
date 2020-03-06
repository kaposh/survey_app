# make sure this is at the top if it isn't already
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class ExampleForm(forms.Form):

    how_did_you_hear = forms.TypedChoiceField(
        label = "How did you hear about the practice?",
        choices = ((0, "Internet"),(1, "Friend "), (3, "Saw your sign"), (4, "Others")),
        widget = forms.RadioSelect,
        required = False,
    )

    years = forms.TypedChoiceField(
        label = "How many years have you been attending this practice?",
        choices = ((0, "Less than 5 years"),(1, "5–10 years  "), (2, "More than 10 years")),
        widget = forms.RadioSelect,
        required = False,
    )

    score = forms.TypedChoiceField(
        label = "Out of 10 the point, how many you would give to this dentist?",
        choices = ((0, "0"),(1, "1 "),(2, "2 "),(3, "3 "),(4, "4 "),(5, "5 "),(6, "6 "),(7, "7 "),(8, "8 "),(9, "9 "),(10, "10 "), ),
        widget = forms.RadioSelect,
        required = False,
    )

    score1 = forms.TypedChoiceField(
        label = "Do you currenly have a dentist that you visit regularly? Would you like to have one?",
        choices = ((0, "Yes"),(1, "No "), (2, "I see my usual dentist regularly")),
        widget = forms.RadioSelect,
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Henry Schein One Survey',
                     'how_did_you_hear',
                     'years',
                     'score',
                     'score1',
                     'notes',
                     ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        self.helper.label_class = 'form_label'
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'


class RegisterForm(forms.Form):

    practice_name = forms.CharField(
        label = "Practice Name",
        required = True,
    )

    practice_id = forms.CharField(
        label = "Practice ID",
        required = True,
    )

    street = forms.CharField(
        label = "Street",
        required = True,
    )

    city = forms.CharField(
        label = "City",
        required = True,
    )

    zip = forms.CharField(
        label = "ZIP",
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Survey Registration',
                     'practice_name',
                     'practice_id',
                     'street',
                     'city',
                     'zip',
                     ),
            ButtonHolder(
                Submit('submit', 'Register', css_class='button white')
            )
        )
        self.helper.label_class = 'form_label'
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'registered'
