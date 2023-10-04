from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from habits.permissions import IsOwner

from habits.serializers import HabitSerializer, HabitCreateSerializer

from habits.models import Habit
from users.models import User

'''HABITS generics'''
# ----------------------------------------------------------------


class HabitCreateAPIView(generics.CreateAPIView):
    '''CREATE Habit'''
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    '''READ ALL Habits'''
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    '''READ ONE Habit'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    '''UPDATE PUT AND PATCH Habits'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    '''DELETE Habit'''
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]



'''HABITS Public generics'''
# ----------------------------------------------------------------


class PublicHabitListAPIView(generics.ListAPIView):
    '''READ ALL Public Habits'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [AllowAny]
