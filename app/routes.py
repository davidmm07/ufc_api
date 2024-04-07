from flask import Blueprint, request, jsonify
from app.fight_logic import calculate_winner
from app.models import Fighter, Fight
from app import db

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/fighters', methods=['GET'])
def get_fighters():
    fighters = Fighter.query.all()
    return jsonify([fighter.to_dict() for fighter in fighters])

@main_blueprint.route('/fighters/<int:fighter_id>', methods=['GET'])
def get_fighter(fighter_id):
    fighter = Fighter.query.get(ident=fighter_id)
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404
    return jsonify(fighter.to_dict())

@main_blueprint.route('/fighters', methods=['POST'])
def add_fighter():
    data = request.get_json()
    fighter = Fighter(name=data['name'], skills=data['skills'], weaknesses=data['weaknesses'])
    db.session.add(fighter)
    db.session.commit()
    return jsonify({"message": "Fighter added successfully"}), 201

@main_blueprint.route('/fights', methods=['POST'])
def add_fight():
    data = request.get_json()
    fighter1 = Fighter.query.get(data['fighter1_id'])
    fighter2 = Fighter.query.get(data['fighter2_id'])

    if not fighter1 or not fighter2:
        return jsonify({"error": "Fighters not found"}), 404

    winner_id = calculate_winner(fighter1, fighter2)

    fight = Fight(fighter1_id=data['fighter1_id'], fighter2_id=data['fighter2_id'], winner_id=winner_id)
    
    db.session.add(fight)
    db.session.commit()
    return jsonify({"message": "Fight added successfully"}), 201


@main_blueprint.route('/fights/<int:fight_id>/winner', methods=['GET'])
def get_fight_winner(fight_id):
    fight = Fight.query.get(fight_id)
    if not fight:
        return jsonify({"error": "Fight not found"}), 404

    if not fight.winner_id:
        return jsonify({"message": "It's a tie!"})

    winner = Fighter.query.get(fight.winner_id)
    return jsonify(winner.to_dict())