"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
def camel_to_snake(value):
    ...

def snake_to_camel(value):
    ...

def multireplace(string, replacements, ignore_case=...):
    """
    Given a string and a dict, replaces occurrences of the dict keys found in the
    string, with their corresponding values. The replacements will occur in "one pass",
    i.e. there should be no clashes.
    :param str string: string to perform replacements on
    :param dict replacements: replacement dictionary {str_to_find: str_to_replace_with}
    :param bool ignore_case: whether to ignore case when looking for matches
    :rtype: str the replaced string
    """
    ...

def printvar(var):
    ...

def print_info(str, *args):
    ...

def print_warning(str, *args):
    ...

if __name__ == '__main__':
    ...
