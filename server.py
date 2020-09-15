from astar import astar

from flask import Flask, render_template, request
app = Flask(__name__)


def d2tod1(list_of_nodes, dim):
  rb = []
  for n in list_of_nodes:
    rb.append(dim[1]*n.x+n.y)
  return rb

@app.route('/astar', methods=['POST'])
def handle_astar():
  import json
  r = json.loads(request.data)
  m = r['m']
  sN = r['start']
  eN = r['end']
  route, explored, o = astar(m, sN, eN)
  dim = (len(m), len(m[0]))
  print(route)
  return json.dumps({'path': d2tod1(route, dim), 'explored': d2tod1(explored, dim), 'open': d2tod1(o, dim)})
  

@app.route('/')
def hello_world():
  dim = (10, 20)
  grid = []
  for i in range(dim[0]):
    b = []
    for j in range(dim[1]):
      b.append(f"<div id={i}{j}></div>")
    grid.append("".join(b))
    #print(grid)
  grid = "\n".join(grid)
  # print(grid)
  return render_template('index.html') 

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port='4000')
