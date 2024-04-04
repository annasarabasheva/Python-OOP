class ExercisePlan:
    id = 1

    def __init__(self, trainer_id, equipment_id, duraton):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duraton
        self.id = ExercisePlan.id
        ExercisePlan.id += 1

    @classmethod
    def from_hours(cls, trainer_id:int, equipment_id:int, hours:int):
        in_minutes = hours * 60
        return cls(trainer_id, equipment_id, in_minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"