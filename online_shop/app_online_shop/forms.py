from django.forms import ModelForm
from .models import OnlineShop
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
 
class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2')








class AdvertisementForm(ModelForm):
    class Meta:
        model = OnlineShop
        fields = ['title', 'description', 'price', 'auction', 'image']
        if 'title'[0] == '?':
            raise ValidationError("you cannot use the sign: ?")
    
    
    
    
    
    
    # # заданием поле для названия
    # title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    # # задаем поле для описания
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    # # задаем поле для цены
    # price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    # # задаем поле для торга
    # auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    # # задаем поле для изображения
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))