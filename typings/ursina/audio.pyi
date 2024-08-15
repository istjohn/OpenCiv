"""
This type stub file was generated by pyright.
"""

from ursina.entity import Entity
from ursina.scripts.property_generator import generate_properties_for_class

"""
This type stub file was generated by pyright.
"""
@generate_properties_for_class()
class Audio(Entity):
    volume_multiplier = ...
    def __init__(self, sound_file_name=..., volume=..., pitch=..., balance=..., loop=..., loops=..., autoplay=..., auto_destroy=..., **kwargs) -> None:
        ...
    
    def volume_setter(self, value):
        ...
    
    def pitch_setter(self, value):
        ...
    
    def loop_setter(self, value):
        ...
    
    def loops_setter(self, value):
        ...
    
    def clip_setter(self, value):
        ...
    
    def length_getter(self):
        ...
    
    def status_getter(self):
        ...
    
    def ready_getter(self):
        ...
    
    def playing_getter(self):
        ...
    
    def time_getter(self):
        ...
    
    def time_setter(self, value):
        ...
    
    def balance_setter(self, value):
        ...
    
    def play(self, start=...):
        ...
    
    def pause(self):
        ...
    
    def resume(self):
        ...
    
    def stop(self, destroy=...):
        ...
    
    def fade(self, value, duration=..., delay=..., curve=..., resolution=..., interrupt=...):
        ...
    
    def fade_in(self, value=..., duration=..., delay=..., curve=..., resolution=..., interrupt=..., destroy_on_ended=...):
        ...
    
    def fade_out(self, value=..., duration=..., delay=..., curve=..., resolution=..., interrupt=..., destroy_on_ended=...):
        ...
    


if __name__ == '__main__':
    app = ...
    a = ...
    def input(key):
        ...
    
