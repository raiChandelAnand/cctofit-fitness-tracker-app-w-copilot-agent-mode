import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout

# Create test users
def create_users():
    users = []
    for i in range(1, 4):
        username = f"testuser{i}"
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password('testpass')
            user.save()
        users.append(user)
    return users

# Create test teams
def create_teams(users):
    team1, _ = Team.objects.get_or_create(name="Alpha Team")
    team2, _ = Team.objects.get_or_create(name="Beta Team")
    team1.members.set(users[:2])
    team2.members.set(users[1:])
    team1.save()
    team2.save()
    return [team1, team2]

# Create test activities
def create_activities(users):
    for i, user in enumerate(users):
        Activity.objects.create(
            user=user,
            activity_type="Running",
            duration=30 + i * 10,
            distance=5.0 + i,
            calories=300 + i * 50,
            date=date.today() - timedelta(days=i)
        )
        Activity.objects.create(
            user=user,
            activity_type="Cycling",
            duration=45 + i * 5,
            distance=15.0 + i * 2,
            calories=400 + i * 60,
            date=date.today() - timedelta(days=i+1)
        )

# Create test workouts
def create_workouts(users):
    for i, user in enumerate(users):
        Workout.objects.create(
            user=user,
            name=f"Workout {i+1}",
            description="Sample workout description",
            date=date.today() - timedelta(days=i)
        )

def main():
    users = create_users()
    create_teams(users)
    create_activities(users)
    create_workouts(users)
    print("Test data created successfully.")

if __name__ == "__main__":
    main()
