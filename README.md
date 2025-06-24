📺 Late Show API
An API to manage episodes, guests, and appearances on the Late Show.

🔧 Setup Instructions
Requirements
Python 3.8+

PostgreSQL

Pipenv

1. Clone the Repo
git clone <your-github-repo-link>
cd late-show-api-challenge

2. Create .env file
FLASK_APP=server/app.py
FLASK_ENV=development
DATABASE_URL=postgresql://<username>:<password>@localhost/<your_db_name>
JWT_SECRET_KEY=your_jwt_secret_key

3. Install Dependencies
pipenv install
pipenv shell

🚀 Running the App
1. Initialize DB
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

2. Seed Data (Optional)
python seed.py

3. Run the Server
flask run

🔐 Auth Flow
Register
POST /register
{
  "username": "user1",
  "password": "pass123"
}

Login
POST /login
{
  "username": "user1",
  "password": "pass123"
}

Token Usage

Copy access_token from login response

In Postman, go to Authorization tab → Bearer Token → Paste token


📡 Routes Overview
Route	Method	Auth	Description
/register	POST	❌	Register a new user
/login	POST	❌	Log in and get JWT
/episodes	GET	❌	Get all episodes
/episodes/<id>	GET	❌	Get an episode with appearances
/episodes/<id>	DELETE	✅	Delete an episode
/guests	GET	❌	Get all guests
/appearances	POST	✅	Create an appearance


📬 Sample Request (Protected)
Create Appearance
POST /appearances

Headers:
Authorization: Bearer <your_token>
Content-Type: application/json

Body:
{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}

🧪 Postman Usage Guide
Open Postman.

Import challenge-4-lateshow.postman_collection.json.

Register → Login → Copy token.

In “Environment”, set a variable token = your JWT.

Use {{token}} in protected route Authorization headers.

