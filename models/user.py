# --- User Class ---
class User:
    def __init__(self, name="", username=""):
        self.name = name
        self.username = username

    def set_user(self, name):
        self.name = name

    def set_username(self, username):
        self.username = username

    def get_user(self):
        return self.name
    
    def get_username(self):
        return self.username