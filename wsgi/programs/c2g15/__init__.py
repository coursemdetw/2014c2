import cherrypy

# 這是 C2G15 類別的定義
class C2G15(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014C2 協同專案下的 c2g15 分組程式開發網頁, 以下為 W12 的任務執行內容.<br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="fillpoly">c2g15 fillpoly 繪圖</a><br />
<a href="drawline">c2g15 drawline 繪圖</a><br />
<a href="drawsquare">c2g15 drawsquare 繪圖</a><br />
<a href="drawstar">c2g15 drawstar 繪圖</a><br />
<a href=" triangle">c2g15 triangle 繪圖</a><br />
<a href=" triangle2">c2g15 triangle2 繪圖</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%20%20%20%20%23%20%E6%BA%96%E5%82%99%E7%B9%AA%E5%9C%96%E7%95%AB%E5%B8%83%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20%23%20%E9%80%B2%E8%A1%8C%E5%BA%A7%E6%A8%99%E8%BD%89%E6%8F%9B%2C%20x%20%E8%BB%B8%E4%B8%8D%E8%AE%8A%2C%20y%20%E8%BB%B8%E5%8F%8D%E5%90%91%E4%B8%94%E7%A7%BB%E5%8B%95%20canvas.height%20%E5%96%AE%E4%BD%8D%E5%85%89%E9%BB%9E%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C%20-400%2C%200)%0A%20%20%20%20ctx.rotate(270*math.pi%2F180)%0A%20%20%20%20%23%20%E4%BB%A5%E4%B8%8B%E6%8E%A1%E7%94%A8%20canvas%20%E5%8E%9F%E5%A7%8B%E5%BA%A7%E6%A8%99%E7%B9%AA%E5%9C%96%0A%20%20%20%20flag_w%20%3D%20300%0A%20%20%20%20flag_h%20%3D%20%20200%0A%20%20%20%20for%20i%20in%20range(7)%3A%0A%20%20%20%20%20%20%20%20%23%E7%95%AB%E7%B4%85%E6%A2%9D%0A%20%20%20%20%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2C400%2Bi*2*flag_h%2F13%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%E8%A8%AD%E7%82%BA%E8%97%8D%E8%89%B2%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C400%2Cflag_w%2F2-5%2Cflag_h*0.5385)%0A%20%20%20%20%23%20%E5%AE%9A%E7%BE%A9%E7%95%AB%E7%B7%9A%E5%87%BD%E5%BC%8F%0A%20%20%20%20def%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20%20%20%20%20ctx.strokeStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20ctx.stroke()%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22%23f00%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%A9%BA%E5%BF%83%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout%2C%20yout%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%95%AB%E7%A9%BA%E5%BF%83%E4%BA%94%E8%8A%92%E6%98%9F%2C%20%E7%84%A1%E9%97%9C%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%2C%20%E8%8B%A5%E5%AF%A6%E5%BF%83%E5%89%87%E8%88%87%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%E6%9C%89%E9%97%9C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout2%2C%20yout2%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(10%2B24*i%2C%20405%2B24*j%2C%206%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(18.5%2B25.5*i%2C%20414.5%2B25.5*j%2C%206%2C%200%2C%20True%2C%20%22white%22)&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g15_A 繪圖</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%20%20%20%20%23%20%E6%BA%96%E5%82%99%E7%B9%AA%E5%9C%96%E7%95%AB%E5%B8%83%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20%23%20%E9%80%B2%E8%A1%8C%E5%BA%A7%E6%A8%99%E8%BD%89%E6%8F%9B%2C%20x%20%E8%BB%B8%E4%B8%8D%E8%AE%8A%2C%20y%20%E8%BB%B8%E5%8F%8D%E5%90%91%E4%B8%94%E7%A7%BB%E5%8B%95%20canvas.height%20%E5%96%AE%E4%BD%8D%E5%85%89%E9%BB%9E%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%201%2C%20250%2C%20100)%0A%20%20%20%20ctx.rotate(45*math.pi%2F180)%0A%20%20%20%20%23%20%E4%BB%A5%E4%B8%8B%E6%8E%A1%E7%94%A8%20canvas%20%E5%8E%9F%E5%A7%8B%E5%BA%A7%E6%A8%99%E7%B9%AA%E5%9C%96%0A%20%20%20%20flag_w%20%3D%20300%0A%20%20%20%20flag_h%20%3D%20200%0A%20%20%20%20for%20i%20in%20range(7)%3A%0A%20%20%20%20%20%20%20%20%23%E7%95%AB%E7%B4%85%E6%A2%9D%0A%20%20%20%20%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2C0%2Bi*2*flag_h%2F13%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%E8%A8%AD%E7%82%BA%E8%97%8D%E8%89%B2%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2F2-5%2Cflag_h*0.5385)%0A%20%20%20%20%23%20%E5%AE%9A%E7%BE%A9%E7%95%AB%E7%B7%9A%E5%87%BD%E5%BC%8F%0A%20%20%20%20def%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20%20%20%20%20ctx.strokeStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20ctx.stroke()%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22%23f00%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%A9%BA%E5%BF%83%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout%2C%20yout%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E7%95%AB%E7%A9%BA%E5%BF%83%E4%BA%94%E8%8A%92%E6%98%9F%2C%20%E7%84%A1%E9%97%9C%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%2C%20%E8%8B%A5%E5%AF%A6%E5%BF%83%E5%89%87%E8%88%87%E7%95%AB%E7%B7%9A%E6%AC%A1%E5%BA%8F%E6%9C%89%E9%97%9C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout2%2C%20yout2%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(10%2B24*i%2C%206%2B24*j%2C%206%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(18.5%2B25.5*i%2C%2015.5%2B25.5*j%2C%206%2C%200%2C%20True%2C%20%22white%22)&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g15_A_45  繪圖</a><br />
<a href=" http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C0%2C0)%0A%20%20%20%20ctx.rotate(270*math.pi%2F180)%0A%20%20%20%20flag_w%20%3D300%0A%20%20%20%20flag_h%20%3D200%0A%20%20%20%20circle_x%20%3D%20flag_w%2F4%0A%20%20%20%20circle_y%20%3D%20flag_h%2F4%0A%20%20%20%20ctx.fillStyle%3D%20'%23fff'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20ctx.fillStyle%3D%20'rgb(255%2C%200%2C%200)'%0A%20%20%20%20for%20i%20in%20range(0%2Cflag_h%2C2*flag_h%2F13)%3A%0A%20%20%20%20%20%20%20%20b%3Di%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2Cb%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2C2*flag_w%2F5%2C7*flag_h%2F13)%0A%20%20%20%20def%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20%20%20%20%20ctx.strokeStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20ctx.stroke()%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22%23f00%22)%3A%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout%2C%20yout%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout2%2C%20yout2%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B20*i%2C%2020%2B20*j%2C%205%2C%200%2C%20true%2C%20%22%23fff%22)%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(10%2B20*i%2C%2010%2B20*j%2C%205%2C%200%2C%20true%2C%20%22%23fff%22)%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C300%2C0)%0A%20%20%20%20ctx.rotate(270*math.pi%2F180)%0A%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2F2%2Cflag_h%2F2)%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20star_radius%20%3D%20flag_w%2F8%0A%20%20%20%20angle%20%3D%200%0A%20%20%20%20for%20i%20in%20range(24)%3A%0A%20%20%20%20%20%20%20%20angle%20%2B%3D%205*math.pi*2%2F12%0A%20%20%20%20%20%20%20%20toX%20%3D%20circle_x%20%2B%20math.cos(angle)*star_radius%0A%20%20%20%20%20%20%20%20toY%20%3D%20circle_y%20%2B%20math.sin(angle)*star_radius%0A%20%20%20%20%20%20%20%20if%20(i)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(toX%2C%20toY)%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(toX%2C%20toY)%0A%20%20%20%20ctx.fillStyle%20%3D%20'%23fff'%0A%20%20%20%20ctx.fill()%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.arc(circle_x%2C%20circle_y%2C%20flag_w*17%2F240%2C%200%2C%20math.pi*2%2C%20true)%0A%20%20%20%20ctx.closePath()%0A%20%20%20%20ctx.fillStyle%20%3D%20'rgb(0%2C%200%2C%20149)'%0A%20%20%20%20ctx.fill()%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.arc(circle_x%2C%20circle_y%2C%20flag_w%2F16%2C%200%2C%20math.pi*2%2C%20true)%0A%20%20%20%20ctx.closePath()%0A%20%20%20%20ctx.fillStyle%20%3D%20'%23fff'%0A%20%20%20%20ctx.fill()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g15_A and T  繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A6%2C%22y%22%3A4%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A5%2C%22_prev_y%22%3A4%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%221%2C1%22%3A%5B%22east%22%5D%2C%221%2C2%22%3A%5B%22east%22%5D%2C%221%2C3%22%3A%5B%22north%22%5D%2C%222%2C5%22%3A%5B%22north%22%5D%2C%221%2C5%22%3A%5B%22north%22%5D%2C%223%2C5%22%3A%5B%22north%22%5D%2C%224%2C5%22%3A%5B%22north%22%5D%2C%225%2C5%22%3A%5B%22north%22%2C%22east%22%5D%2C%222%2C3%22%3A%5B%22north%22%2C%22east%22%5D%2C%222%2C2%22%3A%5B%22east%22%5D%2C%223%2C2%22%3A%5B%22east%22%5D%2C%225%2C1%22%3A%5B%22east%22%5D%2C%225%2C3%22%3A%5B%22east%22%2C%22north%22%5D%2C%224%2C4%22%3A%5B%22east%22%2C%22north%22%5D%2C%224%2C2%22%3A%5B%22east%22%5D%2C%221%2C4%22%3A%5B%22east%22%5D%2C%225%2C2%22%3A%5B%22east%22%2C%22north%22%5D%2C%223%2C1%22%3A%5B%22north%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A6%2C%22y%22%3A4%7D%7D%2C%22large_world%22%3Afalse%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%20%20%20%20%20%20%20&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g15 機器人走迷宮1 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22robots%22%3A%5B%7B%22x%22%3A12%2C%22y%22%3A1%2C%22tokens%22%3A%22infinite%22%2C%22orientation%22%3A0%2C%22_prev_x%22%3A11%2C%22_prev_y%22%3A1%2C%22_prev_orientation%22%3A3%7D%5D%2C%22walls%22%3A%7B%222%2C1%22%3A%5B%22east%22%5D%2C%224%2C1%22%3A%5B%22east%22%5D%2C%226%2C1%22%3A%5B%22east%22%5D%2C%228%2C1%22%3A%5B%22east%22%5D%2C%2210%2C1%22%3A%5B%22east%22%5D%2C%2212%2C1%22%3A%5B%22east%22%5D%7D%2C%22goal%22%3A%7B%22position%22%3A%7B%22x%22%3A12%2C%22y%22%3A1%7D%7D%7D&editor=%23%20%E5%88%A9%E7%94%A8%E4%B8%89%E5%80%8B%E5%B7%A6%E8%BD%89%2C%20%E5%AE%9A%E7%BE%A9%E5%8F%B3%E8%BD%89%0Adef%20turn_right()%3A%0A%20%20%20%20for%20i%20in%20range(3)%3A%0A%20%20%20%20%20%20%20%20turn_left()%0A%20%0Awhile%20not%20at_goal()%3A%0A%20%20%20%20if%20not%20right_is_clear()%20and%20front_is_clear()%3A%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20elif%20right_is_clear()%3A%0A%20%20%20%20%20%20%20%20turn_right()%0A%20%20%20%20%20%20%20%20move()%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn_left()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g15 機器人走迷宮2 繪圖</a><br />
'''
        return outstring

    # 以下為 c2g15 組所建立的 CherryPy 程式方法, 這裡的 fillpoly 利用 Brython 執行網際繪圖
    ''' 
    假如採用下列規畫
    
    import programs.c2g15 as c2g15
    root.c2g15 = c2g15.C2G15()
    
    則程式啟動後, 可以利用 /c2g15/fillpoly 呼叫函式執行
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
    
    import programs.c2g15 as c2g15
    root.c2g15 = c2g15.C2G15()
    
    則程式啟動後, 可以利用 /c2g9/drawline 呼叫函式執行
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
   
  
