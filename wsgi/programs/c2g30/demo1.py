#@+leo-ver=5-thin
#@+node:2014spring.20140520155021.4817: * @file demo1.py
#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:2014spring.20140520155021.4818: ** <<declarations>> (demo1)
import cherrypy
#@-<<declarations>>
#@+others
#@+node:2014spring.20140520155021.4819: ** class DEMO1
# 這是 DEMO1 類別的定義
class DEMO1(object):
    # 各組利用 index 引導隨後的程式執行
    #@+others
    #@+node:2014spring.20140520155021.4820: *3* index
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
<!DOCTYPE html>
<html lang="en">
<head>
<script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
<meta charset=utf-8 />
<title>Canvas Gradient</title>
<style>
body {
  background: #000;
}
canvas {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}
</style>
</head>
<body id="body" onload="brython()">
<canvas id="plotarea" height="600" width="600"></canvas>
<script type="text/python">
from browser import doc, html
# 準備繪圖畫布
canvas = doc["plotarea"]
ctx = canvas.getContext("2d")
grad = None
color = 255

def change_color(event):
    width = canvas.width
    height = canvas.height
    x,y = event.clientX,event.clientY
    rx = 600 * x / width
    ry = 600 * y / height
        
    xc = int(256 * x / width)
    yc = int(256 * y / height)

    grad = ctx.createRadialGradient(rx, ry, 0, rx, ry, 600)
    grad.addColorStop(0, '#000')
    grad.addColorStop(1, 'rgb(%s,%s,%s)' %(xc,(255-xc),yc))
    ctx.fillStyle = grad
    ctx.fillRect(0, 0, 600, 600)

doc["body"].bind('mousemove', change_color)

</script>


</body>
</html>
'''
        return outstring
    #@-others
#@-others
#@-leo
