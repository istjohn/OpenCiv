"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
def generate_properties_for_class(getter_suffix=..., setter_suffix=..., deleter_suffix=...):
    ...

if __name__ == '__main__':
    class Z:
        ...
    
    
    @generate_properties_for_class(getter_suffix='_getter', setter_suffix='_setter')
    class A:
        ...
    
    
    @generate_properties_for_class()
    class B(A):
        def __init__(self) -> None:
            ...
        
        def x_setter(self, value):
            ...
        
    
    
    e = ...
