import math


def pythagoras(x1, x2, y1, y2):
  """Pythagoras' theorem: a*a + b*b = c*c
  """
  dx = abs(x1-x2)
  dy = abs(y1-y2)
  return math.sqrt(dx*dx+dy*dy)


class Node():
  def __init__(self, x, y, parent=None, start=False, end=False):
    global sN, eN, dim
    global XYStart, XYEnd
    self.x = x
    self.y = y
    self.parent = parent
    if start: 
      self.g = 0
      self.h = int(pythagoras(XYStart[0], XYEnd[0], XYStart[1], XYEnd[1]) * 10)
      self.f = self.h
      return
    if end:
      self.g = int(pythagoras(XYStart[0], XYEnd[0], XYStart[1], XYEnd[1]) * 10)
      self.h = 0
      self.f = self.g
      return
    self.g = self.parent.g + Node.d(parent, self)
    self.h = Node.d(self, eN) 
    self.f = self.g + self.h
    

  @staticmethod
  def d(n1, n2) -> float:
    """Returns distance between nodes
    """
    return int(pythagoras(n1.x, n2.x, n1.y, n2.y)*10)


  def neighbors(self):
    global dim, explored, mm
    self._neighbors = []
    print(len(mm), len(mm[0]))
    for i in range(self.y-1, self.y+2):
      for j in range(self.x-1, self.x+2):
        if i < 0 or i > dim[1] or j < 0 or j > dim[0] or (i == self.y and j == self.x):
          continue
        if mm[j-1][i-1]==1:
          continue
        n = Node(j, i, parent=self)
        if n in explored:
          continue
        self._neighbors.append(n)
    return self._neighbors

  def step(self):
    self.g = self.g + Node.d(self, self.parent)
    self.h = Node.d(self, eN)
    self.f = self.g+self.h


  def __repr__(self):
    #return f"Node{(self.x, self.y)}" 
    return f"Node{(self.x, self.y, self.f)}" 

  
  def __eq__(self, other):
    if not isinstance(other, Node):
      return NotImplemented
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((self.x, self.y))


def gen(dim=(8,8)):
  r = []
  for i in range(dim[0]):
    r.append([0]*dim[1])
  return r

#TODO: Change X and Y axis
def astar(m=gen(), start=(1,1), end=(3,3)):
  """A* pathfinding algorithm
  Args:
    m: Map (2D-Array y, x)
    start: Start Node (List length 2)
    end: End Node (List length 2)
  """
  global explored, dim, sN, eN, XYStart, XYEnd, mm
  mm = m
  XYStart = start
  XYEnd = end
  dim = (len(m), len(m[0])) # Y, X
  print(dim)
  explored = set()
  o = set()
  sN = Node(XYStart[0], XYStart[1], start=True)
  eN = Node(XYEnd[0], XYEnd[1], end=True)
  o.add(sN)
  counter = 0
  while o:
    c = min(o, key=lambda x: x.f)
    buf = [x for i, x in enumerate(o) if x.f == c.f]
    print(c)
    if len(buf) > 1:
      print()
      c = min(buf, key=lambda x: x.h)
    if c == eN:
      path = []
      while c.parent:
        path.append(c)
        c = c.parent
      return path, explored, o
    o.remove(c)
    for n in c.neighbors():
      o.add(n)
    explored.add(c)
  print(m, start, end)
  return "fuck"


if __name__ == "__main__":
  r  = astar()
  print(r)
 
