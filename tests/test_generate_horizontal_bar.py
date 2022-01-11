from simple_text_chart import generate_horizontal_bar


def test_generate_bar():
    symbols = '░▏▎▍▌▋▊▉█'
    for n in range(8):
        assert generate_horizontal_bar(n * (100 / 8), 1) == symbols[n]


def test_generate_bar_row():
    assert generate_horizontal_bar(0, 40) == '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    assert generate_horizontal_bar(25, 40) == '██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
    assert generate_horizontal_bar(50, 40) == '████████████████████░░░░░░░░░░░░░░░░░░░░'
    assert generate_horizontal_bar(75, 40) == '██████████████████████████████░░░░░░░░░░'
    assert generate_horizontal_bar(100, 40) == '████████████████████████████████████████'


def test_generate_bar_length():
    for size in (1, 5, 10, 20, 40, 80):
        assert len(generate_horizontal_bar(0, size)) == size
