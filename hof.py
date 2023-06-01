from functools import reduce
def is_present(lst,x):
  return list(map(lambda y: 1 if y == x else 0, lst))

def count_occ(lst,target):
  return sum(map(lambda x: 1 if x == target else 0, lst))

def uniq(lst):
  return [x for i, x in enumerate(lst) if x not in lst[:i]]

def find_max(matrix):
  return max(max(row) for row in matrix)

def count_ones(matrix):
  count = 0
  for row in matrix:
     for element in row:
            if element == 1:
                count += 1
  return count

def addgenerator(x):
  return lambda y: x + y

def apply_to_self():
  return lambda element, func: element + func(element)

def ap(fns,args):
  return [fn(arg) for fn, arg in zip(fns, args)]

def map2(matrix,f):
  return [[f(element) for element in row] for row in matrix]
