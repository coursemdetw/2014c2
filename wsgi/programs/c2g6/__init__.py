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
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20%23%20%E5%B0%8E%E5%85%A5%20doc%0A%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%0A%20%20%20%20%23%20%E6%BA%96%E5%82%99%E7%B9%AA%E5%9C%96%E7%95%AB%E5%B8%83%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20%23%20%E9%80%B2%E8%A1%8C%E5%BA%A7%E6%A8%99%E8%BD%89%E6%8F%9B%2C%20x%20%E8%BB%B8%E4%B8%8D%E8%AE%8A%2C%20y%20%E8%BB%B8%E5%8F%8D%E5%90%91%E4%B8%94%E7%A7%BB%E5%8B%95%20800%20%E5%85%89%E9%BB%9E%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C%20120%2C%20400)%0A%0A%0A%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22white%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin(72*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos(72*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin(72*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos(72*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin(72*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos(72*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20'white'%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%0A%20%20%20%20for%20i%20in%20range(7)%3A%0A%20%20%20%20%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2C%200%2B40*i%2C%20390%2C%2020)%0A%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20149)'%0A%20%20%20%20ctx.fillRect(0%2C%20120%2C%20210%2C%20140)%0A%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B34*i%2C%20134%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(36%2B34*i%2C%20148%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g6 美國國旗 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C0%2C0)%0A%20%20%20%20ctx.rotate(270*math.pi%2F180)%0A%20%20%20%20flag_w%20%3D300%0A%20%20%20%20flag_h%20%3D200%0A%20%20%20%20circle_x%20%3D%20flag_w%2F4%0A%20%20%20%20circle_y%20%3D%20flag_h%2F4%0A%20%20%20%20ctx.fillStyle%3D%20'%23fff'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20ctx.fillStyle%3D%20'rgb(255%2C%200%2C%200)'%0A%20%20%20%20for%20i%20in%20range(0%2Cflag_h%2C2*flag_h%2F13)%3A%0A%20%20%20%20%20%20%20%20b%3Di%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2Cb%2Cflag_w%2Cflag_h%2F13)%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2C2*flag_w%2F5%2C7*flag_h%2F13)%0A%20%20%20%20def%20draw_line(x1%2C%20y1%2C%20x2%2C%20y2%2C%20linethick%20%3D%203%2C%20color%20%3D%20%22black%22)%3A%0A%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20ctx.lineWidth%20%3D%20linethick%0A%20%20%20%20%20%20%20%20ctx.moveTo(x1%2C%20y1)%0A%20%20%20%20%20%20%20%20ctx.lineTo(x2%2C%20y2)%0A%20%20%20%20%20%20%20%20ctx.strokeStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20ctx.stroke()%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22%23f00%22)%3A%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos((360%2F5)*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos((360%2F5)*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos((360%2F5)*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout%2C%20yout%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20draw_line(xout2%2C%20yout2%2C%20xin%2C%20yin%2C%20color)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20color%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B20*i%2C%2020%2B20*j%2C%205%2C%200%2C%20true%2C%20%22%23fff%22)%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(10%2B20*i%2C%2010%2B20*j%2C%205%2C%200%2C%20true%2C%20%22%23fff%22)%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C300%2C0)%0A%20%20%20%20ctx.rotate(270*math.pi%2F180)%0A%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2Cflag_h)%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20150)'%0A%20%20%20%20ctx.fillRect(0%2C0%2Cflag_w%2F2%2Cflag_h%2F2)%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20star_radius%20%3D%20flag_w%2F8%0A%20%20%20%20angle%20%3D%200%0A%20%20%20%20for%20i%20in%20range(24)%3A%0A%20%20%20%20%20%20%20%20angle%20%2B%3D%205*math.pi*2%2F12%0A%20%20%20%20%20%20%20%20toX%20%3D%20circle_x%20%2B%20math.cos(angle)*star_radius%0A%20%20%20%20%20%20%20%20toY%20%3D%20circle_y%20%2B%20math.sin(angle)*star_radius%0A%20%20%20%20%20%20%20%20if%20(i)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(toX%2C%20toY)%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(toX%2C%20toY)%0A%20%20%20%20ctx.fillStyle%20%3D%20'%23fff'%0A%20%20%20%20ctx.fill()%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.arc(circle_x%2C%20circle_y%2C%20flag_w*17%2F240%2C%200%2C%20math.pi*2%2C%20true)%0A%20%20%20%20ctx.closePath()%0A%20%20%20%20ctx.fillStyle%20%3D%20'rgb(0%2C%200%2C%20149)'%0A%20%20%20%20ctx.fill()%0A%20%20%20%20ctx.beginPath()%0A%20%20%20%20ctx.arc(circle_x%2C%20circle_y%2C%20flag_w%2F16%2C%200%2C%20math.pi*2%2C%20true)%0A%20%20%20%20ctx.closePath()%0A%20%20%20%20ctx.fillStyle%20%3D%20'%23fff'%0A%20%20%20%20ctx.fill()&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g6 兩面國旗 繪圖</a><br />
<a href="http://2014c2-mdenfu.rhcloud.com/static/reeborg/world.html?proglang=python-en&world=%7B%22blank_canvas%22%3Atrue%7D&editor=%20%20%20%20%23%20%E5%B0%8E%E5%85%A5%20doc%0A%20%20%20%20from%20browser%20import%20doc%0A%20%20%20%20import%20math%0A%0A%20%20%20%20%23%20%E6%BA%96%E5%82%99%E7%B9%AA%E5%9C%96%E7%95%AB%E5%B8%83%0A%20%20%20%20canvas%20%3D%20doc%5B%22background_canvas%22%5D%0A%20%20%20%20ctx%20%3D%20canvas.getContext(%222d%22)%0A%20%20%20%20%23%20%E9%80%B2%E8%A1%8C%E5%BA%A7%E6%A8%99%E8%BD%89%E6%8F%9B%2C%20x%20%E8%BB%B8%E4%B8%8D%E8%AE%8A%2C%20y%20%E8%BB%B8%E5%8F%8D%E5%90%91%E4%B8%94%E7%A7%BB%E5%8B%95%20800%20%E5%85%89%E9%BB%9E%0A%20%20%20%20ctx.setTransform(1%2C%200%2C%200%2C%20-1%2C%20200%2C%20500)%0A%0A%20%20%20%20ctx.rotate(45*math.pi%2F180)%3B%0A%0A%20%20%20%20%23%20x%2C%20y%20%E7%82%BA%E4%B8%AD%E5%BF%83%2C%20%20r%20%E7%82%BA%E5%8D%8A%E5%BE%91%2C%20angle%20%E6%97%8B%E8%BD%89%E8%A7%92%2C%20%20solid%20%E7%A9%BA%E5%BF%83%E6%88%96%E5%AF%A6%E5%BF%83%2C%20%20color%20%E9%A1%8F%E8%89%B2%0A%20%20%20%20def%20star(x%2C%20y%2C%20r%2C%20angle%3D0%2C%20solid%3DFalse%2C%20color%3D%22white%22)%3A%0A%20%20%20%20%20%20%20%20%23%20%E4%BB%A5%20x%2C%20y%20%E7%82%BA%E5%9C%93%E5%BF%83%2C%20%E8%A8%88%E7%AE%97%E4%BA%94%E5%80%8B%E5%A4%96%E9%BB%9E%0A%20%20%20%20%20%20%20%20deg%20%3D%20math.pi%2F180%0A%20%20%20%20%20%20%20%20%23%20%E5%9C%93%E5%BF%83%E5%88%B0%E6%B0%B4%E5%B9%B3%E7%B7%9A%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20a%20%3D%20r*math.cos(72*deg)%0A%20%20%20%20%20%20%20%20%23%20a%20%E9%A0%82%E9%BB%9E%E5%90%91%E5%8F%B3%E5%88%B0%E5%85%A7%E9%BB%9E%E8%B7%9D%E9%9B%A2%0A%20%20%20%20%20%20%20%20b%20%3D%20(r*math.cos(72*deg)%2Fmath.cos(36*deg))*math.sin(36*deg)%0A%20%20%20%20%20%20%20%20%23%20%E5%88%A9%E7%94%A8%E7%95%A2%E6%B0%8F%E5%AE%9A%E7%90%86%E6%B1%82%E5%85%A7%E9%BB%9E%E5%8D%8A%E5%BE%91%0A%20%20%20%20%20%20%20%20rin%20%3D%20math.sqrt(a**2%20%2B%20b**2)%0A%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%20a%2C%20b%20%E8%88%87%20rin%0A%20%20%20%20%20%20%20%20%23print(a%2C%20b%2C%20rin)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.beginPath()%0A%20%20%20%20%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20xout%20%3D%20(x%20%2B%20r*math.sin(72*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20yout%20%3D%20(y%20%2B%20r*math.cos(72*deg*i%2Bangle*deg))%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A4%96%E9%BB%9E%E5%A2%9E%E9%87%8F%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20xout2%20%3D%20x%20%2B%20r*math.sin(72*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yout2%20%3D%20y%20%2B%20r*math.cos(72*deg*(i%2B1)%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20xin%20%3D%20x%20%2B%20rin*math.sin(72*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20yin%20%3D%20y%20%2B%20rin*math.cos(72*deg*i%2B36*deg%2Bangle*deg)%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E6%9F%A5%E9%A9%97%E5%A4%96%E9%BB%9E%E8%88%87%E5%85%A7%E9%BB%9E%E5%BA%A7%E6%A8%99%0A%20%20%20%20%20%20%20%20%20%20%20%20%23print(xout%2C%20yout%2C%20xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20%E5%A1%AB%E8%89%B2%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if(i%3D%3D0)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.moveTo(xout%2C%20yout)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xin%2C%20yin)%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ctx.lineTo(xout2%2C%20yout2)%0A%20%20%20%20%20%20%20%20if(solid)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fillStyle%20%3D%20'white'%0A%20%20%20%20%20%20%20%20%20%20%20%20ctx.fill()%0A%0A%20%20%20%20for%20i%20in%20range(7)%3A%0A%20%20%20%20%20%20%20%20ctx.fillStyle%3D'rgb(255%2C%200%2C%200)'%0A%20%20%20%20%20%20%20%20ctx.fillRect(0%2C%200%2B40*i%2C%20390%2C%2020)%0A%0A%20%20%20%20ctx.fillStyle%3D'rgb(0%2C%200%2C%20149)'%0A%20%20%20%20ctx.fillRect(0%2C%20120%2C%20210%2C%20140)%0A%0A%20%20%20%20for%20i%20in%20range(6)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(20%2B34*i%2C%20134%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)%0A%20%20%20%20for%20i%20in%20range(5)%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range(4)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20star(36%2B34*i%2C%20148%2B28*j%2C%208%2C%200%2C%20True%2C%20%22white%22)&library=%23%20'import%20my_lib'%20in%20Python%20Code%20is%20required%20to%20use%0A%23%20the%20code%20in%20this%20library.%20%0Adef%20turn_right()%3A%0A%20%20%20%20repeat(turn_left%2C%203)">c2g6 美國國旗45度 繪圖</a><br />

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
    
    import programs.c2g6 as c2g6
    root.c2g6 = c2g6.C2G6()
    
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
    
    import programs.c2g6 as c2g6
    root.c2g6 = c2g6.C2G6()
    
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