def add(a: int, b: int) -> int:
    return a + b

print(add("a", "b"))  

# List:-

from typing import List

numbers: List[int] = [1, 2, 3]
print(numbers)

#Tuples:-

from typing import Tuple

point: Tuple[int, int] = (2, 3)
print(point)


# Dictionary:-
from typing import Dict

data: Dict[str, int] = {"age": 21}
print(data)

# Set :-
from typing import Set

s: Set[int] = {1, 2, 3}
print(s)
