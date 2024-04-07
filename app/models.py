from app import db

class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(200), nullable=False)
    weaknesses = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Fighter('{self.name}')"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "skills": self.skills,
            "weaknesses": self.weaknesses
        }

class Fight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fighter1_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=False)
    fighter2_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=True)
    loser_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=True)

    def __repr__(self):
        return f"Fight('{self.fighter1_id}', '{self.fighter2_id}')"
