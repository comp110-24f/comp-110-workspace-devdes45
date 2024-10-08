"""Challenge question 4: implementing both other files"""

__author__ = "730755654"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

# uses imported functions
print(concat(x, y))
get_coords(x, y)
