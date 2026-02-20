import pgzrun
from src.config.config_state import ConfigState
from src.game_state import GameState
from src.ui.menu import Menu

menu = Menu()
music.set_volume(0.5)
music.play('background_music')

def draw():
    game_state = GameState.get_instance()
    screen.clear()
    if game_state.in_menu:
        menu.draw(screen)

def on_mouse_down(pos, button):
    print(f"Mouse clicked at {pos} with button {button}")
    game_state = GameState.get_instance()
    if game_state.in_menu:
        menu.handle_click(pos)

def update():
    config_state = ConfigState.get_instance()
    if not config_state.music:
        config_state.set_music(music)
        
    pass

pgzrun.go()