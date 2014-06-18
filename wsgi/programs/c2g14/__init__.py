import cherrypy

# 這是 C2G14 類別的定義
class C2G14(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g14 分組程式開發網頁, 以下為 W12 的任務執行內容.<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="fillpoly">c2g14 fillpoly 繪圖</a><br />
<a href="drawline">c2g14 drawline 繪圖</a><br />
<a href="drawsquare">c2g14drawsquare 繪圖</a><br />
<a href="drawstar">c2g14 drawstar 繪圖</a><br />
<a href=" triangle">c2g14 triangle 繪圖</a><br />
<a href=" triangle2">c2g14 triangle2 繪圖</a><br />
<a href=" Japan">c2g14 Japan 繪圖</a><br />
<a href=" American_flag ">c2g14 American_flag  繪圖</a><br />
<a href=" american_flagw14_1 ">c2g14 American_flag_1  繪圖</a><br />
<a href=" american_flagw14_2 ">c2g14 American_flag_2  繪圖</a><br />
<a href=" american_flagw14_3 ">c2g14 American_flag_3  繪圖</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A12%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20turn_right()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0Adef%20hurdles1()%3A%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%20%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0Ahurdles1()%0Ahurdles1()%0Ahurdles1()%0Ahurdles1()%0Ahurdles1()%0Amove()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g14 w15任務一</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20back()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0Adef%20turn_right()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0Adef%20hurdles3()%3A%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20back()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20back()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0Ahurdles3()%0Ahurdles3()%0Amove()%0Aturn_left()%0Amove()%0Aturn_right()%0Amove()%0Aturn_right()%0Amove()%0Aturn_left()%0Amove()%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g14 w15任務二</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%2C%22large_world%22%3Afalse%7D&editor=def%20back()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0Adef%20turn_right()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0A%20%20%20%20turn_left()%0Adef%20hurdles3()%3A%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20back()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20back()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0Ahurdles3()%0Ahurdles3()%0Amove()%0Aturn_left()%0Amove()%0Aturn_right()%0Amove()%0Aturn_right()%0Amove()%0Aturn_left()%0Amove()%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g14 w15任務三( Hurdles1請自行點選)</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A11%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%2C%223%2C2%22%3A%5B%22east%22%5D%2C%226%2C2%22%3A%5B%22east%22%5D%2C%227%2C2%22%3A%5B%22east%22%5D%2C%227%2C3%22%3A%5B%22east%22%5D%2C%2210%2C2%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn_left()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g14 w16任務一 </a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn_left()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g14 w16任務二( Hurdles1~3請自行點選)</a><br />
'''
        return outstring

    # 以下為 c2g14 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫
    
    import programs.c2g14 as c2g14
    root.c2g14 = c2g14.C2G14()
    
    則程式啟動後, 可以利用 /c2g9/fillpoly 呼叫函式執行
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
    
    import programs.c2g14 as c2g14
    root.c2g14 = c2g9.C2G14()
    
    則程式啟動後, 可以利用 /c2g14/drawline 呼叫函式執行
    '''
    @cherrypy.expose
    def drawsquare(self, *args, **kwargs):
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

    draw_line(0, 0, 0, 100)
    draw_line(0, 100, 100, 100)
    draw_line(100, 100, 100, 0)
    draw_line(100, 0, 0 , 0)
    </script>
    </body>
    </html>
    '''
    
        return outstring
        
    @cherrypy.expose
    def drawstar(self, *args, **kwargs):
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

    draw_line(300, 300, 358.78, 342.71)
    draw_line(358.78, 342.71, 417.56, 300)
    draw_line(417.56, 300, 395.11, 369.1)
    draw_line(395.11, 369.1, 453.88, 411.8)
    draw_line(453.88, 411.8, 381.23, 411.8)
    draw_line(381.23, 411.8, 358.78, 480.9)
    draw_line(358.78, 480.9, 336.33, 411.8)
    draw_line(336.33, 411.8, 263.67, 411.8)
    draw_line(263.67, 411.8, 322.45, 369.1)
    draw_line(322.45, 369.1, 300, 300)
    </script>
    </body>
    </html>
    '''
        return outstring
        
    @cherrypy.expose
    def  triangle(self, *args, **kwargs):
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
     
    draw_line(100, 100, 150 , 250, linethick = 3, color="blue")
    draw_line(150, 250 ,400 , 400, linethick = 3, color="blue")
    draw_line(400, 400, 100 , 100, linethick = 3, color="blue" )

    </script>
    </body>
    </html>
    '''
        return outstring
        
    @cherrypy.expose
    def  triangle2(self, *args, **kwargs):
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

    def fill():
        ctx.beginPath()
        ctx.moveTo(100,100)
        ctx.lineTo(150,250)
        ctx.lineTo(400,400)
        ctx.fill()

    ctx.fillStyle = "red"
    fill()
     
    draw_line(100, 100, 150 , 250, linethick = 3, color="blue")
    draw_line(150, 250 ,400 , 400, linethick = 3, color="blue")
    draw_line(400, 400, 100 , 100, linethick = 3, color="blue" )

    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def Japan(self, *args, **kwargs):
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
    circle_x = flag_w/2
    circle_y = flag_h/2
    # 黑底
    ctx.fillStyle='rgb(0, 0, 0)'
    ctx.fillRect(0,0,flag_w,flag_h)
    # 白底
    ctx.fillStyle='rgb(255, 255, 255)'
    ctx.fillRect(0,0,flag_w-5,flag_h-5)
    # 紅日
    ctx.beginPath()
    ctx.arc(circle_x, circle_y, flag_w*17/240, 0, math.pi*2, true)
    ctx.closePath()
    # 填色設為白色
    ctx.fillStyle = 'rgb(255, 0, 0)'
    ctx.fill()
    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def American_flag (self, *args, **kwargs):
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
    <canvas id="plotarea" width="190" height="100"></canvas>
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
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
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
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(12+12*i, 12+10*j, 3, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(6+12*i, 6+10*j, 3, 0, true, "#fff")

    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def american_flagw14_1 (self, *args, **kwargs):
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
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    ctx.setTransform(1, 0, 0, -1,0,0)
    ctx.rotate(270*math.pi/180)
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w =380
    flag_h =200
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
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
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(24+24*i, 24+22*j, 5, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(12+24*i, 12+22*j, 5, 0, true, "#fff")

    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def american_flagw14_2 (self, *args, **kwargs):
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
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    ctx.setTransform(1, 0, 0, -1,0,0)
    ctx.rotate(270*math.pi/180)
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w =300
    flag_h =200
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
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
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(20+20*i, 20+20*j, 5, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(10+20*i, 10+20*j, 5, 0, true, "#fff")
    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    ctx.setTransform(1, 0, 0, -1,300,0)
    ctx.rotate(270*math.pi/180)
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
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
    @cherrypy.expose
    def american_flagw14_3 (self, *args, **kwargs):
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
    <canvas id="plotarea" width="800" height="800"></canvas>
    <script type="text/python">
    # 導入 doc
    from browser import doc
    import math

    # 準備繪圖畫布
    canvas = doc["plotarea"]
    ctx = canvas.getContext("2d")
    # 進行座標轉換, x 軸不變, y 軸反向且移動 canvas.height 單位光點
    ctx.setTransform(1, 0, 0, -1,550/2-190,550/2-100)
    ctx.rotate(315*math.pi/180)
    # ctx.setTransform(1, 0, 0, -1, 0, canvas.height)
    # 以下採用 canvas 原始座標繪圖
    flag_w =380
    flag_h =200
    circle_x = flag_w/4
    circle_y = flag_h/4
    # 先畫滿地紅
    ctx.fillStyle= '#fff'
    ctx.fillRect(0,0,flag_w,flag_h)
    #長條紅線
    ctx.fillRect(0,0,flag_w,flag_h/13)
    ctx.fillStyle= 'rgb(255, 0, 0)'
    for i in range(0,flag_h,2*flag_h/13):
        b=i
        ctx.fillRect(0,b,flag_w,flag_h/13)
        ctx.fillStyle= 'rgb(255, 0, 0)'
        ctx.fill()
    # 先畫滿青天
    ctx.fillStyle='rgb(0, 0, 150)'
    ctx.fillRect(0,0,2*flag_w/5,7*flag_h/13)
    #星星白色
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
    #star(100, 100, 50, 0, False, "#000")
    for i in range(5):
        for j in range(4):
            star(24+24*i, 24+22*j, 5, 0, true, "#fff")
    for i in range(6):
        for j in range(5):
            star(12+24*i, 12+22*j, 5, 0, true, "#fff")

    </script>
    </body>
    </html>
    '''
        return outstring