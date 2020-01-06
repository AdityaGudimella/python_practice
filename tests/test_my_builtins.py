import pytest
import hamcrest as hm
from hypothesis import given, strategies as st

from python_practice import my_builtins as mb


def star_iterables_strategy():
    return st.lists(elements=st.integers())


@given(a=star_iterables_strategy(), b=star_iterables_strategy())
def test_zip_two(a, b):
    hm.assert_that(list(zip(a, b)), hm.equal_to(list(mb.zip(a, b))))
