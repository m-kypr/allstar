let grid = [];
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const button = document.getElementById("button");
const pixelSize = 4;
const gridSize = 1; // Setting this to 0 crashes firefox (bug?)
const padding = 1;
const brushSize = 4;
const mousePosition = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
var mouseDown = false;
var pixelsX = 0;
var pixelsY = 0;
let startPx = 0;
let endPx = 0;
var path = [];
var explored = [];
var o = [];

const resize = () => {
  width = window.innerWidth;
  height = window.innerHeight;
  pixelsY = Math.floor(height / ((pixelSize + padding) * gridSize));
  pixelsX = Math.floor(width / ((pixelSize + padding) * gridSize));
  console.log(pixelsX, pixelsY);
  canvas.width = width;
  canvas.height = height;
  grid = [];
  for (var y = 0; y < pixelsY; y++) {
    for (var x = 0; x < pixelsX; x++) {
      grid.push([
        x * (pixelSize + padding),
        y * (pixelSize + padding),
        pixelSize,
        pixelSize,
        0,
      ]);
    }
  }
  button.style.left = width - 120 - 20 + "px";
  // button.style.borderColor = "red red red red"
  drawGrid();
};
const drawGrid = () => {
  for (var i = 0; i < grid.length; i++) {
    if (
      mouseDown &
      (mousePosition.x >= grid[i][0] - pixelSize * brushSize) &
      (mousePosition.x <= grid[i][0] + pixelSize) &
      (mousePosition.y >= grid[i][1] - pixelSize * brushSize) &
      (mousePosition.y <= grid[i][1] + pixelSize)
    ) {
      grid[i][4] = 1;
    }
  }
  for (var i = 0; i < grid.length; i++) {
    ctx.globalAlpha = 1;
    ctx.fillStyle = "#222";
    if (grid[i][4]) ctx.fillStyle = "#000";
    if (i == pixelsX + 1) {
      ctx.fillStyle = "#0ff";
      startPx = i;
    }
    if (i == grid.length - pixelsX - 2) {
      ctx.fillStyle = "#0ff";
      endPx = i;
    }
    if (explored.includes(i)) ctx.fillStyle = "#0f0";
    if (o.includes(i)) ctx.fillStyle = "#00f";
    if (path.includes(i)) ctx.fillStyle = "#ff0";
    ctx.fillRect(grid[i][0], grid[i][1], grid[i][2], grid[i][3]);
  }
};

const draw = () => {
  drawGrid();
  requestAnimationFrame(draw);
};

resize();
draw();
document.onmousemove = (e) => {
  mousePosition.x = e.pageX;
  mousePosition.y = e.pageY;
};
window.addEventListener("mousedown", function (e) {
  mouseDown = true;
});
window.addEventListener("mouseup", function (e) {
  mouseDown = false;
});
window.addEventListener("resize", resize);
button.addEventListener("click", function (e) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/astar", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  m = new Object();
  // console.log(grid[startPx])
  let start = [];
  let end = [];
  for (let i = 0; i < grid.length; i++) {
    const e = grid[i];
    var ind = Math.floor(i / pixelsX);
    if (i == startPx) {
      start[0] = ind;
      start[1] = Math.floor(i / pixelsY);
    }
    if (i == endPx) {
      end[0] = ind;
      end[1] = Math.floor(i / pixelsY);
    }
    if (!m[ind]) m[ind] = [e[4]];
    else m[ind].push(e[4]);
  }
  m = Object.values(m); // format: y, x
  console.log(start, end);
  console.log(m);
  xhr.send(
    JSON.stringify({
      m: m,
      start: start,
      end: end,
    })
  );

  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4) {
      console.log(xhr.responseText);
      j = JSON.parse(xhr.responseText);
      path = j["path"];
      explored = j["explored"];
      o = j["open"];
      // console.log(path)
    }
  };
  var origColor = button.style.backgroundColor;
  button.style.backgroundColor = "orange";
  button.style.borderRadius = "6px";
  window.setTimeout(function (e) {
    button.style.backgroundColor = origColor;
    button.style.borderRadius = "2px";
  }, 300);
});
