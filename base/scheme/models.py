from django.db import models

class Channels(models.Model):
    channel_name = models.CharField(max_length=300, unique=True, verbose_name='Наименование канала')
    object_a = models.CharField(max_length=100, verbose_name='Объект А')
    object_b = models.CharField(max_length=100, verbose_name='Объект Б')
    traffic = models.CharField(max_length=30, verbose_name='Трафик', blank=True)
    description = models.CharField(max_length=3000, verbose_name='Описание', blank=True)
    equipment_connect = models.ManyToManyField ('Equipment', 
                        related_name='equipmentcon', verbose_name='Оборудование')
    class Meta:
            verbose_name = 'Канал'
            verbose_name_plural = 'Каналы'
    def __str__(self):
        return self.channel_name

    def get_absolute_url(self):
        return f'/scheme/{self.id}/channel_detail_view'

class Equipment(models.Model):
    equipment = models.CharField(max_length=100, verbose_name='Оборудование')
    description = models.CharField(max_length=200, verbose_name='Описание', blank=True)
    locations_connect = models.ForeignKey('Locations', on_delete=models.PROTECT,
                        related_name='locationcon', verbose_name='Прохождение по оборудованию') 
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
    def __str__(self):
        return self.equipment
    def get_absolute_url(self):
        return f'/scheme/{self.id}/equipment_detail_view'
        

class Locations(models.Model):
    location = models.CharField(max_length=100, unique=True, verbose_name='Название объекта')
    address = models.CharField(max_length=300, verbose_name='Адрес объекта', blank=True)
    class Meta:
        verbose_name = 'Объекты'
        verbose_name_plural = 'Объекты'
    def __str__(self):
        return self.location
    def get_absolute_url(self):
        return f'/scheme/{self.id}/location_detail_view'

class Specifications(models.Model):
    specification = models.ForeignKey('Equipment',on_delete=models.PROTECT, related_name='specificationcon', blank=True, verbose_name='Спецификация')
    channel_connect = models.ForeignKey('Channels',on_delete=models.PROTECT, related_name='channelcon', null=True, verbose_name='Канал')
    port = models.CharField(max_length=100, verbose_name='Порт')
    timeslot = models.CharField(max_length=100, verbose_name='Таймслот')
    class Meta:
        verbose_name = 'Состав оборудования'
        verbose_name_plural = 'Состав оборудования'
    def __str__(self):
        return self.specification
    def get_absolute_url(self):
        return f'/scheme/{self.id}/specification_detail_view'
    

    