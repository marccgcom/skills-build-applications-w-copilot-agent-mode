from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        db.users.create_index([("email", 1)], unique=True)

        # Sample data
        users = [
            {"name": "Clark Kent", "email": "clark@dc.com", "team": "DC"},
            {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "DC"},
            {"name": "Diana Prince", "email": "diana@dc.com", "team": "DC"},
            {"name": "Tony Stark", "email": "tony@marvel.com", "team": "Marvel"},
            {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "Marvel"},
            {"name": "Natasha Romanoff", "email": "natasha@marvel.com", "team": "Marvel"},
        ]
        teams = [
            {"name": "Marvel", "members": ["tony@marvel.com", "steve@marvel.com", "natasha@marvel.com"]},
            {"name": "DC", "members": ["clark@dc.com", "bruce@dc.com", "diana@dc.com"]},
        ]
        activities = [
            {"user": "clark@dc.com", "activity": "Running", "duration": 30},
            {"user": "tony@marvel.com", "activity": "Cycling", "duration": 45},
        ]
        leaderboard = [
            {"team": "Marvel", "points": 120},
            {"team": "DC", "points": 110},
        ]
        workouts = [
            {"name": "Super Strength", "suggested_for": "DC"},
            {"name": "Iron Endurance", "suggested_for": "Marvel"},
        ]
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
