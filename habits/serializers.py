from rest_framework import serializers
from habits.models import Habit
from habits.validators import NiceHabitValidator, IsNiceHabitValidator, TimeHabitValidator, PeriodicityHabitValidator


class PleasureHabitSerializer(serializers.ModelSerializer):
    '''Полезная привычка'''

    class Meta:
        model = Habit
        fields = ('user', 'place', 'time', 'action', 'periodicity', 'time_to_complete', 'is_public', 'link_nice_habit')


class HabitSerializer(serializers.ModelSerializer):
    '''Привычка'''

    pleasant_habit = PleasureHabitSerializer(source='habit', many=True)

    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    '''Создание привычки'''
    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'periodicity', 'is_public', 'time_to_complete', 'link_nice_habit',
                  'is_nice_habit', 'reward',)
        validators = [NiceHabitValidator(fields),
                      IsNiceHabitValidator(fields='link_nice_habit'),
                      TimeHabitValidator(field='time_to_complete'),
                      PeriodicityHabitValidator(field='periodicity')]
