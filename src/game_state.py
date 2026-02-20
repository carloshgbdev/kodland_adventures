class GameState:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.in_menu = True
        self.game_over = False
        self.victory = False
        self.current_wave = 0
        self.score = 0