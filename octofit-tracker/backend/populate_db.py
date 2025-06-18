import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Insert test users
db.users.insert_many([
    {"email": "alice@example.com", "name": "Alice", "password": "pass1"},
    {"email": "bob@example.com", "name": "Bob", "password": "pass2"},
    {"email": "carol@example.com", "name": "Carol", "password": "pass3"}
])

# Insert test teams
team1_id = db.teams.insert_one({"name": "Team Alpha", "members": []}).inserted_id
team2_id = db.teams.insert_one({"name": "Team Beta", "members": []}).inserted_id

# Insert test activities
user1 = db.users.find_one({"email": "alice@example.com"})
user2 = db.users.find_one({"email": "bob@example.com"})
db.activity.insert_many([
    {"user": user1["_id"], "activity_type": "run", "duration": 30, "date": datetime(2025, 6, 18)},
    {"user": user2["_id"], "activity_type": "walk", "duration": 45, "date": datetime(2025, 6, 17)}
])

# Insert test leaderboard
leaderboard1 = {"team": team1_id, "points": 100}
leaderboard2 = {"team": team2_id, "points": 80}
db.leaderboard.insert_many([leaderboard1, leaderboard2])

# Insert test workouts
db.workouts.insert_many([
    {"user": user1["_id"], "workout_type": "cardio", "details": "30 min run", "date": datetime(2025, 6, 18)},
    {"user": user2["_id"], "workout_type": "strength", "details": "45 min weights", "date": datetime(2025, 6, 17)}
])

print("Test data inserted into octofit_db.")
