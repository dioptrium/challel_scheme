from django.db import models

class Channels(models.Model):
    channel_name = models.CharField(max_length=300, unique=True, verbose_name='Наименование канала')
    object_a = models.CharField(max_length=100, verbose_name='Объект А')
    object_b = models.CharField(max_length=100, verbose_name='Объект Б')
    traffic = models.CharField(max_length=30, verbose_name='Трафик')
    description = models.CharField(max_length=3000, verbose_name='Описание')
    equipment_connect = models.ManyToManyField ('Equipment', related_name='equipmentcon', verbose_name='Оборудование')
    class Meta:
            verbose_name = 'Канал'
            verbose_name_plural = 'Каналы'
    def __str__(self):
        return self.channel_name

    def get_absolute_url(self):
        return f'/channels/{self.id}'

class Equipment(models.Model):
    equipment = models.CharField(max_length=100, verbose_name='Оборудование')
    description = models.CharField(max_length=200, verbose_name='Описание ')
    locations_connect = models.ForeignKey('Locations', on_delete=models.PROTECT,blank=True, null=True, related_name='locationcon', verbose_name='Прохождение по оборудованию') 
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
    def __str__(self):
        return self.equipment
    def _get_absolute_url(self):
        return f'/channels/{self.id}'

class Locations(models.Model):
    location = models.CharField(max_length=100, unique=True, verbose_name='Название объекта')
    address = models.CharField(max_length=300, verbose_name='Адрес объекта')
    class Meta:
        verbose_name = 'Объекты'
        verbose_name_plural = 'Объекты'
    def __str__(self):
        return self.location
    def get_absolute_url(self):
        return f'/channels/{self.id}'


    