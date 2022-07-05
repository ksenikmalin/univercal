from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    ''' Пользователь '''
    id = models.BigAutoField("Индекс",primary_key=True)
    last_name = models.CharField("Фамилия",max_length=255, default='')
    first_name = models.CharField("Имя",max_length=255)
    middle_name = models.CharField("Отчество",max_length=255)
    email = models.CharField("Почта",max_length=255)
    password = models.CharField("Пароль",max_length=255)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Роль")			
    phone = models.CharField("Телефон",max_length=255)
    date_birth = models.DateField("Дата рождения",default=date.today) 		#date
    created_at = models.DateTimeField("Дата добавления",auto_now=True)		#date    
    
    def __str__(self):
        return self.last_name
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"

class Role(models.Model):
    ''' Роль пользователя '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование",max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Роль"
        verbose_name_plural="Роли"

class Room(models.Model):
    ''' Помещения '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование помещения",max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Помещение"
        verbose_name_plural="Помещения"

class Contract(models.Model):
    ''' Договоры '''
    id = models.BigAutoField("Индекс",primary_key=True)
    date = models.DateField("Дата заключения договора",default=date.today)
    name = models.CharField("Название промышленного предприятия",max_length=255)
    key_product = models.CharField("Регистрационный ключ продукта",max_length=255)
    users_id = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name="Пользователь")
    address = models.CharField("Адрес промышленного предприятия",max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Договор"
        verbose_name_plural="Договоры"

class Manufacturer(models.Model):
    ''' Производитель оборудования '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование системы",max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Производитель оборудования"
        verbose_name_plural="Производители оборудования"

class Type_devices(models.Model):
    ''' Тип оборудования '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование типа оборудования",max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Тип оборудования"
        verbose_name_plural="Типы оборудования"

class System(models.Model):
    ''' Системы '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование системы",max_length=255)
    description = models.TextField("Описание", blank=True)
    photo = models.ImageField("Иконка", upload_to='img/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Система"
        verbose_name_plural="Системы"

class Unit(models.Model):
    ''' Единицы измерения '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование",max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Единица измерения"
        verbose_name_plural="Единицы измерения"

class Equipment(models.Model):
    ''' Оборудование '''
    id = models.BigAutoField("Индекс",primary_key=True)
    name = models.CharField("Наименование",max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Оборудование"
        verbose_name_plural="Оборудование"

class Device(models.Model):
    ''' Устройства '''
    id = models.BigAutoField("Индекс",primary_key=True)
    series = models.CharField("Серийный номер устройства",max_length=255)
    manufacturer_id = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, verbose_name="Производитель оборудования")
    type_devices_id = models.ForeignKey('Type_devices', on_delete=models.CASCADE, verbose_name="Тип устройства ")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Устройство"
        verbose_name_plural="Устройства"

class Installed_devices(models.Model):
    ''' Установленные устройства '''
    id = models.BigAutoField("Индекс",primary_key=True)
    systems = models.ForeignKey('System', on_delete=models.CASCADE, verbose_name="Система")
    room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name="Помещение")
    devices = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name="Устройство")
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, verbose_name="Оборудование")
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, verbose_name="Единица измерения")
    value = models.CharField("Значение устройства",max_length=255)
    limit_max = models.CharField("Максимальное значение устройства ",max_length=255)
    limit_min = models.CharField("Минимальное значение устройства",max_length=255)
    
    def __str__(self):
        return self.devices_id
    
    class Meta:
        verbose_name="Установленное устройство"
        verbose_name_plural="Установленные устройства"

class Error(models.Model):
    ''' Ошибки '''
    id = models.BigAutoField("Индекс",primary_key=True)
    created_at = models.DateField("Дата и время возникновения ошибки",default=date.today)
    description = models.CharField("Описание ошибки",max_length=255)
    installed_devices_id = models.ForeignKey('Installed_devices', on_delete=models.PROTECT, verbose_name="Устройство")
    
    def __str__(self):
        return self.devices_id
    
    class Meta:
        verbose_name="Ошибка"
        verbose_name_plural="Ошибки"

class Event(models.Model):
    ''' События '''
    id = models.BigAutoField("Индекс",primary_key=True)
    installed_devices_id = models.ForeignKey('Installed_devices', on_delete=models.PROTECT, verbose_name="Устройство")
    date = models.DateField("Дата и время момента фиксации показания",default=date.today)
    status = models.CharField("Состояние устройства (On/Off)",max_length=3)
    meaning = models.PositiveIntegerField(null=True, blank=True)    
    
    def __str__(self):
        return self.devices_id
    
    class Meta:
        verbose_name="Событие"
        verbose_name_plural="События"


