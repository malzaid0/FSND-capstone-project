# Udacity Full Stack Developer Nanodegree: Capstone Project

**Heroku link:** (https://malzaidfsnd.herokuapp.com/)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

To run the server, execute:

```
set FLASK_APP=app.py
flask run --reload
```


## Casting Agency Specifications

The app serves people who want to make a competition in any kind of sports. The database has two tables Club and Players. There's a link between the players and their clubs. In this app you can create clubs and teams to have a clear view in the leagues.

## Models

Clubs with attributes name and league 
Players with attributes name, age, club.id

## Environment Variables

The JWT for each User Role
- coach

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh3czRDOENNSlhBd0dTQ3BDZXh6dyJ9.eyJpc3MiOiJodHRwczovL21hbHphaWQxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjQyNWNhN2ZlNDUyNzAwNmQ5M2I1ZjkiLCJhdWQiOiJjYXBzdG9uZXAiLCJpYXQiOjE1OTg2NzA1MTIsImV4cCI6MTU5ODc1NjkxMiwiYXpwIjoiTFV1MnZKMndqOU1rNDV6YVJta2oybU5LZmNGVWNyaVAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwbGF5ZXJzIl19.F7dBuJ7LlfyN66C_nY4o9PjMrzBEkpP2DPyPeoSVwfUYVCBLwNudiiAjfB3uFbuU4jzRFsZvy2RrnpdbDU9-tbKPhUVhoHA7aHQj7mGABKK5myTZYVfYL7mDGGFQqT7Y2sDzXe49e2rPP4Sz8OU5U3ytILLk-FQFasGBStGUviIu14oaQw3vuadY_sMS4zJI4p7UdNXTSceb01_sW7yCqa7WYxroEjJJl3esSIQ6549eyLDwqe0eM0hZrNTXSyF759iHxnUW1fljjHs47ZjKErRbojfTfKM2digCfJjw0fRg3iIQVCSvgLdniuoJC90-xB-5h_67QJa3VPUwhnzOtg
```

- director

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh3czRDOENNSlhBd0dTQ3BDZXh6dyJ9.eyJpc3MiOiJodHRwczovL21hbHphaWQxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjQyNWQ0YTM4ZDFhMjAwNmQyMWM3NzMiLCJhdWQiOiJjYXBzdG9uZXAiLCJpYXQiOjE1OTg2NzA3NDUsImV4cCI6MTU5ODc1NzE0NSwiYXpwIjoiTFV1MnZKMndqOU1rNDV6YVJta2oybU5LZmNGVWNyaVAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwbGF5ZXJzIiwiZ2V0OnBsYXllcnMiLCJwYXRjaDpwbGF5ZXJzIiwicG9zdDpjbHVicyIsInBvc3Q6cGxheWVycyJdfQ.MXsmwaCX38TQ7XyX1Blu72TLF3Yxx0qpM6R6tMopJUnJedVMjXIlpMtqCY5xQO7S-tA4goF1g0o1IOnKWigiYN9Raipja3PrevmMJexyjVvpX09J_pZGujq0YYTZKB_zHVI58pctmrqqvro-ZFQrclEfn_CpQVuw-Kqd9LTalbhO90fAWtWypcudaPOTzkS-n3Rgnij12yGBrOubQgClnCp8kCY4PtqhB2p9chFgI4NA8eihvRvipKuNcCFbjsRot5c1TY_XmkPnLJiJDWZYlQrQnu-6Lsa_3RtKMf8V9Ea4SEZxyuL67gxEfg7v0UtnpWqo88SkkBS3EhOQkcmOaA
```

## Roles

### no auth
- GET:clubs

###Coach
- GET:players

###Director
- GET:players
- POST:players
- POST:clubs
- PATCH:players
- DELETE:players


## Endpoints


GET `````'/clubs'`````

response
```
{
    "clubs": [
        {
            "id": 2,
            "league": "Laliga",
            "name": "Real Madrid"
        }
    ],
    "success": true
}
```
-------------------------
GET `````'/players'`````

response
```
{
    "players": [
        {
            "age": 33,
            "club": 2,
            "id": 9,
            "name": "Sergio Ramos"
        }
    ],
    "success": true
}
```
-------------------------
GET `````/clubs/<int:actor_id>/players`````

response
```
{
    "players": [
        {
            "age": 33,
            "id": 9,
            "name": "Sergio Ramos"
        }
    ],
    "success": true
}
```
-------------------------
POST `````/clubs`````

sample
```
{
    "name": "Real Madrid",
    "league": "Laliga"
}
```

response
```
{
    "club": {
        "id": 2,
        "league": "Laliga",
        "name": "Real Madrid"
    },
    "success": true
}
```
-------------------------
POST `````'/players'`````

sample
```
{
    "name": "Sergio Ramos",
    "age": 33,
    "club": 2
}
```

response
```
{
    "player": {
        "age": 33,
        "club": 2,
        "id": 9,
        "name": "Sergio Ramos"
    },
    "success": true
}
```
-------------------------
PATCH `````'/players/<int:player_id>'`````

sample
```
{
    "name": "Babi Gomis",
    "age": 34,
    "club": 1
}
```

response
```
{
    "player": {
        "age": 34,
        "club": 1,
        "id": 7,
        "name": "Babi Gomis"
    },
    "success": true
}
```
-------------------------
DELETE `````'/players/<int:player_id>'`````

response
```
{
    "delete": 6,
    "success": true
}
```
## Testing

To run the tests, and run in your terminal

```bash

python test_project.py
```