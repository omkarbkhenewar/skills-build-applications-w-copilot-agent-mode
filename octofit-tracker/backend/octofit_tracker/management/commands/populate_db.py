from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users (super heroes)
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', type='Running', duration=30),
            Activity(user='Captain America', type='Cycling', duration=45),
            Activity(user='Spider-Man', type='Swimming', duration=25),
            Activity(user='Batman', type='Running', duration=40),
            Activity(user='Superman', type='Cycling', duration=50),
            Activity(user='Wonder Woman', type='Swimming', duration=35),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        leaderboard = [
            Leaderboard(user='Iron Man', points=100),
            Leaderboard(user='Captain America', points=90),
            Leaderboard(user='Spider-Man', points=80),
            Leaderboard(user='Batman', points=95),
            Leaderboard(user='Superman', points=85),
            Leaderboard(user='Wonder Woman', points=75),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Workouts
        workouts = [
            Workout(name='Full Body Blast', description='A superhero-level full body workout.'),
            Workout(name='Speed Run', description='Run like the Flash!'),
            Workout(name='Strength Training', description='Build strength like Superman.'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
