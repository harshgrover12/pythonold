# Named Tuple is compromise between tuple and dictionary

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)
print(color.red)
