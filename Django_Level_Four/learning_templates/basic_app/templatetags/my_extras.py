from django import template

# create an object
register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string
    """
    return value.replace(arg,'')

# register the custom filter with django
register.filter('cut',cut)