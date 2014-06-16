import cherrypy

# 這是 C2G1 類別的定義
class C2G5(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g5 分組程式開發網頁<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
老師示範<br />
<a href="fillpoly">c2g5 fillpoly 繪圖</a><br />
<a href="drawline">c2g5 drawline 繪圖</a><br />
<a href="animate1">c2g5 animate1 繪圖</a><br />
<a href="flag">c2g5 flag 繪圖</a><br />
<a href="square">c2g5 squared 繪圖</a><br />
<br />
第十二週任務<br />
<a href="triangle1">c2g5 triangle1 繪圖</a><br />
<a href="triangle2">c2g5 triangle2 繪圖</a><br />
<br />
第十三週任務<br />
<a href="JPflag">c2g5 JPflag 繪圖</a><br />
<br />
第十四週任務<br />
<a href="USAflag">c2g5 USAflag 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20%23%20%E5%B0%8E%E5%85%A5%20doc%0A%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%0A%20%20%20%20%23%20%E6%BA%96%E5%82%99%E7%B9%AA%E5%9C%96%E7%95%AB%E5%B8%83%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20%23%20%E9%80%B2%E8%A1%8C%E5%BA%A7%E6%A8%99%E8%BD%89%E6%8F%9B%2C%20x%20%E8%BB%B8%E4%B8%8D%E8%AE%8A%2C%20y%20%E8%BB%B8%E5%8F%8D%E5%90%91%E4%B8%94%E7%A7%BB%E5%8B%95%20canvas.height%20%E5%96%AE%E4%BD%8D%E5%85%89%E9%BB%9E%0A%20%20%20%20%23%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C%200%2C%20canvas.height)%0A%20%20%20%20%23%20%E4%BB%A5%E4%B8%8B%E6%8E%A1%E7%94%A8%20canvas%20%E5%8E%9F%E5%A7%8B%E5%BA%A7%E6%A8%99%E7%B9%AA%E5%9C%96%0A%20%20%20%20flag_w%20%3D%20180%0A%20%20%20%20flag_h%20%3D%20100%0A%20%20%20%20circle_x%20%3D%20flag_w%2F4%0A%20%20%20%20circle_y%20%3D%20flag_h%2F4%0A%20%20%20%20%23%20%E5%85%88%E7%95%AB%E6%BB%BF%E5%9C%B0%E7%B4%85%0A%20%20%20%20ctx.fillStyle%3D%20'%23fff'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%20%20%20%20%23%E9%95%B7%E6%A2%9D%E7%B4%85%E7%B7%9A%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20ctx.fillStyle%3D%20'rgb(255%2C%200%2C%200)'%0A%20%20%20%20for%20i%20in%20range(0%2Cflag_h%2C2*flag_h%2F13)%3A%0A%20%20%20%20%20%20%20%20b%3Di%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2Cb%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20%20%20%20%20ctx.fillStyle%3D%20'rgb(255%2C%200%2C%200)'%0A%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20%23%20%E5%85%88%E7%95%AB%E6%BB%BF%E9%9D%92%E5%A4%A9%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2C2*flag_w%2F5%2C7*flag_h%2F13)%0A%20%20%20%20%23%E6%98%9F%E6%98%9F%E7%99%BD%E8%89%B2%0A%20%20%20%20def%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20%20%20%20%20ctx.strokeStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20ctx.stroke()%0A%20%20%20%20%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22%23f00%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%A9%BA%E5%BF%83%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout%2C%20yout%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%95%AB%E7%A9%BA%E5%BF%83%E4%BA%94%E8%8A%92%E6%98%9F%2C%20%E7%84%A1%E9%97%9C%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%2C%20%E8%8B%A5%E5%AF%A6%E5%BF%83%E5%89%87%E8%88%87%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%E6%9C%89%E9%97%9C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout2%2C%20yout2%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20%23star(100%2C%20100%2C%2050%2C%200%2C%20False%2C%20%22%23000%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(12%2B12*i%2C%2012%2B10*j%2C%203%2C%200%2C%20true%2C%20%22%23fff%22)%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(6%2B12*i%2C%206%2B10*j%2C%203%2C%200%2C%20true%2C%20%22%23fff%22)&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g5 機器人-USA 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20%23%20%E5%B0%8E%E5%85%A5%20doc%0A%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%0A%20%20%20%20%23%20%E6%BA%96%E5%82%99%E7%B9%AA%E5%9C%96%E7%95%AB%E5%B8%83%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20ctx.setTransform(1%2C%201%2C%20-1%2C%201%2C%20150%2C%20100)%0A%20%20%20%20%23%20%E9%80%B2%E8%A1%8C%E5%BA%A7%E6%A8%99%E8%BD%89%E6%8F%9B%2C%20x%20%E8%BB%B8%E4%B8%8D%E8%AE%8A%2C%20y%20%E8%BB%B8%E5%8F%8D%E5%90%91%E4%B8%94%E7%A7%BB%E5%8B%95%20canvas.height%20%E5%96%AE%E4%BD%8D%E5%85%89%E9%BB%9E%0A%20%20%20%20%23%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C%200%2C%20canvas.height)%0A%20%20%20%20%23%20%E4%BB%A5%E4%B8%8B%E6%8E%A1%E7%94%A8%20canvas%20%E5%8E%9F%E5%A7%8B%E5%BA%A7%E6%A8%99%E7%B9%AA%E5%9C%96%0A%20%20%20%20flag_w%20%3D%20180%0A%20%20%20%20flag_h%20%3D%20100%0A%20%20%20%20circle_x%20%3D%20flag_w%2F4%0A%20%20%20%20circle_y%20%3D%20flag_h%2F4%0A%20%20%20%20%23%20%E5%85%88%E7%95%AB%E6%BB%BF%E5%9C%B0%E7%B4%85%0A%20%20%20%20ctx.fillStyle%3D%20'%23fff'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%20%20%20%20%23%E9%95%B7%E6%A2%9D%E7%B4%85%E7%B7%9A%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20ctx.fillStyle%3D%20'rgb(255%2C%200%2C%200)'%0A%20%20%20%20for%20i%20in%20range(0%2Cflag_h%2C2*flag_h%2F13)%3A%0A%20%20%20%20%20%20%20%20b%3Di%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2Cb%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20%20%20%20%20ctx.fillStyle%3D%20'rgb(255%2C%200%2C%200)'%0A%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20%23%20%E5%85%88%E7%95%AB%E6%BB%BF%E9%9D%92%E5%A4%A9%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2C2*flag_w%2F5%2C7*flag_h%2F13)%0A%20%20%20%20%23%E6%98%9F%E6%98%9F%E7%99%BD%E8%89%B2%0A%20%20%20%20def%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20%20%20%20%20ctx.strokeStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20ctx.stroke()%0A%20%20%20%20%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22%23f00%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%A9%BA%E5%BF%83%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout%2C%20yout%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%95%AB%E7%A9%BA%E5%BF%83%E4%BA%94%E8%8A%92%E6%98%9F%2C%20%E7%84%A1%E9%97%9C%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%2C%20%E8%8B%A5%E5%AF%A6%E5%BF%83%E5%89%87%E8%88%87%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%E6%9C%89%E9%97%9C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout2%2C%20yout2%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20%23star(100%2C%20100%2C%2050%2C%200%2C%20False%2C%20%22%23000%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(12%2B12*i%2C%2012%2B10*j%2C%203%2C%200%2C%20true%2C%20%22%23fff%22)%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(6%2B12*i%2C%206%2B10*j%2C%203%2C%200%2C%20true%2C%20%22%23fff%22)&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g5 機器人-USA-轉 繪圖</a><br />
<br />
第十五週任務<br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A1%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A1%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A0%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0Adef%20jump_over_hurdle()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%0Amove()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g5 Robot跨越Hurdles1</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A11%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%2C%223%2C1%22%3A%5B%22east%22%5D%2C%227%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=def%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)%0Adef%20jump_over_hurdle()%3A%0A%20%20%20%20turn_left()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_right()%0A%20%20%20%20move()%0A%20%20%20%20turn_left()%0A%0Amove()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Ajump_over_hurdle()%0Amove()%0Ajump_over_hurdle()%0Amove()%0A&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g5 Robot跨越Hurdles3</a><br />
<a href="http://www.facebook.com/l.php?u=http%3A%2F%2F2014c2-mdenfu.rhcloud.com%2Fstatic%2Freeborg%2Fworld.html%3Fproglang%3Dpython-en%26world%3D%257B%2522robots%2522%253A%255B%257B%2522x%2522%253A1%252C%2522y%2522%253A1%252C%2522tokens%2522%253A%2522infinite%2522%252C%2522orientation%2522%253A0%252C%2522_prev_x%2522%253A1%252C%2522_prev_y%2522%253A1%252C%2522_prev_orientation%2522%253A0%257D%255D%252C%2522walls%2522%253A%257B%25222%252C1%2522%253A%255B%2522east%2522%255D%252C%25224%252C1%2522%253A%255B%2522east%2522%255D%252C%25226%252C1%2522%253A%255B%2522east%2522%255D%252C%25228%252C1%2522%253A%255B%2522east%2522%255D%252C%252210%252C1%2522%253A%255B%2522east%2522%255D%252C%252212%252C1%2522%253A%255B%2522east%2522%255D%252C%25223%252C1%2522%253A%255B%2522east%2522%255D%252C%25227%252C1%2522%253A%255B%2522east%2522%255D%257D%252C%2522goal%2522%253A%257B%2522position%2522%253A%257B%2522x%2522%253A12%252C%2522y%2522%253A1%257D%257D%257D%26editor%3Ddef%2520turn_right()%253A%250A%2520%2520%2520%2520repeat(turn_left%252C%25203)%250A%250Adef%2520jump_over_hurdle()%253A%250A%2520%2520%2520%2520turn_left()%250A%2520%2520%2520%2520move()%250A%2520%2520%2520%2520turn_right()%250A%2520%2520%2520%2520move()%250A%2520%2520%2520%2520turn_right()%250A%2520%2520%2520%2520move()%250A%2520%2520%2520%2520turn_left()%250A%2520%2520%2520%2520%250A%2520%250Amove()%250Ajump_over_hurdle()%250Ajump_over_hurdle()%250Ajump_over_hurdle()%250Amove()%250Ajump_over_hurdle()%250Ajump_over_hurdle()%250Ajump_over_hurdle()%250Amove()%250Ajump_over_hurdle()%250Amove()%26library%3D%2523%2520%2527import%2520my_lib%2527%2520in%2520Python%2520Code%2520is%2520required%2520to%2520use%250A%2523%2520the%2520code%2520in%2520this%2520library.%2520%250A%250A&h=iAQHcqml0">c2g5 Robot同時跨越Hurdles1.Hurdles3</a><br />
'''
        return outstring

    # 以下為 c2g1 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫
    
    import programs.c2g1 as c2g1
    root.c2g1 = c2g1.C2G1()
    
    則程式啟動後, 可以利用 /c2g1/fillpoly 呼叫函式執行
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
    ctx.setTransform(1, 0, 0, -1, 0, 800)

    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()
    def square(x, y ,width):
        draw_line(300, 300, 500, 300)
        draw_line(500, 300, 500, 500)
        draw_line(500, 500, 300, 500)
        draw_line(300, 500, 300, 300)
    square(400,400,200)
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
    draw_line(150, 250, 400, 400)
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

    draw_line(100, 100, 150, 250)
    draw_line(150, 250, 400, 400)
    draw_line(400, 400, 100, 100)
  
    </script>
    </body>
    </html>
    '''
        return outstring
    @cherrypy.expose
    def JPflag(self, *args, **kwargs):
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
    ctx.setTransform(1, 0, 0, -1, 0, canvas.height)

    flag_w = canvas.width
    flag_h = canvas.height
    circle_x = flag_w/2
    circle_y = flag_h/2
    
    # 定義畫線函式
    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(0, 0, 300, 0)
    draw_line(300, 0, 300, 200)
    draw_line(300, 200, 0, 200)
    draw_line(0, 200, 0, 0)  

    ctx.beginPath()
    #ctx.arc(circle_x, circle_y, flag_h*0.6, 0, pi*2, true)
    ctx.arc(circle_x, circle_y, 60, 0, pi*2)
    ctx.closePath()
    # 填色設為紅色
    ctx.fillStyle = 'rgb(255, 0, 0)'
    ctx.fill()

    def draw_line(x1, y1, x2, y2, linethick = 3, color = "blue"):
        ctx.beginPath()
        ctx.lineWidth = linethick
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = color
        ctx.stroke()

    draw_line(0, 0, 300, 0)
    draw_line(300, 0, 300, 200)
    draw_line(300, 200, 0, 200)
    draw_line(0, 200, 0, 0)  

    ctx.beginPath()
    #ctx.arc(circle_x, circle_y, flag_h*0.6, 0, pi*2, true)
    ctx.arc(circle_x, circle_y, 60, 0, pi*2)
    ctx.closePath()
    # 填色設為紅色
    ctx.fillStyle = 'rgb(255, 0, 0)'
    ctx.fill()
    
    </script>
    </body>
    </html>
    '''
        return outstring

    @cherrypy.expose
    def USAflag (self, *args, **kwargs):
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