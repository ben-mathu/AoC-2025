from input_parser import get_lines

# each line consists
# light diagram - in []
# button wiring schematic - in ()
# joltage requirement
machines = list(map(lambda  e: e.strip(), get_lines(10, 'e')))
# print(machines)

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

def dfs(state, obj, schema):
  presses = 1
  comb = 0
  i = 0
  while True:
    new_state = state
    batteries = [schema[i:][j] for j in range(comb)]
    for bat in batteries:
      new_state = swtich(new_state, bat)
    
    rem_batteries = schema[i+comb:]
    new_new_state = new_state
    for rem in rem_batteries:
      if comb == 0: i+=1
      new_new_state = swtich(new_state, rem)
      if new_new_state == obj:
        return presses

    # reached end of list for current set up
    if i+1 == len(schema) - comb:
      comb += 1
      presses+=1

    # move to next index to iterate the next combination, comb
    i+=1
    

    
memo = {}
count = 0
for machine in machines:
  components = machine.split(' ')
  lights = [e for e in components[0][1:len(components[0])-1]]
  lights_obj = ['.' for i in range(len(components[0][1:len(components[0])-1]))]
  schema = [list(map(int, components[i][1:len(components[i])-1].split(','))) for i in range(1, len(components) - 1)]

  presses = dfs(lights, lights_obj, schema[::-1])
  print(presses)
  count += presses
      
print(count)