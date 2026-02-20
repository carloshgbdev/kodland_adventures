# Define uma classe Singleton para armazenar as configurações escolhidas pelo usuário.
class ConfigState:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
        
    def __init__(self):
        self.music = None
        self.audio = True
    
    def set_music(self, music):
        self.music = music
        
    def toggle_audio(self):
        if self.music:
            self.music.set_volume(0 if self.audio else 0.5)
            
        self.audio = not self.audio