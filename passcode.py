with open('./input/passcode.txt', 'r') as f:
  lines = f.readlines()
  code = 50
  count = 0
  for r in lines:
    direction = r[:1]
    r_code = int(r[1:len(r)].strip())
    
    num_dir = 1 if direction == 'R' else -1
    while r_code > 0:
      if code == 100:
        code = 0
      elif code == -1:
        code = 99
      else:
        code += num_dir
        r_code -= 1
      
      if code == 0 and r_code > 0:
        count += 1
    
    if code == -1:
      code = 99
    if code == 100:
      code = 0
      
    if code == 0:
      count += 1
  print(count)