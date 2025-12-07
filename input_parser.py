def get_lines(day, test_type=''):
    file_path = get_file_path(day, test_type)
    print(file_path)
    with open(file_path, 'r') as f:
        return [s.strip() for s in f.readlines()]

def get_line(day, test_type=''):
    file_path = get_file_path(day, test_type)
    print(file_path)
    with open(file_path, 'r') as f:
        return f.read().strip()
    
def get_file_path(day, test_type):
    return f'input/{day}{test_type if test_type == '' else f'_{test_type}'}.txt'