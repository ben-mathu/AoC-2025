from input_parser import get_lines

def map_devices(day, type):
  lines = get_lines(day, type)
  devices = {}
  for l in lines:
    name, output = l.split(':')
    device_list = output.strip().split(' ')

    devices[name] = device_list
  return devices

class Node:
  visited = []

  def __init__(self, name, children=None):
    self.name = name
    self.children = children
    
  def count_paths(self):
    if not self.children:
      return 1
    
    total_paths = 0
    for child in self.children:
      total_paths += child.count_paths()
    
    return total_paths
  
  def find_node(self, name):
    if self.name == name:
      return self
    
    if self.children:
      for child in self.children:
        if child.name == 'svr':
          print(child.name)
        result = child.find_node(name)
        if result:
          return result
    
    return None
  
  def count_path_by_params(self, found1, found2):
    if self.name == 'out':
      if found1 and found2:
        return 1
      else:
        return 0
      
    total_count = 0
    for child in self.children:
      total_count += child.count_path_by_params(found1 or child.name == 'dac', found2 or child.name == 'fft')
    
    return total_count

def dfs(name, devices):
  if name == 'out':
    return Node(name)
  
  new_node = Node(name)
  for output in devices[name]:
    child = dfs(output, devices)
    if not new_node.children:
      new_node.children = []
    new_node.children.append(child)

  return new_node

# Part 1 example
devices_e = map_devices('11', 'e')
root = dfs('you', devices_e)
print('Possible path count', root.count_paths())

# Part 1
devices = map_devices('11', '')
root = dfs('you', devices)
print('Possible path count', root.count_paths())


memo = {}
def dfs_2(name, found1, found2, inputs):
  state = (name, found1, found2)
  
  if state in memo:
    return memo[state]
  
  if name == 'out':
    return 1 if found1 and found2 else 0
  
  total = 0
  for output in inputs[name]:
    total += dfs_2(output, found1 or output == 'dac', found2 or output == 'fft', inputs)

  memo[state] = total
  return total

# Part 2 example
devices_e = map_devices('11', '2_e')
count = dfs_2('svr', False, False, devices_e)
print('Possible path count', count)

# Part 2
total_count = dfs_2('svr', False, False, devices)
print('Possible path count', count)