"""
This type stub file was generated by pyright.
"""

from ursina import *

"""
This type stub file was generated by pyright.
"""
class Animation(Sprite):
    def __init__(self, name, fps=..., loop=..., autoplay=..., frame_times=..., **kwargs) -> None:
        ...

    def start(self):
        ...

    def pause(self):
        ...

    def resume(self):
        ...

    def finish(self):
        ...

    @property
    def duration(self):
        ...

    def __setattr__(self, name, value):
        ...



if __name__ == '__main__':
    app = ...
    a = ...
