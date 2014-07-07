import cherrypy

# 這是 C2G4 類別的定義
class C2G4(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g4 分組程式開發網頁, 以下為 W12 的任務執行內容.<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="fillpoly">c2g4 fillpoly 繪圖</a><br />
<a href="drawline">c2g4 drawline 繪圖</a><br />
<a href="drawsqure">c2g4 drawsqure 繪圖</a><br />
<a href="triangle1">c2g4 triangle1繪圖</a><br />
<a href="triangle2">c2g4 triangle2繪圖</a><br />
<a href="flag1">c2g4 flag1繪圖</a><br />
<a href="flag2">c2g4 flag2繪圖</a><br />
<a href="USAflag">c2g4 USAflag繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%2C%22large_world%22%3Afalse%7D&editor=from%20browser%20import%20html%2C%20doc%0A%23%20use%20plotarea%20as%20canvas%0A%23%E7%BE%8E%E5%9C%8B%E5%9C%8B%E6%97%97%0Acanvas%20%3D%20doc%5B%22background_canvas%22%5D%0Actx%20%3D%20canvas.getContext(%222d%22)%0Actx.setTransform(1%2C%200%2C%200%2C1%2C270%20%2C%2010)%0A%23%20%E6%BA%96%E5%82%99%E5%9C%A8%20canvas%20%E4%B8%AD%E7%B9%AA%E5%9C%96%0A%23%20%E5%B0%8E%E5%85%A5%20doc%0Afrom%20browser%20import%20doc%0Aimport%20math%0A%23%20%E5%AE%9A%E7%BE%A9%E7%95%AB%E7%B7%9A%E5%87%BD%E5%BC%8F%0Actx.rotate(90*math.pi%2F180)%0Adef%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20ctx.strokeStyle%20%3Dblack%0A%20%20%20%20ctx.stroke()%0A%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0Adef%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22white%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20'white'%0A%20%20%20%20%20%20%20%20ctx.fill()%0A%0Afor%20i%20in%20range(7)%3A%0A%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20ctx.fillRect(0%2C%200%2B40*i%2C%20390%2C%2020)%0A%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20149)'%0A%20%20%20%20ctx.fillRect(0%2C%20120%2C%20210%2C%20140)%0A%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B34*i%2C%20134%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(36%2B34*i%2C%20148%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%0A%0A%0AdataURL%20%3D%20canvas.toDataURL()%0Adoc%5B'canvas_image'%5D.src%20%3D%20dataURL&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g4 week14_1繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%2C%22large_world%22%3Afalse%7D&editor=from%20browser%20import%20html%2C%20doc%0A%23%20use%20plotarea%20as%20canvas%0Acanvas%20%3D%20doc%5B%22background_canvas%22%5D%0Actx%20%3D%20canvas.getContext(%222d%22)%0A%0A%23%20%E6%BA%96%E5%82%99%E5%9C%A8%20canvas%20%E4%B8%AD%E7%B9%AA%E5%9C%96%0Actx.setTransform(1%2C%200%2C%200%2C%201%2C%20600%2C%20100)%0A%0A%23%20%E5%B0%8E%E5%85%A5%20doc%0Afrom%20browser%20import%20doc%0Aimport%20math%0A%23%20%E4%BB%A5%E4%B8%8B%E6%8E%A1%E7%94%A8%20canvas%20%E5%8E%9F%E5%A7%8B%E5%BA%A7%E6%A8%99%E7%B9%AA%E5%9C%96%0Actx.rotate(90*math.pi%2F180)%0Aflag_w%20%3D%20300%0Aflag_h%20%3D%20200%0Acircle_x%20%3D%20flag_w%2F4%0Acircle_y%20%3D%20flag_h%2F4%0A%23%20%E5%85%88%E7%95%AB%E6%BB%BF%E5%9C%B0%E7%B4%85%0Actx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0Actx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%23%20%E5%86%8D%E7%95%AB%E9%9D%92%E5%A4%A9%0Actx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0Actx.fillRect(0%2C0%2Cflag_w%2F2%2Cflag_h%2F2)%0A%23%20%E7%95%AB%E5%8D%81%E4%BA%8C%E5%88%B0%E5%85%89%E8%8A%92%E7%99%BD%E6%97%A5%0Actx.beginPath()%0Astar_radius%20%3D%20flag_w%2F8%0Aangle%20%3D%200%0Afor%20i%20in%20range(24)%3A%0A%20%20%20%20angle%20%2B%3D%205*math.pi*2%2F12%0A%20%20%20%20toX%20%3D%20circle_x%20%2B%20math.cos(angle)*star_radius%0A%20%20%20%20toY%20%3D%20circle_y%20%2B%20math.sin(angle)*star_radius%0A%20%20%20%20%23%20%E5%8F%AA%E6%9C%89%20i%20%E7%82%BA%200%20%E6%99%82%E7%A7%BB%E5%8B%95%E5%88%B0%20toX%2C%20toY%2C%20%E5%85%B6%E9%A4%98%E9%83%BD%E9%80%B2%E8%A1%8C%20lineTo%0A%20%20%20%20if%20(i)%3A%0A%20%20%20%20%20%20%20%20ctx.lineTo(toX%2C%20toY)%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20ctx.moveTo(toX%2C%20toY)%0A%23%20%E5%B0%87%E5%A1%AB%E8%89%B2%E8%A8%AD%E7%82%BA%E7%99%BD%E8%89%B2%0Actx.fillStyle%20%3D%20'%23fff'%0Actx.fill()%0A%23%20%E7%99%BD%E6%97%A5%3A%E8%97%8D%E5%9C%88%0Actx.beginPath()%0A%23%20%E6%9F%A5%E8%A9%A2%20canvas%20arc%20%E5%A6%82%E4%BD%95%E5%AE%9A%E7%BE%A9%0Actx.arc(circle_x%2C%20circle_y%2C%20flag_w*17%2F240%2C%200%2C%20math.pi*2%2C%20true)%0Actx.closePath()%0A%23%20%E5%A1%AB%E8%89%B2%E8%A8%AD%E7%82%BA%E8%97%8D%E8%89%B2%0Actx.fillStyle%20%3D%20'rgb(0%2C%200%2C%20149)'%0Actx.fill()%0A%23%20%E7%99%BD%E6%97%A5%3A%E7%99%BD%E5%BF%83%0Actx.beginPath()%0Actx.arc(circle_x%2C%20circle_y%2C%20flag_w%2F16%2C%200%2C%20math.pi*2%2C%20true)%0Actx.closePath()%0A%23%20%E5%A1%AB%E8%89%B2%E8%A8%AD%E7%82%BA%E7%99%BD%E8%89%B2%0Actx.fillStyle%20%3D%20'%23fff'%0Actx.fill()%0A%0A%23%E7%BE%8E%E5%9C%8B%E5%9C%8B%E6%97%97%0Acanvas%20%3D%20doc%5B%22background_canvas%22%5D%0Actx%20%3D%20canvas.getContext(%222d%22)%0Actx.setTransform(1%2C%200%2C%200%2C1%2C270%20%2C%2010)%0A%23%20%E6%BA%96%E5%82%99%E5%9C%A8%20canvas%20%E4%B8%AD%E7%B9%AA%E5%9C%96%0A%23%20%E5%B0%8E%E5%85%A5%20doc%0Afrom%20browser%20import%20doc%0Aimport%20math%0A%23%20%E5%AE%9A%E7%BE%A9%E7%95%AB%E7%B7%9A%E5%87%BD%E5%BC%8F%0Actx.rotate(90*math.pi%2F180)%0Adef%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20ctx.strokeStyle%20%3Dblack%0A%20%20%20%20ctx.stroke()%0A%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0Adef%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22white%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20'white'%0A%20%20%20%20%20%20%20%20ctx.fill()%0A%0Afor%20i%20in%20range(7)%3A%0A%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20ctx.fillRect(0%2C%200%2B40*i%2C%20390%2C%2020)%0A%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20149)'%0A%20%20%20%20ctx.fillRect(0%2C%20120%2C%20210%2C%20140)%0A%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B34*i%2C%20134%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(36%2B34*i%2C%20148%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%0A%0A%0AdataURL%20%3D%20canvas.toDataURL()%0Adoc%5B'canvas_image'%5D.src%20%3D%20dataURL&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g4 week14_2繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=from%20browser%20import%20html%2C%20doc%0A%23%20use%20plotarea%20as%20canvas%0Acanvas%20%3D%20doc%5B%22background_canvas%22%5D%0Actx%20%3D%20canvas.getContext(%222d%22)%0Actx.setTransform(1%2C%200%2C%200%2C%20-1%2C%2080%2C%20200)%0A%23%20%E6%BA%96%E5%82%99%E5%9C%A8%20canvas%20%E4%B8%AD%E7%B9%AA%E5%9C%96%0A%23%20%E5%B0%8E%E5%85%A5%20doc%0Afrom%20browser%20import%20doc%0Aimport%20math%0A%23%20%E5%AE%9A%E7%BE%A9%E7%95%AB%E7%B7%9A%E5%87%BD%E5%BC%8F%0Actx.rotate(315*math.pi%2F180)%0Adef%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20ctx.strokeStyle%20%3Dblack%0A%20%20%20%20ctx.stroke()%0A%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0Adef%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22white%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20'white'%0A%20%20%20%20%20%20%20%20ctx.fill()%0A%0Afor%20i%20in%20range(7)%3A%0A%20%20%20%20ctx.fillStyle%3D'%23B22234'%0A%20%20%20%20ctx.fillRect(0%2C%200%2B40*i%2C%20470%2C%2020)%0A%0A%20%20%20%20ctx.fillStyle%3D'%233C3B6E'%0A%20%20%20%20ctx.fillRect(0%2C%20120%2C%20210%2C%20140)%0A%20%20%20%20%0A%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B34*i%2C%20134%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(36%2B34*i%2C%20148%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0AdataURL%20%3D%20canvas.toDataURL()%0Adoc%5B'canvas_image'%5D.src%20%3D%20dataURL&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g4 week14_3繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0A%20%0A%23%20%E5%88%A9%E7%94%A8%E5%B7%A6%E5%8F%B3%E8%BD%89%E8%88%87%E5%89%8D%E9%80%B2%E5%AE%9A%E7%BE%A9%E8%B7%A8%E6%AC%84%E5%8B%95%E4%BD%9C%0Adef%20jump_over_hurdle()%3A%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_left()%0A%0A%20%20%20%20move()%0A%20%20%20%20at_goal()%0A%23%20%E5%91%BC%E5%8F%AB%E8%B7%A8%E6%AC%84%E8%88%87%E5%89%8D%E9%80%B2%E5%87%BD%E5%BC%8F%0Ajump_over_hurdle()%0A%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0A%0A">c2g4 week15_1繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0Adef%20turn_back()%3A%0A%20%20%20%20repeat(turn_left%2C%202)%0A%23%20%E5%88%A9%E7%94%A8%E5%B7%A6%E5%8F%B3%E8%BD%89%E8%88%87%E5%89%8D%E9%80%B2%E5%AE%9A%E7%BE%A9%E8%B7%A8%E6%AC%84%E5%8B%95%E4%BD%9C%0Adef%20jump_over_hurdle()%3A%0A%20%20%20%20for%20i%20in%20range(2)%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(2)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20%20%20%20%20turn_back()%0A%20%20%20%20%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20turn_left()%20%20%20%20%20%20%20%20%0Adef%20jump_over_hurdle2()%3A%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%20%20%20%20%20%20%20%20%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20at_goal()%20%20%20%0A%23%20%E5%91%BC%E5%8F%AB%E8%B7%A8%E6%AC%84%E8%88%87%E5%89%8D%E9%80%B2%E5%87%BD%E5%BC%8F%0Ajump_over_hurdle()%0Ajump_over_hurdle2()%0A%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0A%0A">c2g4 week15_2繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A6%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A6%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0A%0A%23%20%E8%B7%AF%E5%BE%91%E8%A6%8F%E5%8A%83%E7%9B%B4%E5%88%B0%E5%88%B0%E9%81%94%E7%9B%AE%E7%9A%84%E5%9C%B0%E7%82%BA%E6%AD%A2%0Awhile%20(at_goal()%20%3D%3D%20False)%3A%0A%20%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%8F%B3%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%2C%20%E5%8F%B3%E8%BD%89%E4%B8%80%E6%AD%A5%0A%20%20%20%20if%20(right_is_clear()%20%3D%3D%20True)%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A4%E6%96%B7%E5%89%8D%E6%96%B9%E6%B2%92%E6%9C%89%E9%9A%9C%E7%A4%99%E7%89%A9%2C%20%E5%89%8D%E9%80%B2%E4%B8%80%E6%AD%A5%0A%20%20%20%20%20%20%20%20if%20(front_is_clear()%20%3D%3D%20True)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20move()%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E4%B8%8D%E8%83%BD%E5%8F%B3%E8%BD%89%2C%20%E4%B8%8D%E8%83%BD%E5%89%8D%E9%80%B2%2C%20%E5%89%87%E5%B7%A6%E8%BD%89%0A%20%20%20%20%20%20%20%20%20%20%20%20turn_left()%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%23%E6%AF%94%E7%85%A7%E7%AC%AC19%E7%B5%84%E5%AD%B8%E9%95%B7%E7%9A%84%0A%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g4 week15_3繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A11%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%2C%223%2C2%22%3A%5B%22east%22%5D%2C%226%2C2%22%3A%5B%22east%22%5D%2C%227%2C2%22%3A%5B%22east%22%5D%2C%227%2C3%22%3A%5B%22east%22%5D%2C%2210%2C2%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn_left()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g4 week16_1+2繪圖</a><br />
<a href="https://copy.com/JDxVHpB2hVcw">c2g4 week17+18report</a><br />
'''
        return outstring

    # 以下為 c2g4 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫
    
    import programs.c2g4 as c2g4
    root.c2g4 = c2g4.C2G4()
    
    則程式啟動後, 可以利用 /c2g4/fillpoly 呼叫函式執行
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
    
    import programs.c2g1 as c2g1
    root.c2g1 = c2g1.C2G1()
    
    則程式啟動後, 可以利用 /c2g1/drawline 呼叫函式執行
    
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
        
    @cherrypy.expose
    def drawsqure(self, *args, **kwargs):
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
    def drawsqure(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
        
    drawsqure(300, 300, 500, 300)
    drawsqure(500, 300, 500, 500)
    drawsqure(500, 500, 300, 500)
    drawsqure(300, 500, 300, 300)
    </script>
    </body>
    </html>
    '''
        return outstring


    @cherrypy.expose
    def triangle1(self, *args, **kwargs):
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
        
    # 定義畫線函式, angle 旋轉角,  solid 空心或實心,  color 顏色
    def draw_line(x1, y1, x2, y2,angle=0,solid=False ,linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
            
  
    draw_line(100, 100, 150,250 )
    draw_line(150, 250, 400, 400 )
    draw_line(400,400, 100, 100)   
    
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
        
    # 定義畫線函式, angle 旋轉角,  solid 空心或實心,  color 顏色
    def draw_line(x1, y1, x2, y2,angle=0,solid=False ,linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
    def full():
        ctx.beginPath()
        ctx.moveTo(100,100)
        ctx.lineTo(150,250)
        ctx.lineTo(400,400)
        ctx.lineTo(100,100)
        ctx.fill()
        
    ctx.fillStyle = "red"
    full()
    
  
    draw_line(100, 100, 150,250 )
    draw_line(150, 250, 400, 400 )
    draw_line(400,400, 100, 100)       
    
    </script>
    </body>
    </html>
    '''
        return outstring
        

        
    @cherrypy.expose
    def flag1(self, *args, **kwargs):
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
    math.pi
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
    
    ctx.moveTo(0,0 )
    ctx.lineTo(300, 0)
    ctx.lineTo(300, 200)
    ctx.lineTo(0,200 )
    ctx.lineTo(0, 0)
    ctx.stroke()

    ctx.beginPath();
    ctx.arc(150,100,50,0,2*math.pi);
    ctx.fillStyle = 'rgb(255, 0, 0)'
   
    ctx.fill()
    ctx.stroke();

    </script>
    </body>
    </html>
    '''
        return outstring
        

    @cherrypy.expose
    def flag2(self, *args, **kwargs):
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
    if 10+450.0< canvas.width and         150+300< canvas.width:
        japan_flag(10, 150, 300)
    else:
        # 畫出最大面的國旗
        japan_flag(10, 10, 790*2/3)
    </script>
    </body>
    </html>
    '''
        return outstring
                
    
    
    @cherrypy.expose
    def USAflag(self, *args, **kwargs):
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
        ctx.strokeStyle =black
        ctx.stroke()

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
                
        
