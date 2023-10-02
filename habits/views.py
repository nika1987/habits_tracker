from django.shortcuts import render
from rest_framework import viewsets, generics

from habits.serializers import HabitSerializer, HabitCreateSerializer

from habits.models import Habit
from users.models import User

'''HABITS generics'''
# ----------------------------------------------------------------


class HabitCreateAPIView(generics.CreateAPIView):
    '''CREATE Habit'''
    serializer_class = HabitCreateSerializer


class HabitListAPIView(generics.ListAPIView):
    '''READ ALL Habits'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    '''READ ONE Habit'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH Habits'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    '''DELETE Habit'''
    queryset = Habit.objects.all()



'''HABITS Public generics'''
# ----------------------------------------------------------------


class PublicHabitListAPIView(generics.ListAPIView):
    '''READ ALL Public Habits'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
