from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import  Task, City,Student


class CustomUserForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2 border-3', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

Choices=[
    ('CreditCard','CreditCard'),
    ('DebitCard','DebitCard'),
    ('PassBook','PassBook')
]
class TaskForm(forms.ModelForm):
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width:50%;height:1.5rem;margin:1rem;'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'style': 'width:50%;height:1.5rem;margin:1rem;','type':'date'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width:50%;height:1.5rem;margin:1rem;','type':'number'}))

    class Meta:
        model = Task
        # fields = "__all__"
        exclude = ('slug',)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'district' in self.data:
            try:
                branch_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(branch_id=branch_id)
                    # .order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.branch.city_set.order_by('name')



    # def post(self):
    #     self.fields['material'] = self.request.POST.getall('mat')

    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     # self.fields['material'].widget = forms.CheckboxSelectMultiple(
    #     #     queryset=Material.objects.all(),
    #     #     widget=forms.CheckboxSelectMultiple,
    #     # )



class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"