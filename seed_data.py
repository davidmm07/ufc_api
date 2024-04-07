from app.models import Fighter, Fight
from app import db
from app.routes import calculate_winner  # Import calculate_winner from routes to use it here

def seed_data():
    fighter1 = Fighter(name="John", skills="Jiu-Jitsu,Wrestling", weaknesses="Striking")
    fighter2 = Fighter(name="Mike", skills="Striking", weaknesses="Jiu-Jitsu")
    
    db.session.add(fighter1)
    db.session.add(fighter2)
    db.session.commit()

    winner_id = calculate_winner(fighter1, fighter2)
    
    fight = Fight(fighter1_id=fighter1.id, fighter2_id=fighter2.id, winner_id=winner_id)
    
    db.session.add(fight)
    db.session.commit()

if __name__ == '__main__':
    seed_data()
