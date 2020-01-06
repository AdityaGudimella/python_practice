import typing
# Implement every function in functools and more_itertools and itertools using python loops

# Write a function that finds the length of an iterable without storing it in memory.
def iter_len(iterable: typing.Iterable) -> int:
    """ Return len of iterable without storing it in memory """


# Write a function that finds the length of an iterable without storing it in memory and without consuming it.
def iter_len(iterable: typing.Iterable) -> int:
    """
    iterable = (x for x in range(5))
    assert iter_len(iterable) == 5
    assert len(list(iterable)) == 5
    """

# Related Qeustions:
#  - [1295] Find Numbers with Even Number of Digits
