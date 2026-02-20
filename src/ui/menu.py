from pygame import Rect
from src.config.config import WIDTH, HEIGHT, MENU_BG, CIRCLE_NORMAL, TEXT_TITLE, TEXT_BUTTON
from src.config.config_state import ConfigState
from src.game_state import GameState

class Menu:
    def __init__(self):
        self.game_state = GameState.get_instance()
        self.config_state = ConfigState.get_instance()
        
        self.botoes = [
            {
                'btn_pos': (WIDTH // 2, 250),
                'width': 200,
                'height': 50,
                'texto': 'Começar o Jogo',
                'action': None
            },
            {
                'btn_pos': (WIDTH // 2, 250 + 60),
                'width': 200,
                'height': 50,
                'texto': 'Áudio', 
                'action': self._toggle_audio
            },
            {
                'btn_pos': (WIDTH // 2, 250 + 60*2),
                'width': 200,
                'height': 50,
                'texto': 'Saída',
                'action': exit  
            }
        ]

    def draw(self, screen):
        screen.draw.filled_rect(Rect((0, 0), (WIDTH, HEIGHT)), MENU_BG)
        
        screen.draw.text('Kodland Adventures', center=(WIDTH // 2, 120), fontsize=48, color=TEXT_TITLE)
        
        for btn in self.botoes:
            screen.draw.filled_rect(Rect((btn['btn_pos'][0] - btn['width'] // 2, btn['btn_pos'][1] - btn['height'] // 2), (btn['width'], btn['height'])), CIRCLE_NORMAL)
            
            screen.draw.text(btn['texto'], center=btn['btn_pos'], fontsize=24, color=TEXT_BUTTON)

    def handle_click(self, pos):
        for btn in self.botoes:
            cx, cy = btn['btn_pos']
            w = btn['width']
            h = btn['height']
            btn_rect = Rect((cx - w // 2, cy - h // 2), (w, h))
            if btn_rect.collidepoint(pos):
                btn['action']()
                return

    def _toggle_audio(self):
        self.config_state.toggle_audio()