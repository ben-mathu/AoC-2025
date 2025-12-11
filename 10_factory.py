from input_parser import get_lines

# each line consists
# light diagram - in []
# button wiring schematic - in ()
# joltage requirement
machines = list(map(lambda  e: e.strip(), get_lines(10, 'e')))
print(machines)

# Goal [.##.]
# 
# no press [....]
# 3 -> [...#]
# 1,3 -> [.#..]
# 2 -> [.##.]
# 
# Reversed -> (3) (1,3) (2) (2,3) (0,2) (0,1)
# [.##.] -> 
def swtich(lights, schema):
  s = lights.copy()
  for button in schema:
    if s[button] == '.':
      s[button] = '#'
    else:
      s[button] = '.'
  return s

visited = []
def dfs(i, depth, state, obj, schema):
  if depth == len(schema):
    return depth, state

  new_state = []
  new_schema = [schema[i]] + schema[:i] + schema[i+1:]
  if not (i > 0 and depth == 0):
    for j in range(depth, len(new_schema)):
      
      new_state = swtich(state, schema[j])
      if new_state == obj:
        break
    
  if new_state == obj:
    return depth, new_state
  else:
    new_state = swtich(state, new_schema[depth])
    d, new_state = dfs(i, depth + 1, new_state, obj, schema)
    visited.append(new_schema[i])
  return d, new_state
    
memo = {}
count = 0
for machine in machines:
  components = machine.split(' ')
  lights = [e for e in components[0][1:len(components[0])-1]]
  lights_obj = ['.' for i in range(len(components[0][1:len(components[0])-1]))]
  schema = [tuple(map(int, components[i][1:len(components[i])-1].split(','))) for i in range(1, len(components) - 1)]

  min_button_pressed = float('inf')
  for i in range(len(schema)):
    c, new_state = dfs(i, 0, lights, lights_obj, schema)
    
    if c > 0:
      min_button_pressed = min(min_button_pressed, c)
  count += min_button_pressed
      
print(count)