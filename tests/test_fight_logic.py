from app.fight_logic import calculate_winner
from app.models import Fighter

def test_calculate_winner():
    fighter1 = Fighter(name="John", skills="Jiu-Jitsu,Wrestling", weaknesses="Striking")
    fighter2 = Fighter(name="Mike", skills="Striking", weaknesses="Jiu-Jitsu")
    
    winner_id = calculate_winner(fighter1, fighter2)
    assert winner_id == fighter1.id
