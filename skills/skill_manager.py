class SkillManager:
    def __init__(self):
        self.skills = {}

    def register(self, name: str, skill):
        self.skills[name] = skill

    def get(self, name: str):
        return self.skills.get(name)

    def list_skills(self):
        return list(self.skills.keys())


skills = SkillManager()
