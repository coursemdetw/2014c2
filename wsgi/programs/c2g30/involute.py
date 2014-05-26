#@+leo-ver=5-thin
#@+node:2014spring.20140520155021.4813: * @file involute.py
#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:2014spring.20140520155021.4814: ** <<declarations>> (involute)
import cherrypy
#@-<<declarations>>
#@+others
#@+node:2014spring.20140520155021.4815: ** class INVOLUTE
# 這是 INVOLUTE 類別的定義
class INVOLUTE(object):
    # 各組利用 index 引導隨後的程式執行
    #@+others
    #@+node:2014spring.20140520155021.4816: *3* index
    @cherrypy.expose
    def index(self, *args, **kwargs):
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

    # 進行座標轉換, x 軸不變, y 軸反向且移動 800 光點
    #ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    def draw_circle(x, y, r, linethick=1, color="black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.arc(x, y, r, 0, pi*2, true)
        ctx.closePath()
        ctx.strokeStyle = color
        ctx.stroke()

    def gear(midx, midy, rp, n, linethick=1, color="black"):
        deg = pi/180
        # 齒輪漸開線分成 15 線段繪製
        imax = 15
        # 在輸入的畫布上繪製直線, 由圓心到節圓 y 軸頂點畫一直線
        draw_line(midx, midy, midx, midy-rp, linethick, color)
        # 畫出 rp 圓
        #draw_circle(midx, midy, rp)
        # a 為模數 (代表公制中齒的大小), 模數為節圓直徑(稱為節徑)除以齒數
        # 模數也就是齒冠大小
        a = 2*rp/n
        # d 為齒根大小, 為模數的 1.157 或 1.25倍, 這裡採 1.25 倍
        d = 2.5*rp/n
        # ra 為齒輪的外圍半徑
        ra = rp + a
        # 畫出 ra 圓
        #draw_circle(midx, midy, ra)
        # rb 則為齒輪的基圓半徑
        # 基圓為漸開線長齒之基準圓
        rb = rp*cos(20*deg)
        # 畫出 rb 圓 (基圓)
        #draw_circle(midx, midy, rb)
        # rd 為齒根圓半徑
        rd = rp - d
        # 畫出 rd 圓 (齒根圓)
        #draw_circle(midx, midy, rd)
        # 在 100, 100 列出各圓半徑
        ctx.strokeText(round(ra,1), 50, midy)
        ctx.strokeText(round(rp,1), 50, midy+30)
        ctx.strokeText(str(round(rb,1)), 50, midy+60)
        ctx.strokeText(str(round(rd,1)), 50, midy+90)
        # 當齒數大於 齒時, rd 將會大於 rb
        # dr 則為基圓到齒頂圓半徑分成 imax 段後的每段半徑增量大小
        # 將圓弧分成 imax 段來繪製漸開線
        dr = (ra-rb)/imax
        # tan(20*deg)-20*deg 為漸開線函數
        sigma = pi/(2*n) + tan(20*deg) - 20*deg
     
        for j in range(n):
            ang = -2.*j*pi/n + sigma
            ang2 = 2.*j*pi/n + sigma
            lxd = midx + rd*sin(ang2-2.*pi/n)
            lyd = midy - rd*cos(ang2-2.*pi/n)
            for i in range(imax+1):
                r = rb + i*dr
                theta = sqrt((r*r)/(rb*rb)-1.)
                alpha = theta-atan(theta)
                xpt = r*sin(alpha-ang)
                ypt = r*cos(alpha-ang)
                xd = rd*sin(-ang)
                yd = rd*cos(-ang)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由左側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                # 若 rd > rb 時, 則 rd 以內的漸開線不用畫
                if r > rd:
                    draw_line(midx+xpt, midy-ypt, last_x, last_y, linethick, color)
                # 最後一點, 則為齒頂圓
                if(i==imax):
                    lfx=midx+xpt
                    lfy=midy-ypt
                last_x = midx+xpt
                last_y = midy-ypt
            # lxd 為齒根圓上的左側 x 座標, lyd 則為 y 座標
            # 下列為齒根圓上用來近似圓弧的直線
            # 當 rd > rb 時, 此線段必須配合從 rb 來計算偏角, 也就是會變短
            draw_line(lxd, lyd, midx + xd, midy - yd, linethick, "blue")
            for i in range(imax+1):
                r = rb + i*dr
                theta = sqrt((r*r)/(rb*rb)-1.)
                alpha = theta-atan(theta)
                xpt = r*sin(ang2-alpha)
                ypt = r*cos(ang2-alpha)
                xd = rd*sin(ang2)
                yd = rd*cos(ang2)
                # i=0 時, 繪線起點由齒根圓上的點, 作為起點
                if(i==0):
                    last_x = midx+xd
                    last_y = midy-yd
                # 由右側齒根圓作為起點, 除第一點 (xd,yd) 齒根圓上的起點外, 其餘的 (xpt,ypt)則為漸開線上的分段點
                if r > rd:
                    draw_line(midx+xpt, midy-ypt, last_x, last_y, linethick, color)
                # 最後一點, 則為齒頂圓
                if(i == imax):
                    rfx = midx + xpt
                    rfy = midy - ypt
                last_x = midx + xpt
                last_y = midy - ypt
            # lfx 為齒頂圓上的左側 x 座標, lfy 則為 y 座標
            # 下列為齒頂圓上用來近似圓弧的直線
            draw_line(lfx, lfy, rfx, rfy, linethick, color)
    gear(500, 400, 400, 250, linethick=1, color="black")
    gear(400, 400, 50, 18, linethick=1, color="blue")
    gear(150, 300, 50, 90, linethick=1, color="red")
    </script>
    </body>
    </html>
'''
        return outstring
    #@-others
#@-others
#@-leo
