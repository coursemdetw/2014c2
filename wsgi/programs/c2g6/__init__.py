import cherrypy

# 這是 C2G6 類別的定義
class C2G6(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g6 分組程式開發網頁, 以下為 W12 的任務執行內容.<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="fillpoly">c2g6 fillpoly 繪圖</a><br />
<a href="drawline">c2g6 drawline 繪圖</a><br />
<a href="triangle">c2g6 triangle 繪圖</a><br />
<a href="triangle2">c2g6 triangle2 繪圖</a><br />
<a href="japanflag">c2g6 japanflag 繪圖</a><br />
<a href="usaflag">c2g6 usaflag 繪圖</a><br />
'''
        return outstring

    # 以下為 c2g2 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫
    
    import programs.c2g6 as c2g6
    root.c2g6 = c2g6.C2G6()
    
    則程式啟動後, 可以利用 /c2g2/fillpoly 呼叫函式執行
    '''
    @cherrypy.expose
    def fillpoly(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入數學模組的所有方法
    from math import *
    # 導入時間模組
    import time
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")

    # 定義座標轉換(0, 0) 到 (75, 20)
    def change_ref_system(x, y):
        return (20 + x * 8, 420 - y * 20)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    def fill():
        ctx.beginPath()
        ctx.moveTo(75,50)
        ctx.lineTo(100,75)
        ctx.lineTo(100,25)
        ctx.fill()
        
    def star():
        ctx.beginPath()
        ctx.moveTo(0,50)
        ctx.lineTo(11,16)
        ctx.lineTo(48,16)
        ctx.fill()

    ctx.fillStyle = "blue"
    fill()
    star()

    x1, y1 = change_ref_system(0, 0)
    for 索引 in range(0, 70, 4):
        x2, y2 = change_ref_system(索引, 20)
        draw_line(x1, y1, x2, y2, linethick=3, color="blue")
    x1, y1 = change_ref_system(70, 0)
    for 索引 in range(0, 70, 4):
        x2, y2 = change_ref_system(索引, 20)
        draw_line(x1, y1, x2, y2, linethick=3, color="red")
    </script>
    </body>
    </html>
    '''
        return outstring
    ''' 
    假如採用下列規畫
    
    import programs.c2g6 as c2g6
    root.c2g6 = c2g6.C2G6()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def drawline(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    
    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(0, 0, 100, 100)
    </script>
    </body>
    </html>
    '''
        return outstring







    @cherrypy.expose
    def triangle(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(100, 100, 150, 250)
    draw_line(150,  250, 400, 400)
    draw_line(400, 400, 100, 100)
   
    </script>
    </body>
    </html>
    '''
        return outstring


    @cherrypy.expose
    def triangle2(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    def fill():
        ctx.beginPath()
        ctx.moveTo(100,100)
        ctx.lineTo(150,250)
        ctx.lineTo(400,400)
        ctx.fill()

    ctx.fillStyle = "red"
    fill()

    draw_line(100, 100, 150, 250, linethick = 3, color = "blue")
    draw_line(150, 250, 400, 400, linethick = 3, color = "blue")
    draw_line(400, 400, 100, 100, linethick = 3, color = "blue")

    </script>
    </body>
    </html>
    '''
        return outstring



    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def japanflag(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript"        src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="300" height="200"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w = canvas.width
    flag_h = canvas.height
    circle_x = flag_w/2
    circle_y = flag_h/2

    # 先畫白
    ctx.fillStyle= 'black'
    ctx.fillRect(0,0,flag_w,flag_h)
    ctx.fillStyle= 'white'
    ctx.fillRect(0,0,flag_w-10,flag_h-10)
    # 白日:red心
    ctx.beginPath()
    ctx.arc(circle_x, circle_y, flag_w/8, flag_h/8, math.pi*2 ,  true)
    ctx.closePath()
    # 填色設為red
    ctx.fillStyle = 'red'
    ctx.fill()
    
    </script>
    </body>
    </html>
    '''
        return outstring

    ''' 
    假如採用下列規畫
    
    import programs.c2g7 as c2g7
    root.c2g7 = c2g7.C2G7()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    '''
 
    @cherrypy.expose
    def usaflag(self, *args, **kwargs):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
    </head>
    <body onload="brython({debug:1, cache:'version'})">
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)



    # x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色
    def star(x, y, r, angle=0, solid=False, color="white"):
        # 以 x, y 為圓心, 計算五個外點
        deg = math.pi/180
        # 圓心到水平線距離
        a = r*math.cos(72*deg)
        # a 頂點向右到內點距離
        b = (r*math.cos(72*deg)/math.cos(36*deg))*math.sin(36*deg)
        # 利用畢氏定理求內點半徑
        rin = math.sqrt(a**2 + b**2)
        # 查驗 a, b 與 rin
        #print(a, b, rin)
        if(solid):
            ctx.beginPath()
        for i in range(5):
            xout = (x + r*math.sin(72*deg*i+angle*deg))
            yout = (y + r*math.cos(72*deg*i+angle*deg))
            # 外點增量 + 1
            xout2 = x + r*math.sin(72*deg*(i+1)+angle*deg)
            yout2 = y + r*math.cos(72*deg*(i+1)+angle*deg)
            xin = x + rin*math.sin(72*deg*i+36*deg+angle*deg)
            yin = y + rin*math.cos(72*deg*i+36*deg+angle*deg)
            # 查驗外點與內點座標
            #print(xout, yout, xin, yin)
            if(solid):
                # 填色
                if(i==0):
                    ctx.moveTo(xout, yout)
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
                else:
                    ctx.lineTo(xin, yin)
                    ctx.lineTo(xout2, yout2)
        if(solid):
            ctx.fillStyle = 'white'
            ctx.fill()

    for i in range(7):
        ctx.fillStyle='rgb(255, 0, 0)'
        ctx.fillRect(0, 0+40*i, 390, 20)

    ctx.fillStyle='rgb(0, 0, 149)'
    ctx.fillRect(0, 120, 210, 140)

    for i in range(6):
        for j in range(5):
            star(20+34*i, 134+28*j, 8, 0, True, "white")
    for i in range(5):
        for j in range(4):
            star(36+34*i, 148+28*j, 8, 0, True, "white")
    
    </script>
    </body>
    </html>
    '''
        return outstring