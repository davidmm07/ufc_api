import json
from app.fight_logic import calculate_winner
from app.models import Fighter, Fight
from app import db

def test_get_fighters(client):
    response = client.get('/fighters')
    assert response.status_code == 200
    assert b'[]' in response.data

def test_add_fighter(client):
    data = {
        "name": "John",
        "skills": "Jiu-Jitsu,Wrestling",
        "weaknesses": "Striking"
    }
    response = client.post('/fighters', json=data)
    assert response.status_code == 201

def test_add_fight(client):
    fighter1 = {
        "name": "John",
        "skills": "Jiu-Jitsu,Wrestling",
        "weaknesses": "Striking"
    }
    fighter2 = {
        "name": "Mike",
        "skills": "Striking",
        "weaknesses": "Jiu-Jitsu"
    }

    response = client.post('/fighters', json=fighter1)
    assert response.status_code == 201
    response = client.post('/fighters', json=fighter2)
    assert response.status_code == 201

    data = {
        "fighter1_id": 1,
        "fighter2_id": 2
    }
    response = client.post('/fights', json=data)
    assert response.status_code == 201


def test_get_fight_winner(client):
    # Add a new fight
    fighter1 = Fighter(name="John", skills="Jiu-Jitsu,Wrestling", weaknesses="Striking")
    fighter2 = Fighter(name="Mike", skills="Striking", weaknesses="Jiu-Jitsu")
    
    db.session.add(fighter1)
    db.session.add(fighter2)
    db.session.commit()

    winner_id = calculate_winner(fighter1, fighter2)
    
    fight = Fight(fighter1_id=fighter1.id, fighter2_id=fighter2.id, winner_id=winner_id)
    
    db.session.add(fight)
    db.session.commit()

    response = client.get(f'/fights/{fight.id}/winner')
    data = json.loads(response.data.decode())

    if not fight.winner_id:
        assert response.status_code == 200
        assert data["message"] == "It's a tie!"
    else:
        assert response.status_code == 200
        assert data["name"] == (fighter1.name if winner_id == fighter1.id else fighter2.name)

def test_fight_tie(client):
    # Add a new fight with a tie
    fighter1 = Fighter(name="John", skills="Jiu-Jitsu", weaknesses="Striking")
    fighter2 = Fighter(name="Mike", skills="Striking", weaknesses="Jiu-Jitsu")
    
    db.session.add(fighter1)
    db.session.add(fighter2)
    db.session.commit()

    fight = Fight(fighter1_id=fighter1.id, fighter2_id=fighter2.id)
    
    db.session.add(fight)
    db.session.commit()

    response = client.get(f'/fights/{fight.id}/winner')
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert data["message"] == "It's a tie!"