# Firstly How we can comment statements in Python
# With '#' (hash tag) you can comment single line
"""
You can use a multiline string.
Since Python will ignore string literals that are not assigned to a variable,
you can add a multiline string (triple quotes) in your code, and place your comment inside it.
These are also used as Doc String accessed through __doc__ function
"""

"""
Checking Python Version
>python --version
"""

"""
Running Python Command Line
>python
>>>
OR
>py
>>>
"""

"""
Running Python program from command prompt
>python program_main_file.py
"""

print("Hello World")
print("Hi".__doc__)

"""
Statements in Python typically end with a new line. 
Python does, however, allow the use of the line continuation character (\) to denote that the line should continue.
total = item_one + \
        item_two + \
        item_three
Statements contained within the [], {}, or () brackets do not need to use the line continuation character.
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
"""
