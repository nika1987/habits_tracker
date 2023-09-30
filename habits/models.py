from django.db import models
from django.utils import timezone
from users.models import User

# Constants
NULLABLE = {'blank': True, 'null': True}


# Habit

class Habit(models.Model):
    '''Привычка'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cоздатель привычки', **NULLABLE)
    link_nice_habit = models.ForeignKey('self', verbose_name='Связанная привычка', on_delete=models.CASCADE, **NULLABLE,
                                        related_name='habit')

    place = models.CharField(max_length=200, verbose_name='Место привычки')
    time = models.DateTimeField(default=timezone.now, verbose_name='Время привычки')
    action = models.CharField(max_length=250, verbose_name='Действие привычки')
    is_nice_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки', **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=250, verbose_name='Награда', **NULLABLE)
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
