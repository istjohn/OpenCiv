"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
class Mouse:
    def __init__(self) -> None:
        ...
    
    @property
    def x(self):
        ...
    
    @x.setter
    def x(self, value):
        ...
    
    @property
    def y(self):
        ...
    
    @y.setter
    def y(self, value):
        ...
    
    @property
    def position(self):
        ...
    
    @position.setter
    def position(self, value):
        ...
    
    @property
    def locked(self):
        ...
    
    @locked.setter
    def locked(self, value):
        ...
    
    @property
    def visible(self):
        ...
    
    @visible.setter
    def visible(self, value):
        ...
    
    def input(self, key):
        ...
    
    def update(self):
        ...
    
    @property
    def normal(self):
        ...
    
    @property
    def world_normal(self):
        ...
    
    @property
    def point(self):
        ...
    
    @property
    def world_point(self):
        ...
    
    @property
    def is_outside(self):
        ...
    
    def find_collision(self):
        ...
    
    def unhover_everything_not_hit(self):
        ...
    


instance = ...
if __name__ == '__main__':
    app = ...
    def input(key):
        ...
    
