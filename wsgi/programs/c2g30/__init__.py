#@+leo-ver=5-thin
#@+node:2014spring.20140520155021.4796: * @file __init__.py
#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:2014spring.20140520155021.4797: ** <<declarations>> (__init__)
import cherrypy
#@-<<declarations>>
#@+others
#@+node:2014spring.20140520155021.4798: ** class C2G30
# 這是 C2G30 類別的定義
class C2G30(object):
    # 各組利用 index 引導隨後的程式執行
    #@+others
    #@+node:2014spring.20140520155021.4799: *3* index
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g30 分組程式開發網頁, 以下為 W12 的任務執行內容.<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="fillpoly">c2g30 fillpoly 繪圖</a><br />
<a href="drawline">c2g30 drawline 繪圖</a><br />
<a href="animate1">c2g30 animate1 繪圖</a><br />
<a href="flag">c2g30 flag 繪圖</a><br />
<a href="square">c2g30 square 繪圖</a><br />
<a href="star">c2g30 star 繪圖</a><br />
'''
        return outstring
    #@+node:2014spring.20140520155021.4800: *3* fillpoly
    # 以下為 c2g30 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫

    import programs.c2g30 as c2g30
    root.c2g30 = c2g30.C2G30()

    則程式啟動後, 可以利用 /c2g30/fillpoly 呼叫函式執行
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
    #@+node:2014spring.20140520155021.4801: *3* drawline
    ''' 
    假如採用下列規畫

    import programs.c2g30 as c2g30
    root.c2g30 = c2g30.C2G30()

    則程式啟動後, 可以利用 /c2g30/drawline 呼叫函式執行

    context.setTransform(a,b,c,d,e,f)
    a	To Scale the object across along the X axis
    b	To skew the object horizontally(i.e horizontal shear)
    c	To skew the object vertically(i.e vertical shear)
    d	To scale the object across Y axis
    e	To translate the object along the X axis
    f	To translate the object along the Y axis

    a c e
    b d f
    0 0 1
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
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)

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
    #@+node:2014spring.20140520155021.4802: *3* animate1
    @cherrypy.expose
    def animate1(self, *args, **kwargs):
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
    import browser.timer

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    ctx.setTransform(1, 0, 0, -1, 0, 800)
    # 設定 y 的起始值
    y = 0
    # 設定增量變數 inc 為 1
    inc = 1
    # 將畫筆設為紅色
    ctx.strokeStyle = "rgb(255, 0, 0)"

    # 定義畫水平線函式
    def draw():
        # 將 y 與 inc 設為全域變數
        global y, inc
        # 畫新圖之前, 先清除畫面
        ctx.clearRect(0, 0, 800, 800)
        # 開始畫水平線
        ctx.beginPath()
        ctx.moveTo(0, y)
        ctx.lineTo(800-1, y)
        ctx.stroke()
        # y 的值增量
        y = y + inc
        # 若 y 碰到兩個極端值, 則改變增量方向
        if y == 0 or y == 800-1:
            inc = inc*-1

    # ev 為事件輸入, 與隨後的 bind 方法配合
    def start(ev):
        # interval 為全域變數, 因為 stop 函式需要
        global interval
        # 每 10 個 micro second 呼叫一次 draw
        interval = browser.timer.set_interval(draw,10)
        
    def stop(ev):
        global interval
        browser.timer.clear_interval(interval)

    # 將 id 為 start 的按鈕與 start  函式利用 click 事件加以連結
    doc['start'].bind('click', start)
    # 將 id 為 stop 的按鈕與 stop  函式利用 click 事件加以連結
    doc['stop'].bind('click', stop)

    </script>
    <!-- 這裡建立 start 與 stop 按鈕-->
    <button id="start">start</button>
    <button id="stop">stop</button>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4803: *3* flag
    @cherrypy.expose
    def flag(self, *args, **kwargs):
        '''
        原始程式來源: http://blog.roodo.com/esabear/archives/19215194.html
        改寫為 Brython 程式
        '''
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script type="text/javascript" src="/static/Brython2.1.0-20140419-113919/brython.js"></script>
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
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle='rgb(255, 0, 0)'
    ctx.fillRect(0,0,flag_w,flag_h)
    # 再畫青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,flag_w/2,flag_h/2)
    # 畫十二到光芒白日
    ctx.beginPath()
    star_radius = flag_w/8
    angle = 0
    for i in range(24):
        angle += 5*math.pi*2/12
        toX = circle_x + math.cos(angle)*star_radius
        toY = circle_y + math.sin(angle)*star_radius
        # 只有 i 為 0 時移動到 toX, toY, 其餘都進行 lineTo
        if (i):
            ctx.lineTo(toX, toY)
        else:
            ctx.moveTo(toX, toY)
    # 將填色設為白色
    ctx.fillStyle = '#fff'
    ctx.fill()
    # 白日:藍圈
    ctx.beginPath()
    # 查詢 canvas arc 如何定義
    ctx.arc(circle_x, circle_y, flag_w*17/240, 0, math.pi*2, true)
    ctx.closePath()
    # 填色設為藍色
    ctx.fillStyle = 'rgb(0, 0, 149)'
    ctx.fill()
    # 白日:白心
    ctx.beginPath()
    ctx.arc(circle_x, circle_y, flag_w/16, 0, math.pi*2, true)
    ctx.closePath()
    # 填色設為白色
    ctx.fillStyle = '#fff'
    ctx.fill()
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4804: *3* square
    @cherrypy.expose
    def square(self, *args, **kwargs):
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
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    def square(x, y, width, color="black"):
        half = width/2
        draw_line(x+half, y+half, x+half, y-half)
        draw_line(x+half, y-half, x-half, y-half, color="red")
        draw_line(x-half, y-half, x-half, y+half)
        draw_line(x-half, y+half, x+half, y+half)

    for i in range(5):
        square(400, 400, 200+50*i)
        square(400+i*50, 400-i*50, 200)
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4805: *3* star
    @cherrypy.expose
    def star(self, *args, **kwargs):
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

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    # x, y 為中心,  r 為半徑, angle 旋轉角,  solid 空心或實心,  color 顏色
    def star(x, y, r, angle=0, solid=False, color="#f00"):
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
            xout = (x + r*math.sin((360/5)*deg*i+angle*deg))
            yout = (y + r*math.cos((360/5)*deg*i+angle*deg))
            # 外點增量 + 1
            xout2 = x + r*math.sin((360/5)*deg*(i+1)+angle*deg)
            yout2 = y + r*math.cos((360/5)*deg*(i+1)+angle*deg)
            xin = x + rin*math.sin((360/5)*deg*i+36*deg+angle*deg)
            yin = y + rin*math.cos((360/5)*deg*i+36*deg+angle*deg)
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
            else:
                # 空心
                draw_line(xout, yout, xin, yin, color)
                # 畫空心五芒星, 無關畫線次序, 若實心則與畫線次序有關
                draw_line(xout2, yout2, xin, yin, color)
        if(solid):
            ctx.fillStyle = color
            ctx.fill()
    star(600, 600, 100, 30, True, "#00f")
    star(100, 100, 30, 0, True, "#f00")
    #star(300, 300, 50, 0, False, "#000")
    for i in range(5):
        for j in range(5):
            star(200+65*i, 200+65*j, 30, 0, False, "#000")
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4806: *3* w13_1_1
    # w13_1_1 是第十三週第一題的第一個步驟
    # 目的在畫布上畫一條直線
    @cherrypy.expose
    def w13_1_1(self, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 先畫一條直線
    ctx.beginPath()
    # 設定線的寬度為 1 個單位
    ctx.lineWidth = 1
    # 將畫筆移動到 (100, 100) 座標點
    ctx.moveTo(100, 100)
    # 然後畫直線到 (150, 200) 座標點
    ctx.lineTo(150, 200)
    # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
    ctx.strokeStyle = "blue"
    # 實際執行畫線
    ctx.stroke()
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4807: *3* w13_1_2
    # w13_1_2 是第十三週第一題的第二個步驟
    # 目的在畫布上畫四條直線, 然後當作國旗的外框
    @cherrypy.expose
    def w13_1_2(self, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 因為要畫四條直線, 這裡要將畫直線改寫為函式
    # 定義畫直線的函式, 以 (x1, y1) 為起點, 畫到 (x2, y2)
    def draw_line(x1, y1, x2, y2):
        ctx.beginPath()
        # 設定線的寬度為 1 個單位
        ctx.lineWidth = 1
        # 將畫筆移動到 (x1, y1) 座標點
        ctx.moveTo(x1, y1)
        # 然後畫直線到 (x2, y2) 座標點
        ctx.lineTo(x2, y2)
        # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
        ctx.strokeStyle = "blue"
        # 實際執行畫線
        ctx.stroke()
        
    # 準備呼叫 draw_line() 四次以便畫出國旗外框四條線
    # 假設從 (10, 10) 畫到 (410, 310) 的外框
    # 先畫兩條水平線
    draw_line(10, 10, 410, 10)
    draw_line(10, 310, 410, 310)
    # 再畫兩條垂直線
    draw_line(10, 10, 10, 310)
    draw_line(410, 10, 410, 310)
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4808: *3* w13_1_3
    # w13_1_3 是第十三週第一題的第三個步驟
    # 目的在畫布上畫四條直線, 然後當作國旗的外框
    # 而且在框正中心, 畫一個圓
    @cherrypy.expose
    def w13_1_3(self, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 因為要畫四條直線, 這裡要將畫直線改寫為函式
    # 定義畫直線的函式, 以 (x1, y1) 為起點, 畫到 (x2, y2)
    def draw_line(x1, y1, x2, y2):
        ctx.beginPath()
        # 設定線的寬度為 1 個單位
        ctx.lineWidth = 1
        # 將畫筆移動到 (x1, y1) 座標點
        ctx.moveTo(x1, y1)
        # 然後畫直線到 (x2, y2) 座標點
        ctx.lineTo(x2, y2)
        # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
        ctx.strokeStyle = "blue"
        # 實際執行畫線
        ctx.stroke()
        
    # 準備呼叫 draw_line() 四次以便畫出國旗外框四條線
    # 假設從 (10, 10) 畫到 (410, 310) 的外框
    # 先畫兩條水平線
    draw_line(10, 10, 410, 10)
    draw_line(10, 310, 410, 310)
    # 再畫兩條垂直線
    draw_line(10, 10, 10, 310)
    draw_line(410, 10, 410, 310)

    # 以下要在框線中央畫一個圓, 設半徑為 80
    ctx.beginPath()
    # context.arc(x,y,r,sAngle,eAngle,counterclockwise)
    # arc(圓心 x, 圓心 y, 起始角, 終點角, 是否逆時鐘轉)
    circle_x = 10 + 400/2
    circle_y = 10 + 300/2
    ctx.arc(circle_x, circle_y, 80, 0, math.pi*2, true)
    ctx.closePath()
    # 設線顏色為紅色
    ctx.strokeStyle = 'rgb(255, 0, 0)'
    ctx.stroke()

    # 填色設為紅色
    #ctx.fillStyle = 'rgb(255, 0, 0)'
    #ctx.fill()

    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4809: *3* w13_1_4
    # w13_1_4 是第十三週第一題的第四個步驟
    # 目的在畫布上畫四條直線, 然後當作國旗的外框
    # 而且在框正中心, 畫一個圓, 然後在圓中填入紅色
    @cherrypy.expose
    def w13_1_4(self, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 因為要畫四條直線, 這裡要將畫直線改寫為函式
    # 定義畫直線的函式, 以 (x1, y1) 為起點, 畫到 (x2, y2)
    def draw_line(x1, y1, x2, y2):
        ctx.beginPath()
        # 設定線的寬度為 1 個單位
        ctx.lineWidth = 1
        # 將畫筆移動到 (x1, y1) 座標點
        ctx.moveTo(x1, y1)
        # 然後畫直線到 (x2, y2) 座標點
        ctx.lineTo(x2, y2)
        # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
        ctx.strokeStyle = "blue"
        # 實際執行畫線
        ctx.stroke()
        
    # 準備呼叫 draw_line() 四次以便畫出國旗外框四條線
    # 假設從 (10, 10) 畫到 (410, 310) 的外框
    # 先畫兩條水平線
    draw_line(10, 10, 410, 10)
    draw_line(10, 310, 410, 310)
    # 再畫兩條垂直線
    draw_line(10, 10, 10, 310)
    draw_line(410, 10, 410, 310)

    # 以下要在框線中央畫一個圓, 設半徑為 80
    ctx.beginPath()
    # context.arc(x,y,r,sAngle,eAngle,counterclockwise)
    # arc(圓心 x, 圓心 y, 起始角, 終點角, 是否逆時鐘轉)
    circle_x = 10 + 400/2
    circle_y = 10 + 300/2
    ctx.arc(circle_x, circle_y, 80, 0, math.pi*2, true)
    ctx.closePath()
    # 設線顏色為紅色
    #ctx.strokeStyle = 'rgb(255, 0, 0)'
    #ctx.stroke()

    # 填色設為紅色
    ctx.fillStyle = 'rgb(255, 0, 0)'
    ctx.fill()

    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4810: *3* w13_1_5
    # w13_1_5 是第十三週第一題的第五個步驟
    # 目的在畫布上畫四條直線, 然後當作國旗的外框
    # 而且在框正中心, 畫一個圓, 然後在圓中填入紅色
    # 將日本國旗以左上角點座標, 及高度作為單位, 寫為函式
    @cherrypy.expose
    def w13_1_5(self, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 因為要畫四條直線, 這裡要將畫直線改寫為函式
    # 定義畫直線的函式, 以 (x1, y1) 為起點, 畫到 (x2, y2)
    def draw_line(x1, y1, x2, y2):
        global ctx
        ctx.beginPath()
        # 設定線的寬度為 1 個單位
        ctx.lineWidth = 1
        # 將畫筆移動到 (x1, y1) 座標點
        ctx.moveTo(x1, y1)
        # 然後畫直線到 (x2, y2) 座標點
        ctx.lineTo(x2, y2)
        # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
        ctx.strokeStyle = "blue"
        # 實際執行畫線
        ctx.stroke()
        
    # 將外框線寫成函式, 寬為高的 3/2 倍
    # 因為 draw_frame 函式呼叫 draw_line() 因此要在其後定義
    def draw_frame(x, y, w):
        # 準備呼叫 draw_line() 四次以便畫出國旗外框四條線
        # 假設從 (x, y) 畫到 (410, 310) 的外框
        # 先畫兩條水平線
        draw_line(x, y, w*3/2+x, y)
        draw_line(x, w+y, w*3/2+x, w+y)
        # 再畫兩條垂直線
        draw_line(x, y, x, w+y)
        draw_line(w*3/2+x, y, w*3/2+x, w+y)

    def draw_circle(x, y, r, fill=None):
        global ctx
        ctx.beginPath()
        ctx.arc(x, y, r, 0, math.pi*2, true)
        ctx.closePath()
        if fill == None:
            ctx.fillStyle = 'rgb(255, 0, 0)'
            ctx.fill()
        else:
            ctx.strokeStyle = "rgb(255, 0, 0)"
            ctx.stroke()

    # 呼叫 draw_frame()
    width = 400
    draw_frame(10, 10, width)
    # 計算框的中心點座標
    x_center = 10 + width*3/2/2
    y_center = 10 + width/2
    # 中間圓的直徑為寬的 3/5
    radius = width*3/5/2
    draw_circle(x_center, y_center, radius)
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4811: *3* w13_1_6
    # w13_1_6 是第十三週第一題的第六個步驟
    # 目的在將日本國旗繪製寫成函式
    # 可控制的變數為 (x, y) 國旗的左上角座標, 內定為 (10, 10)
    # 國旗的高度以 h 表示, 內定為 300
    @cherrypy.expose
    def w13_1_6(self, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 因為要畫四條直線, 這裡要將畫直線改寫為函式
    # 定義畫直線的函式, 以 (x1, y1) 為起點, 畫到 (x2, y2)
    def draw_line(x1, y1, x2, y2):
        global ctx
        ctx.beginPath()
        # 設定線的寬度為 1 個單位
        ctx.lineWidth = 1
        # 將畫筆移動到 (x1, y1) 座標點
        ctx.moveTo(x1, y1)
        # 然後畫直線到 (x2, y2) 座標點
        ctx.lineTo(x2, y2)
        # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
        ctx.strokeStyle = "blue"
        # 實際執行畫線
        ctx.stroke()
        
    # 將外框線寫成函式, 寬為高的 3/2 倍
    # 因為 draw_frame 函式呼叫 draw_line() 因此要在其後定義
    def draw_frame(x, y, w):
        # 準備呼叫 draw_line() 四次以便畫出國旗外框四條線
        # 假設從 (x, y) 畫到 (410, 310) 的外框
        # 先畫兩條水平線
        draw_line(x, y, w*3/2+x, y)
        draw_line(x, w+y, w*3/2+x, w+y)
        # 再畫兩條垂直線
        draw_line(x, y, x, w+y)
        draw_line(w*3/2+x, y, w*3/2+x, w+y)

    def draw_circle(x, y, r, fill=None):
        global ctx
        ctx.beginPath()
        ctx.arc(x, y, r, 0, math.pi*2, true)
        ctx.closePath()
        if fill == None:
            ctx.fillStyle = 'rgb(255, 0, 0)'
            ctx.fill()
        else:
            ctx.strokeStyle = "rgb(255, 0, 0)"
            ctx.stroke()

    def japan_flag(x, y, w):
        width = w
        draw_frame(x, y, width)
        # 計算框的中心點座標
        x_center = x + width*3/2/2
        y_center = y + width/2
        # 中間圓的直徑為寬的 3/5
        radius = width*3/5/2
        draw_circle(x_center, y_center, radius)

    # 呼叫 japan_flag, 以 60 為單位, 用迴圈繪圖
    width = 60
    # x 方向增量與  y 方向增量
    xinc = width*3/2 + 15
    yinc = width + 15
    for i in range(5):
        for j in range(5):
            japan_flag(10+i*xinc, 10+j*yinc, width)
    </script>
    </body>
    </html>
    '''
        return outstring
    #@+node:2014spring.20140520155021.4812: *3* w13_1_7
    # w13_1_7 是第十三週第一題的第七個步驟
    # 目的在 CherryPy 設置操控變數, 讓使用者可以透過 URL 操控繪圖內容
    @cherrypy.expose
    def w13_1_7(self, x=10, y=10, w=300, *args, **kwargs):
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

    # 以下可以利用 ctx 物件進行畫圖
    # 因為要畫四條直線, 這裡要將畫直線改寫為函式
    # 定義畫直線的函式, 以 (x1, y1) 為起點, 畫到 (x2, y2)
    def draw_line(x1, y1, x2, y2):
        global ctx
        ctx.beginPath()
        # 設定線的寬度為 1 個單位
        ctx.lineWidth = 1
        # 將畫筆移動到 (x1, y1) 座標點
        ctx.moveTo(x1, y1)
        # 然後畫直線到 (x2, y2) 座標點
        ctx.lineTo(x2, y2)
        # 設定顏色為藍色, 也可以使用 "rgb(0, 0, 255)" 字串設定顏色值
        ctx.strokeStyle = "blue"
        # 實際執行畫線
        ctx.stroke()
        
    # 將外框線寫成函式, 寬為高的 3/2 倍
    # 因為 draw_frame 函式呼叫 draw_line() 因此要在其後定義
    def draw_frame(x, y, w):
        # 準備呼叫 draw_line() 四次以便畫出國旗外框四條線
        # 假設從 (x, y) 畫到 (410, 310) 的外框
        # 先畫兩條水平線
        draw_line(x, y, w*3/2+x, y)
        draw_line(x, w+y, w*3/2+x, w+y)
        # 再畫兩條垂直線
        draw_line(x, y, x, w+y)
        draw_line(w*3/2+x, y, w*3/2+x, w+y)

    def draw_circle(x, y, r, fill=None):
        global ctx
        ctx.beginPath()
        ctx.arc(x, y, r, 0, math.pi*2, true)
        ctx.closePath()
        if fill == None:
            ctx.fillStyle = 'rgb(255, 0, 0)'
            ctx.fill()
        else:
            ctx.strokeStyle = "rgb(255, 0, 0)"
            ctx.stroke()

    def japan_flag(x, y, w):
        width = w
        draw_frame(x, y, width)
        # 計算框的中心點座標
        x_center = x + width*3/2/2
        y_center = y + width/2
        # 中間圓的直徑為寬的 3/5
        radius = width*3/5/2
        draw_circle(x_center, y_center, radius)

    # 利用外部的 x, y, w 變數來控制國旗位置與大小
    # 當所要求\的國旗超出畫布, 則採取畫最大幅的國旗因應
    if '''+str(x)+'''+'''+str(int(w)*3/2)+'''< canvas.width and \
        '''+str(y)+'''+'''+str(w)+'''< canvas.width:
        japan_flag('''+str(x)+''', '''+str(y)+''', '''+str(w)+''')
    else:
        # 畫出最大面的國旗
        japan_flag(10, 10, 790*2/3)
    </script>
    </body>
    </html>
    '''
        return outstring
    #@-others
#@-others
#@-leo
