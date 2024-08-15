"""
This type stub file was generated by pyright.
"""

from ursina import Entity

"""
This type stub file was generated by pyright.
"""
class ButtonGroup(Entity):
    default_selected_color = ...
    def __init__(self, options, default=..., min_selection=..., max_selection=..., origin=..., spacing=..., **kwargs) -> None:
        ...
    
    @property
    def options(self):
        ...
    
    @options.setter
    def options(self, value):
        ...
    
    @property
    def value(self):
        ...
    
    @value.setter
    def value(self, value):
        ...
    
    def layout(self):
        ...
    
    def input(self, key):
        ...
    
    def select(self, b):
        ...
    
    def on_value_changed(self):
        ...
    


if __name__ == '__main__':
    app = ...
    center = ...
    gender_selection = ...
    def on_value_changed():
        ...
    
