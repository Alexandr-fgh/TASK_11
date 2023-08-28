from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm

# Create your models here.

User = get_user_model()

# создаем класс с описание структуры будущей таблицы (наследуемся от класса Model)
class OnlineShop(models.Model):
    # создаем заголовок объявления
    # CharField - класс, обозначающий символьное поле (набор символов), подходит для небольших текстов
    title = models.CharField('Заголовок', max_length=128)
    # создаем описание объявления
    # TextField - класс, обозначающий строковое поле больших размеров
    description = models.TextField('Описание')
    # создаем цену
    # Decimal - дробное число с фиксированной точностью (похоже на float в Python)
    # max_digits - максимальное кол-во цифр в числе
    # decival_places - кол-во знаком после запятой
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    # создаем возможность торгроваться
    # BooleanField - логический тип данных (истина или ложь)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    # создаем дату размещения объявления
    # auto_now_add=True - сразу получаем дату в момент создания объявления
    created_time = models.DateTimeField(auto_now_add=True)
    # создаем дату обновления объявления
    # auto_now=True - получаем дату в момент обновления объявления
    update_time = models.DateTimeField(auto_now=True)
    # поле для создателя объявления (пользователя)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    # поле для изображения
    image = models.ImageField('Изображение', upload_to='online_shop/')
    
    
    
    
    
    
    
    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return 'Нет изо-я'
            
            
    image_img.short_description = 'Изображение'
    image_img.allow_tags = True

    class Meta:
        db_table = "advertisements"

    def __str__(self): 
        return 'id = ' + str(self.id) + "," + "Заголовок = " + self.title + "," + " Цена = "  + str(self.price)