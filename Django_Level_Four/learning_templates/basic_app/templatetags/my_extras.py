# how to add custom template tag filters

from django import template

#make a template.Library object called register
register = template.Library()

# #define the custom filter
# def cut(value, arg):
#     """
#     This cuts out all values of arg from the string
#     """
#     return value.replace(arg,'')

# register.filter('cut', cut)

# # This can be done more neatly using decorators.
# # the last line is a function with another function passed as an argument. 
# # instead of having the last line like this, we can say

@register.filter(name='cut') #kwarg format used for clarity
def cut(value, arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

