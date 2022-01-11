"""
* clone from https://github.com/matchai/waka-box
"""

from math import floor


def generate_horizontal_bar(percent: float, size: int):
    symbols = '░▏▎▍▌▋▊▉█'
    frac = floor((size * 8 * percent) / 100)
    bars_full = floor(frac / 8)
    if bars_full >= size:
        return symbols[8:9] * size

    semi = frac % 8
    return ''.join([symbols[8:9] * bars_full, symbols[semi:semi + 1]]).ljust(size, symbols[0:1])
