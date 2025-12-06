def get_lines(day, test_type=''):
    with open(f'{day}{'_e' if test_type == 'e' else ''}.txt', 'r') as f:
        return map(lambda s: s.strip(), f.readlines())

def get_line(day, test_type=''):
    with open(f'{day}{'_e' if test_type == 'e' else ''}.txt', 'r') as f:
        return f.read().strip()