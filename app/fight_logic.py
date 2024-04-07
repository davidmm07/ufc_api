def calculate_winner(fighter1, fighter2):
    fighter1_skills = set(fighter1.skills.split(','))
    fighter2_weaknesses = set(fighter2.weaknesses.split(','))

    if fighter1_skills.intersection(fighter2_weaknesses):
        return fighter1.id
    else:
        return fighter2.id
