"""
This type stub file was generated by pyright.
"""

from ursina import Entity

"""
This type stub file was generated by pyright.
"""
class SpriteSheetAnimation(Entity):
    def __init__(self, texture, animations, tileset_size=..., fps=..., model=..., autoplay=..., **kwargs) -> None:
        ...

    def play_animation(self, animation_name):
        ...



if __name__ == '__main__':
    app = ...
    player_graphics = ...
    def input(key):
        ...

