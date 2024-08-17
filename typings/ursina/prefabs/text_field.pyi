"""
This type stub file was generated by pyright.
"""

from ursina import Entity

"""
This type stub file was generated by pyright.
"""
class TextField(Entity):
    def __init__(self, max_lines=..., line_height=..., character_limit=..., **kwargs) -> None:
        ...

    @property
    def active(self):
        ...

    @active.setter
    def active(self, value):
        ...

    def add_text(self, s, move_cursor=..., rerender=...):
        ...

    def move_line(self, line_index, delta, move_cursor=...):
        ...

    def erase(self, rerender=...):
        ...

    def delete_selected(self):
        ...

    def get_selected(self):
        ...

    def get_mouse_position_unclamped(self):
        ...

    def get_mouse_position(self):
        ...

    def set_scroll(self, value, render=...):
        ...

    def input(self, key):
        ...

    def move_to_start_of_word(self):
        ...

    def move_to_end_of_word(self):
        ...

    def scroll_to_bottom(self, blank_lines_at_bottom=...):
        ...

    def text_input(self, key):
        ...

    def render(self):
        ...

    def update(self):
        ...

    def select_all(self):
        ...

    def draw_selection(self):
        ...



if __name__ == '__main__':
    app = ...
    te = ...
    def input(key):
        ...

