
########################### 1. 導入所需模組
import cherrypy
import os

########################### 2. 設定近端與遠端目錄
# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"

########################### 3. 建立主物件
class HelloWorld(object):
    _cp_config = {
    # if there is no utf-8 encoding, no Chinese input available
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    'tools.sessions.locking' : 'explicit',
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session timeout is 60 minutes
    'tools.sessions.timeout' : 60
    }
    
    @cherrypy.expose
    def fileuploadform(self):
        return '''<h1>file upload</h1>
    <script src="/static/jquery.js" type="text/javascript"></script>
    <script src="/static/axuploader.js" type="text/javascript"></script>
    <script>
    $(document).ready(function(){
    $('.prova').axuploader({url:'/fileaxupload', allowExt:['jpg','png','gif','7z','pdf','zip','flv','stl','txt'],
    finish:function(x,files)
        {
            alert('All files have been uploaded: '+files);
        },
    enable:true,
    remotePath:function(){
        return 'downloads/';
    }
    });
    });
    </script>
    <div class="prova"></div>
    <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
    <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
    </section></body></html>
    '''
    @cherrypy.expose
    def brythonuploadform(self):
        return '''<h1>file upload</h1>
    <script type="text/javascript" src="/static/Brython2.0.0-20140209-164925/brython.js"></script>
    <script type="text/javascript" >
    function getradio(tagname){
    var radios = document.getElementsByName(tagname);
    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            // do whatever you want with the checked radio
            return radios[i].value;
            // only one radio can be logically checked, don't check the rest
            break;
          }
       }
    }

    function run_js(){
        var cons = document.getElementById("console")
        var jscode = cons.value
        var t0 = (new Date()).getTime()
        eval(jscode)
        var t1 = (new Date()).getTime()
        console.log("Javascript code run in "+(t1-t0)+" ms")
    }
    </script>
    <script type="text/python3" src="/static/editor.py"></script>

    <script type="text/python3">
    from browser import doc

    overwrite = 0
    # add delete_program 1/7, seven steps to complete the ajax task, the last step is to add delete_program function on server
    # delete1 and delete2 parameters are also added into save_program function.
    delete1 = 0
    delete2 = 0

    def set_debug(ev):
        if ev.target.checked:
            __BRYTHON__.debug = 1
        else:
            __BRYTHON__.debug = 0
            
    def set_overwrite(ev):
        global overwrite
        if ev.target.checked:
            overwrite = 1
        else:
            overwrite = 0

    # add delete_program 2/7, client side add set_delete1 and set_delete2 functions.
    def set_delete1(ev):
        global delete1
        if ev.target.checked:
            delete1 = 1
        else:
            delete1 = 0

    def set_delete2(ev):
        global delete2
        if ev.target.checked:
            delete2 = 1
        else:
            delete2 = 0

    #### ajax process
    from browser import ajax,doc

    def on_complete(req):
        print(req.readyState)
        print('status',req.status)
        if req.status==200 or req.status==0:
            # show request text on id=result division
            doc["result"].html = req.text
        else:
            doc["result"].html = "error "+req.text

    def err_msg():
        doc["result"].html = "server didn't reply after %s seconds" %timeout

    timeout = 4

    def go(url):
        req = ajax.ajax()
        req.bind('complete', on_complete)
        req.set_timeout(timeout, err_msg)
        req.open('GET', url, True)
        req.send()

    def post(url):
        req = ajax.ajax()
        req.bind('complete', on_complete)
        req.set_timeout(timeout, err_msg)
        req.open('POST', url, True)
        req.set_header('content-type','application/x-www-form-urlencoded')
        # doc["filename"].value is the id=filename input field's value
        # editor.getValue() is the content on editor, need to send dictionary format data
        # while post url, need to save editor content into local_storage to use the previous load javascripts
        storage["py_src"] = editor.getValue()
        # add delete_program 3/7, two parameters added, this will also affect save_program function on server.
        req.send({'filename':doc["filename"].value, 'editor':editor.getValue(), 'overwrite':overwrite, 'delete1':delete1, 'delete2':delete2})
        
    # get program from server
    def get_prog(ev):
        # ajax can only read data from server
        _name = '/brython_programs/'+doc["filename"].value
        try:
            editor.setValue(open(_name, encoding="utf-8").read())
            doc["result"].html = doc["filename"].value+" loaded!"
        except:
            doc["result"].html = "can not get "+doc["filename"].value+"!"
        editor.scrollToRow(0)
        editor.gotoLine(0)
        reset_theme()
        
    def get_radio(ev):
        from javascript import JSObject
        filename = JSObject(getradio)("filename")
        # ajax can only read data from server
        doc["filename"].value = filename
        _name = '/brython_programs/'+filename
        editor.setValue(open(_name, encoding="utf-8").read())
        doc["result"].html = filename+" loaded!"
        editor.scrollToRow(0)
        editor.gotoLine(0)
        reset_theme()
        
    # bindings
    doc['run_js'].bind('click',run_js)
    doc['set_debug'].bind('change',set_debug)
    doc['set_overwrite'].bind('change',set_overwrite)
    # add delete_program 4/7, two associated binds added
    doc['set_delete1'].bind('change',set_delete1)
    doc['set_delete2'].bind('change',set_delete2)
    # next functions are defined in editor.py
    doc['show_js'].bind('click',show_js)
    doc['run'].bind('click',run)
    doc['show_console'].bind('click',show_console)
    # get_prog and get _radio (working)
    doc['get_prog'].bind('click', get_prog)
    doc['get_radio'].bind('click', get_radio)
    # reset_the_src and clear_console (working)
    doc['reset_the_src'].bind('click',reset_the_src)
    doc['clear_console'].bind('click',clear_console)
    # clear_canvas and clear_src
    doc['clear_canvas'].bind('click',clear_canvas)
    doc['clear_src'].bind('click',clear_src)
    # only admin can save program to server
    doc['save_program'].bind('click',lambda ev:post('/save_program'))
    # add delete_program 5/7, delete_program button bind to execute delete_program on server.
    doc['delete_program'].bind('click',lambda ev:post('/delete_program'))
    </script>
    <script type="text/javascript">
    window.onload=brython({debug:1, cache:'version'});
    </script>
    <div class="prova"></div>
    <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
    <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
    </section></body></html>
    '''
    @cherrypy.expose
    def fileaxupload(self, *args, **kwargs):
        filename = kwargs["ax-file-name"]
        flag = kwargs["start"]
        # 終於找到 bug, 因為從 kwargs[] 所取得的變數為字串, 而非數字, 先前用 flag == 0 是錯誤的
        if flag == "0":
            # 若從 0 byte 送起, 表示要開啟新檔案
            file = open(download_root_dir+"downloads/"+filename, "wb")
        else:
            file = open(download_root_dir+"downloads/"+filename, "ab")
        file.write(cherrypy.request.body.read())
        file.close()
        
        return "files uploaded!"
    @cherrypy.expose
    def index(self, input1=None, input2=None):
        return "Hello world!"+str(input1)+_curdir
    @cherrypy.expose
    def inputform(self, input1=None, input2=None):
        return "input form"+str(input1)
    #index.exposed = True

########################### 4. 安排啟動設定
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"}
    }

########################### 5. 在近端或遠端啟動程式
# 利用 HelloWorld() class 產生案例物件
root = HelloWorld()
# 假如在 os 環境變數中存在 'OPENSHIFT_REPO_DIR', 表示程式在 OpenShift 環境中執行
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 雲端執行啟動
    application = cherrypy.Application(root, config = application_conf)
else:
    # 近端執行啟動
    '''
    cherrypy.server.socket_port = 8083
    cherrypy.server.socket_host = '127.0.0.1'
    '''
    cherrypy.quickstart(root, config = application_conf)
