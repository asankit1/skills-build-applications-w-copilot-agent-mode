from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Marvel", description="Marvel superheroes")
        self.assertEqual(str(team), "Marvel")

    def test_user_creation(self):
        team = Team.objects.create(name="DC", description="DC superheroes")
        user = User.objects.create(name="Batman", email="batman@dc.com", team=team, is_superhero=True)
        self.assertEqual(str(user), "Batman")

    def test_activity_creation(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=team)
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2024-01-01")
        self.assertEqual(str(activity), "Iron Man - Running on 2024-01-01")

    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body workout")
        self.assertEqual(str(workout), "Pushups")

    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Marvel")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), "Marvel - 100 points")
