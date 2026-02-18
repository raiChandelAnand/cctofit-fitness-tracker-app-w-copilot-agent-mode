from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout
from datetime import date

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='member', password='pass')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='activityuser', password='pass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, date=date.today())
        self.assertEqual(activity.activity_type, 'Run')
        self.assertEqual(activity.user, user)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username='workoutuser', password='pass')
        workout = Workout.objects.create(user=user, name='Morning Routine', date=date.today())
        self.assertEqual(workout.name, 'Morning Routine')
        self.assertEqual(workout.user, user)
