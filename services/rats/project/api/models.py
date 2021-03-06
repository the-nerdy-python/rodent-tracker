from project import db


class Rat(db.Model):
    __tablename__ = 'rats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(128), nullable=False)
    weight = db.Column(db.Integer(), nullable=False)
    alive = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, color, weight, alive):
        self.color = color
        self.weight = weight
        self.alive = alive

    def to_json(self):
        return {
            'id': self.id,
            'color': self.color,
            'weight': self.weight,
            'alive': self.alive
        }
