"""
This type stub file was generated by pyright.
"""

from direct.showbase.ShowBase import ShowBase
from ursina.scripts.singleton_decorator import singleton

"""
This type stub file was generated by pyright.
"""
keyboard_keys = ...
@singleton
class Ursina(ShowBase):
    def __init__(self, title=..., icon=..., borderless=..., fullscreen=..., size=..., forced_aspect_ratio=..., position=..., vsync=..., editor_ui_enabled=..., window_type=..., development_mode=..., render_mode=..., show_ursina_splash=..., **kwargs) -> None:
        """The main class of Ursina. This class is a singleton, so you can only have one instance of it.

        Keyword Args (optional):
            title (str): The title of the window.\n
            fullscreen (bool): Whether the window should be fullscreen or not.\n
            size (tuple(int, int)): The size of the window.\n
            forced_aspect_ratio (bool): Whether the window should have a forced aspect ratio or not.\n
            position (tuple(int, int)): The position of the window.\n
            vsync (bool): Whether the window should have vsync enabled or not.\n
            borderless (bool): Whether the window should be borderless or not.\n
            show_ursina_splash (bool): Whether the Ursina splash should be shown or not.\n
            render_mode (str): The render mode of the window.\n
            development_mode (bool): Whether the development mode should be enabled or not.\n
            editor_ui_enabled (bool): Whether the editor UI should be enabled or not.\n
            window_type (str): The type of the window. Can be 'onscreen', 'offscreen' or 'none'.\n
        """
        ...

    def input_up(self, key, is_raw=...):
        ...

    def input_hold(self, key, is_raw=...):
        ...

    def input(self, key, is_raw=...):
        """Built-in input handler. Propagates the input to all entities and the input function of the main script. Main use case for this it to simulate input though code, like: app.input('a').

        Args:
            key (Any): The input key.
            is_raw (bool, optional): Whether or not the input should be treated as "raw". Defaults to False.
        """
        ...

    def text_input(self, key):
        ...

    def step(self):
        ...

    def run(self, info=...):
        ...



if __name__ == '__main__':
    app = ...
    def input(key):
        ...

