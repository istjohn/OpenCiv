"""
This type stub file was generated by pyright.
"""

from ursina import Entity
from ursina.scripts.property_generator import generate_properties_for_class

"""
This type stub file was generated by pyright.
"""
@generate_properties_for_class()
class Button(Entity):
    default_color = ...
    default_model = ...
    def __init__(self, text=..., parent=..., model=..., radius=..., origin=..., text_origin=..., text_size=..., color=..., collider=..., highlight_scale=..., pressed_scale=..., disabled=..., **kwargs) -> None:
        ...
    
    def text_getter(self):
        ...
    
    def text_setter(self, value):
        ...
    
    def text_origin_getter(self):
        ...
    
    def text_origin_setter(self, value):
        ...
    
    def text_color_getter(self):
        ...
    
    def text_color_setter(self, value):
        ...
    
    def icon_getter(self):
        ...
    
    def icon_setter(self, value):
        ...
    
    def icon_world_scale_getter(self):
        ...
    
    def icon_world_scale_setter(self, value):
        ...
    
    def text_size_getter(self):
        ...
    
    def text_size_setter(self, value):
        ...
    
    def origin_getter(self):
        ...
    
    def origin_setter(self, value):
        ...
    
    def input(self, key):
        ...
    
    def on_mouse_enter(self):
        ...
    
    def on_mouse_exit(self):
        ...
    
    def fit_to_text(self, radius=..., padding=...):
        ...
    


if __name__ == '__main__':
    app = ...
    b = ...
    b = ...
    b = ...
    par = ...
    b = ...
    def input(key):
        ...
    
