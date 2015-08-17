#ScratchEdit editor by Dylan Beswick
global scratchBlocks
global version
version = 3.4
scratchBlocks = {'procDef':{'t':"Custom Block: §1", 's':[1]}, 'whenGreenFlag':{'t':"When Green Flag Clicked", 's':[]}, 'whenIReceive':{'t':r"When I Receive: §1", 's':[1]}, 'doBroadcastAndWait':{'t':"Broadcast §1 and wait", 's':[1]}, 'broadcast:':{'t':"Broadcast §1", 's':[1]}, 'whenSensorGreaterThan':{'t':r"When §1 greater than §2", 's':[1,2]}, 'whenKeyPressed':{'t':"When §1 key pressed", 's':[1]}, 'whenClicked':{'t':"When this sprite clicked", 's':[]}, 'whenCloned':{'t':"When I start as a clone", 's':[]}, 'wait:elapsed:from:':{'t':"Wait §1 secs", 's':[1]}, 'doRepeat':{'t':"Repeat §1 Times >", 's':[1]}, 'doForever':{'t':"Repeat Forever >", 's':[]}, 'doIf':{'t':'If §1 >', 's':[1]}, 'doIfElse':{'t':'If §1 Else >', 's':[1]}, 'doWaitUntil':{'t':'Wait Until §1', 's':[1]}, 'doUntil':{'t':'Repeat Until §1>', 's':[1]}, 'stopScripts':{'t':'Stop §1', 's':[1]},
    'createCloneOf':{'t':'Create clone of §1', 's':[1]}, 'deleteClone':{'t':'Delete this clone', 's':[]}, 'touching:':{'t':'Touching §1', 's':[1]}, 'touchingColor:':{'t':'Touching color (int) §1', 's':[1]}, 'distanceTo:':{'t':'Distance to §1', 's':[1]}, 'color:sees:':{'t':'Colorid §1 is touching colorid §2', 's':[1, 2]}, 'doAsk':{'t':'Ask §1', 's':[1]}, 'answer':{'t':'Answer', 's':[]},
    'keyPressed:':{'t':'Key §1 pressed?', 's':[1]}, 'mousePressed':{'t':'Mouse Down?', 's':[]}, 'mouseX':{'t':'Mouse X', 's':[]}, 'mouseY':{'t':'Mouse Y', 's':[]}, 'soundLevel':{'t':'Loudness', 's':[]}, 'senseVideoMotion':{'t':'Video §1 on §2', 's':[1,2]}, 'setVideoState':{'t':'Turn video [§1]', 's':[1]},
    'setVideoTransparency':{'t':"Set Video Transparency To §1%", 's':[1]}, 'timer':{'t':"Timer", 's':[]}, 'timerReset':{'t':"Reset Timer", 's':[]}, 'getAttribute:of:':{'t':"§1 of §2", 's':[1,2]}, 'timeAndDate':{'t':"Current §1", 's':[1]}, 'timestamp':{'t':'Days since 2000', 's':[]}, 'getUserName':{'t':"Username", 's':[]},
    '+':{'t':"§1 + §2", 's':[1,2]}, '-':{'t':"§1 - §2", 's':[1,2]}, '*':{'t':"§1 * §2", 's':[1,2]}, '/':{'t':"§1 / §2", 's':[1,2]}, 'randomFrom:to:':{'t':"Pick random from §1 to §2", 's':[1,2]}, '>':{'t':"§1 > §2", 's':[1, 2]}, '<':{'t':"§1 < §2", 's':[1, 2]}, '=':{'t':"§1 = §2",'s':[1, 2]}, '&':{'t':"§1 and §2", 's':[1,2]}, '|':{'t':"§1 or §2", 's':[1,2]}, 'not':{'t':"Not §1", 's':[1]}, 'concatenate:with:':{'t':"Join §1 §2", 's':[1,2]}, 'letter:of:':{'t':"Letter §1 of §2", 's':[1,2]} ,
    'stringLength:':{'t':"Length of §1", 's':[1]}, '%':{'t':"§1 mod §2", 's':[1,2]}, 'rounded':{'t':"Round §1", 's':[1]}, 'computeFunction:of:':{'t':"§1 of §2", 's':[1,2]}, 'call':{'t':"§1", 's':[1]}, 'forward:':{'t':"Move §1 steps", 's':[1]}, 'turnRight:':{'t':"Rotate §1 degrees clockwise", 's':[1]}, 'turnLeft:':{'t':"Rotate §1 degrees counterclockwise", 's':[1]},
    'heading:':{'t':"Point in direction §1", 's':[1]}, 'pointTowards:':{'t':"Point Towards §1", 's':[1]}, 'gotoX:y:':{'t':"Goto X: §1 Y: §2", 's':[1,2]}, 'gotoSpriteOrMouse:':{'t':"Go to §1", 's':[1]}, 'glideSecs:toX:y:elapsed:from:':{'t':"Glide §3 secs to X: §1 Y: §2", 's':[1,2,3]},
    'changeXposBy:':{'t':"Change X by §1", 's':[1]}, 'xpos:':{'t':"Set X to §1", 's':[1]}, 'changeYposBy:':{'t':"Change Y by §1", 's':[1]}, 'ypos:':{'t':"Set Y to §1", 's':[1]}, 'bounceOffEdge':{'t':"If on edge, bounce", 's':[]}, 'setRotationStyle':{'t':'Set rotation style §1', 's':[1]}, 'xpos':{'t':"X position", 's':[]}, 'ypos':{'t':"Y position", 's':[]},
    'heading':{'t':"Direction", 's':[]}, 'say:duration:elapsed:from:':{'t':"Say §1 for §2 secs", 's':[1,2]}, 'say:':{'t':"Say §1", 's':[1]}, 'think:duration:elapsed:from:':{'t':"Think §1 for §2 secs", 's':[1,2]}, 'think:':{'t':"Think §1", 's':[1]}, 'show':{'t':"Show", 's':[]}, 'hide':{'t':"Hide",'s':[]},
    'lookLike:':{'t':"Switch costume to §1", 's':[1]}, 'nextCostume':{'t':"Next Costume", 's':[]}, 'startScene':{'t':"Switch backdrop to §1", 's':[1]}, 'changeGraphicEffect:by:':{'t':"Change §1 effect by §2", 's':[1,2]}, 'setGraphicEffect:to:':{'t':"Set §1 effect to §2", 's':[1,2]}, 'filterReset':{'t':"Clear Graphic Effects", 's':[]},
    'changeSizeBy:':{'t':'Change Size by §1%', 's':[1]}, 'setSizeTo:':{'t':'Set size to §1%', 's':[1]}, 'comeToFront':{'t':'Go to front', 's':[]}, 'goBackByLayers:':{'t':"Go back §1 layers", 's':[1]}, 'costumeIndex':{'t':'Costume #','s':[]}, 'sceneName':{'t':"Backdrop name", 's':[]}, 'scale':{'t':'Size', 's':[]},
    'playSound:':{'t':'Play sound §1', 's':[1]}, 'doPlaySoundAndWait':{'t':'Play sound §1 and wait', 's':[1]}, 'stopAllSounds':{'t':'Stop all sounds', 's':[]}, 'playDrum':{'t':'Play drum §1 for §2 beats', 's':[1,2]}, 'rest:elapsed:from:':{'t':'Rest for §1 beats', 's':[1]},
    'noteOn:duration:elapsed:from:':{'t':'Play note §1 for §2 beats', 's':[1,2]}, 'instrument:':{'t':'Set Instrument to §1', 's':[1]}, 'changeVolumeBy:':{'t':'Change Volume by §1', 's':[1]}, 'setVolumeTo:':{'t':'Set Volume To §1', 's':[1]}, 'volume':{'t':'Volume', 's':[]}, 'changeTempoBy:':{'t':'Change tempo by §1', 's':[1]},
    'setTempoTo:':{'t':'Set tempo to §1', 's':[1]}, 'tempo':{'t':'Tempo', 's':[]}, 'stampCostume':{'t':'Stamp', 's':[]}, 'putPenDown':{'t':'Pen Down', 's':[]}, 'clearPenTrails':{'t':'Clear', 's':[]}, 'putPenUp':{'t':'Pen Up', 's':[]}, 'penColor:':{'t':'Set pen colour (number) to §1', 's':[1]}, 'changePenHueBy:':{'t':'Change pen colour by §1', 's':[1]},
    'setPenHueTo:':{'t':"Set pen colour to §1", 's':[1]}, 'changePenShadeBy:':{'t':"Change pen shade by §1", 's':[1]}, 'setPenShadeTo:':{'t':"Set pen shade to §1", 's':[1]}, 'changePenSizeBy:':{'t':"Change pen size by §1", 's':[1]}, 'penSize:':{'t':"Set pen size to §1", 's':[1]}, 'readVariable':{'t':"Variable: §1", 's':[1]},
    'setVar:to:':{'t':"Set §1 to §2", 's':[1,2]}, 'changeVar:by:':{'t':"Change §1 by §2", 's':[1,2]}, 'showVariable:':{'t':"Show Variable §1", 's':[1]}, 'hideVariable:':{'t':"Hide Variable §1", 's':[1]}, 'contentsOfList:':{'t':"List: §1", 's':[1]}, 'append:toList:':{'t':"Add §1 to §2", 's':[1,2]},
    'deleteLine:ofList:':{'t':"Delete §1 of §2", 's':[1,2]}, 'insert:at:ofList:':{'t':"Insert §1 at §2 of §3", 's':[1,2,3]}, 'setLine:ofList:to:':{'t':"Replace Item §1 of §2 with §3", 's':[1,2,3]} , 'getLine:ofList:':{'t':"Item §1 of list §2", 's':[1,2]}, 'lineCountOfList:':{'t':'Length of list: §1', 's':[1]},
    'list:contains:':{'t':"List §1 Contains §2", 's':[1,2]}, 'showList:':{'t':"Show List §1", 's':[1]}, 'hideList:':{'t':"Hide List §1", 's':[1]}, 'getParam':{'t':"Argument: §1", 's':[1]}}
global FILE_LOADED
FILE_LOADED = False
import sys
import time
import urllib.request
import platform
import threading
import os
import collections
import zipfile
import subprocess
import traceback
import json
import webbrowser
# Done imports
args = sys.argv
if args[1] == 'error':
    print(args[2])
    sys.stdin.readline(0)
    sys.exit()

fatalErr = False
errText = ''
if not int(platform.python_branch().replace('.','')[1:]) > 339:
    errText = errText + ('ScratchEdit is made for Python "v3.4.0" but your Python version is "' + platform.python_branch() + '"\n')
    fatalErr = True
try:
    import tkinter
except:
    errText = errText + ('tkinter wasn\'t installed during Python installation!! ScratchEdit cannot be used if Python has not been installed with the official installer OR you have unchecked "Tcl/IDLE" in the installer. Please reinstall Python and do it right\n')
    fatalErr = True
else:
    del tkinter
if not platform.uname().system == 'Windows':
    errText = errText + ('You have to be using Windows to run ScratchEdit!\n')
    fatalErr = True
if fatalErr == True:
    errText = errText + ('Press return to close')
    subprocess.call([sys.executable.replace('pythonw','python'), __file__, 'error', fatalErr])
    sys.exit()

def crash(error,header='ERROR',raw=False,c=True,sysexit=True,openlogfile=True):
    log.add(error,header,raw=raw,c=c)
    if openlogfile:
        os.startfile(log.name)
    if sysexit:
        os._exit(1)
from tkinter import *
class _ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None, edit=False, wrap=False):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets(edit, wrap)
        self.settext(text, file)
    def makewidgets(self, edit=False, wrap=False):
        sbar = Scrollbar(self)
        if wrap:
            text = Text(self, relief=SUNKEN, wrap=WORD)
        else:
            text = Text(self, relief=SUNKEN)
        if edit == False:
            text.config(state=DISABLED)
        self.edit = edit
        sbar.config(command=text.yview)               
        text.config(yscrollcommand=sbar.set)           
        sbar.pack(side=RIGHT, fill=Y)                 
        text.pack(side=LEFT, expand=YES, fill=BOTH)  
        self.text = text
    def settext(self, text='', file=None):
        self.text.config(state=NORMAL)
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                 
        self.text.insert('1.0', text)               
        self.text.mark_set(INSERT, '1.0')          
        self.text.focus()
        if not self.edit:
            self.text.config(state=DISABLED)
    def gettext(self):                             
        return self.text.get('1.0', END + '-1c')
    def print(self, value, end='\n'):
        self.settext(self.gettext() + value + end)
class ini:
    "Class for manipulating .ini files"
    def __init__(self, ini):
        "Read ini from file object or string given -> ini object"
        if str(ini)[:18] == '<_io.TextIOWrapper':
            if ini.mode == 'r':
                data = ini.read()
                ini.close()
            else:
                invalidFileOperationMode = 'File object does not support reading ("r") mode'
                raise ValueError(invalidFileOperationMode)
        else:
            if type(ini) == str:
                data = ini
            else:
                invalidObjectType = 'Expected "str" or "_io.TextIOWrapper" but got ' + (str(ini.__class__).split()[1][:-1])
                raise TypeError(invalidObjectType)
        data = str(data).rsplit(sep='\n')
        output = {"__default__":{}}
        currentPosition = "__default__"
        currentGroup = 0
        lines = [{"id":"__default__", "subObjects":[]}]
        lineNumber = -1
        for x in data:
            lineNumber = lineNumber + 1
            if (str(x).replace(' ', '') != '') and (str(x)[0] != '#'):
                if x[0] == '[':
                    st = ''
                    for y in x:
                        if y == ']':
                            break
                        elif y != '[':
                            st = st + y
                    currentPosition = st
                    lines.append({"id":st, "subObjects":[]})
                    currentGroup = currentGroup + 1
                    output[currentPosition] = {}
                else:
                    key = ''
                    val = ''
                    mode = 'key'
                    counter = -1
                    for z in x:
                        counter = counter + 1
                        if mode == 'key':
                            if z == '=':
                                mode = 'value'
                                continue
                            elif z == ' ':
                                try:
                                    if x[counter + 1] != '=':
                                        key = key + z
                                except:
                                    pass
                            else:
                                key = key + z
                        if mode == 'value':
                            if z == ' ':
                                try:
                                    if x[counter - 1] != '=':
                                        val = val + z
                                except:
                                    pass
                            else:
                                val = val + z
                    lines[currentGroup]["subObjects"].append(key)
                    try:
                        value1 = eval(val)
                    except:
                        value1 = val
                    output[currentPosition][key] = value1
            else:
                if str(x).replace(' ','') != '':
                    if str(x)[0] == '#':
                        lines[currentGroup]["subObjects"].append({"comment":str(x)})
        self._orderIndex = lines
        self.ini = output

    def dump(self, ini, file=None):
        "Write ini to file or return ini syntax if file argument not given"
        if ini.__class__ != dict:
            badIni = 'Expected "dict" but got ' + (str(ini.__class__).split()[1][:-1])
            raise TypeError(badIni)
        default = ini["__default__"]
        self.specified = ini
        del self.specified["__default__"]
        iniText = ''
        if default != {}:
            run = True
        else:
            run = False
        for x in self._orderIndex[0]["subObjects"]:
            try:
                if isinstance(x, dict):
                    if "comment" in x:
                        iniText = iniText + x["comment"] + '\n'
                else:
                    iniText = iniText + str(x) + ' = ' + str(default[x]) + '\n'
                    del default[x]
            except:
                traceback.print_exc()
        for x in default:
            if not (x in self._orderindex[0]):
                iniText = iniText + str(x) + ' = ' + str(default[x]) + '\n'
        if run:
            iniText = iniText + '\n'
        for x in self._orderIndex:
            if x["id"] != "__default__":
                try:
                    iniText = iniText + '[' + str(x["id"]) + ']\n'
                    for y in x["subObjects"]:
                        try:
                            if isinstance(y, dict):
                                if "comment" in y:
                                    iniText = iniText + y["comment"] + '\n'
                            else:
                                iniText = iniText + str(y) + ' = ' + str(self.specified[x["id"]][y]) + '\n'
                                del self.specified[x["id"]][y]
                        except:
                            traceback.print_exc()
                    for y in self.specified[x["id"]]:
                        try:
                            iniText = iniText + str(y) + ' = ' + str(self.specified[x["id"]][y]) + '\n'
                        except:
                            pass
                    del self.specified[x["id"]]
                    iniText = iniText + '\n'
                except:
                    pass

        for x in self.specified:
            iniText = iniText + '[' + str(x) + ']\n'
            for y in self.specified[x]:
                iniText = iniText + str(y) + ' = ' + str(self.specified[x][y]) + '\n'
            iniText = iniText + '\n'
            
        if file:
            if str(file)[:18] == '<_io.TextIOWrapper':
                if (not (file.mode == 'w')) and (not (file.mode == 'w+')):
                    invalidFileOperationMode = 'File object does not support writing ("w"/"w+") mode'
                    raise ValueError(invalidFileOperationMode)
            else:
                invalidObjectType = 'Expected "_io.TextIOWrapper" but got ' + (str(file.__class__).split()[1][:-1])
                raise TypeError(invalidObjectType)
            file.write(iniText)
            file.close()
        else:
            return iniText


if not os.path.isdir('C:\\ProgramData\\ScratchEdit'):
    os.makedirs('C:\\ProgramData\\ScratchEdit')
    os.makedirs('C:\\ProgramData\\ScratchEdit\\.logging')
    fh = open('C:\\ProgramData\\ScratchEdit\\ScratchEdit.ini', 'w')
    fh.write('''# ScratchEdit ini, set options here. Only change text on the righthand side of the equals sign.
[Graphics]
Show Script Formatting = True
Text Size = 14
Font = Arial
Text Colour = Black

[System]
# This won't slow down ScratchEdit. It may take a little while to check though.
Check For Update at Startup = True
# You will have massive lag when viewing large Scratch Projects if this is set to true.
Update JSON Window Every Edit = False''')
    fh.close()
time.sleep(0.01)
import subprocess
import threading
import urllib.request
class raw_version_wget_threader:
    def thread_run(arg_url, arg_version, callback):
        def runInThread(url, version, callback):
            r = urllib.request.urlopen(url).read().decode('utf-8')
            if str(r).replace('\n','') != str(version):
                callback(r)
            return
        thread = threading.Thread(target=runInThread, args=(arg_url, arg_version, callback))
        thread.start()
def api_update_check_se_callback(ver=None):
    t = Tk()
    t.withdraw()
    if db.askyesno('ScratchEdit Update', 'A Newer version of ScratchEdit is available: ' + str(ver) + '\nDo you want to install it?', master=t):
        f = urllib.request.urlopen('https://raw.githubusercontent.com/Dylan5797/ScratchEdit/master/ScratchEdit.pyw').read().decode('utf-8')
        fr = open(__file__, 'w',encoding='utf8')
        fr.write(f)
        fr.close()
        os.startfile(__file__)
        os._exit(1)
set0 = ini(open("C:\\ProgramData\\ScratchEdit\\ScratchEdit.ini")).ini
set1 = {}
for x in set0:
    if x != '__default__':
        set1.update(set0[x])
global sets
sets = {}
for x in set1:
    key = x.upper()
    if str(set1[x]).lower() in ["true", "false"]:
        value = eval(str(set1[x]).lower().capitalize())
    else:
        try:
            int(set1[x])
        except:
            value = set1[x]
        else:
            value = int(set1[x])
    sets[key] = value

class Log():
    def __init__(self, text='ScratchEdit ' + str(version)):
        self.time = self.timestamp()
        self.name = 'C:\\ProgramData\\ScratchEdit\\.logging\\' + self.time + '.txt'
        a = open(self.name, 'w')
        a.write(text + ' --' + self.timestamp(False) + '\n')
        a.close()
    def add(self, value, header='INFO', raw=False, c=True):
        f = open(self.name)
        if not raw:
            if c:
                ap = f.read() + self.timestamp(False) + ' [' + str(header) + ']: ' + str(value) + '\n'
            else:
                ap = f.read() + '\n' + self.timestamp().replace('-', '/') + ' [' + str(header) + ']' + str(value) + '\n'
        else:
            ap = f.read() + str(value)
        f.close()
        f = open(self.name, 'w+')
        f.write(ap)
        f.close()
    def get_current_time(self, ff=True):
        if ff:
            return time.strftime('[%H.%M.%S]')
        else:
            return time.strftime('[%H:%M:%S]')
    def get_current_date(self, ff=True):
        if ff:
            return time.strftime('[%y-%m-%d]')
        else:
            return time.strftime('[%y/%m/%d]')
    def timestamp(self, ff=True):
        if ff:
            return time.strftime('[%y-%m-%d %H.%M.%S]')
        else:
            return time.strftime('[%y/%m/%d %H:%M:%S]')
import tkinter.messagebox as db
import tkinter.filedialog
import tkinter.simpledialog as sd
if sets["Check For Update at Startup".upper()]:
    raw_version_wget_threader.thread_run('https://raw.githubusercontent.com/Dylan5797/ScratchEdit/current-update/latestupdate.txt', str(version), api_update_check_se_callback)
tk = Tk()
tk.focus()
tk.title('ScratchEdit')
global log
log = Log()
log.add('Successfully imported all modules')
def forcekill(e=None):
    log.add('Under forcekill() call. Destroying {"EditorWindow":"edw", "ValueEditor":"ky", "HelpScreen":"helps", "MainScratchEditWindow":"tk"}')
    try:
        edw.destroy()
    except:
        pass
    try:
        ky.destroy()
    except:
        pass
    try:
        helps.destroy()
    except:
        pass
    try:
        tk.destroy()
    except:
        pass
# Load Call
def load():
    log.add('Initializing Load Call...')
    global FILE_LOADED
    FILE_LOADED = True
    global loadf
    loadf = tkinter.filedialog.askopenfilename(filetypes=[('Scratch Projects','sb2')])
    if os.path.isfile(loadf):
        log.add('Ready to read file at "' + loadf + '" ')
        global zipf
        try:
            zipf = zipfile.ZipFile(loadf)
        except:
            log.add('[corruptScratchFile] [' + str(traceback.format_exc()) + ']')
        try:
            # regenerate_lb() -> Advance in explorer -> regenerate listbox -> edit items that are not explorable
            def regenerate_lb(goback=False):
                log.add('Regenerating ListBox at depth [\'stage\']' + str(dep) + '. ')
                global ls
                ls = dat
                isdict = True
                for x in dep:
                    if not (isinstance(ls, dict) or isinstance(ls, list)):
                        isdict = False
                        break
                    try:
                        ls = ls[x]
                    except:
                        exec('ls = ls["""' + x + '"""]')
                try:
                    if isinstance(ls[0], int) and isinstance(ls[1], int) and isinstance(ls[2], list):
                        try:
                            if ls[2][0][0] in scratchBlocks:
                                if goback:
                                    del dep[-1]
                                    ls = dat
                                    for x in dep:
                                        try:
                                            ls = ls[x]
                                        except:
                                            exec('ls = ls["""' + x + '"""]')
                                    
                                else:
                                    dep.append(2)
                                    ls = ls[2]
                        except:
                            pass
                except:
                    pass
                if isdict:
                    if isinstance(ls, list) or isinstance(ls, dict):
                        try:
                            lb.delete(0, END)
                            global lst
                            lst = list()
                            lp = 0
                            for x in lst:
                                del lst[lp]
                                lp = lp + 1
                            lp = 0
                            FONTSIZE = 18
                            for x in ls:
                                try:
                                    if not sets["SHOW SCRIPT FORMATTING"]:
                                        raise TypeError()
                                    lb.insert(END, 'Sprite: ' + str(x['objName']))
                                    t = 'objName'
                                except:
                                    try:
                                        if not sets["SHOW SCRIPT FORMATTING"]:
                                            raise TypeError()
                                        lb.insert(END, 'List: ' + str(x['listName']))
                                        t = 'listName'
                                    except:
                                        try:
                                            if not sets["SHOW SCRIPT FORMATTING"]:
                                                raise TypeError()
                                            lb.insert(END, 'Variable: ' + str(x['label']))
                                            t = 'label'
                                        except:
                                            try:
                                                if not sets["SHOW SCRIPT FORMATTING"]:
                                                    raise TypeError()
                                                lb.insert(END, 'Sound: ' + str(x['soundName']))
                                                t = 'soundName'
                                            except:
                                                try:
                                                    if not sets["SHOW SCRIPT FORMATTING"]:
                                                        raise TypeError()
                                                    lb.insert(END, 'Costume: ' + str(x['costumeName']))
                                                    t = 'costumeName'
                                                except:
                                                    try:
                                                        def getData(lData):
                                                            try:
                                                                formatting = scratchBlocks[lData[0]]['s']
                                                                name = scratchBlocks[lData[0]]['t']
                                                                loopData = 0
                                                                for m in formatting:
                                                                    try:
                                                                        ddt = str(getData(lData[m]))
                                                                    except:
                                                                        ddt = str(lData[m])
                                                                    name = name.replace('§' + str(loopData + 1), '[' + ddt + ']')
                                                                    loopData = loopData + 1
                                                                return name
                                                            except:
                                                                raise RuntimeError()
                                                        if not sets['SHOW SCRIPT FORMATTING']:
                                                            raise TypeError()
                                                        nextTest = False
                                                        lastTest = False
                                                        isScratchItem = False
                                                        ##Do NOT think the tests are in the wrong order (you will see the way this works if you view IF blocks or REPEAT blocks :P)
                                                        try:
                                                            if x[0] in scratchBlocks:
                                                                isScratchItem = True
                                                                dataItem = x
                                                            else:
                                                                nextTest = True
                                                        except:
                                                            nextTest = True
                                                        if nextTest:
                                                            try:
                                                                a = x[0][0]
                                                                if a in scratchBlocks:
                                                                    isScratchItem = True
                                                                    dataItem = x[0]
                                                                
                                                                else:
                                                                    lastTest = True
                                                            except:
                                                                lastTest = True
                                                        if lastTest:
                                                            try:
                                                                if x[2][0][0] in scratchBlocks:
                                                                    isScratchItem = True
                                                                    dataItem = x[2][0]
                                                                else:
                                                                    raise TypeError()
                                                            except:
                                                                raise TypeError()
                                                        if isScratchItem:
                                                            lb.insert(END, getData(dataItem))
                                                            
                                                        else:
                                                            raise TypeError()
                                                    except:
                                                        if str(x) == 'objName':
                                                            lb.insert(END, 'Object Name')
                                                        elif str(x) == 'children':
                                                            lb.insert(END, 'Sprites')
                                                        elif str(x) == 'currentCostumeIndex':
                                                            lb.insert(END, 'Costume #')
                                                        elif str(x) == 'videoAlpha':
                                                            lb.insert(END, 'Video Transparency')
                                                        elif str(x) == 'tempoBPM':
                                                            lb.insert(END, 'Tempo')
                                                        elif str(x) == 'info':
                                                            lb.insert(END, 'Project Info')
                                                        elif str(x) == 'rotationStyle':
                                                            lb.insert(END, 'Rotation Style')
                                                        elif str(x) == 'scratchX':
                                                            lb.insert(END, 'X Position')
                                                        elif str(x) == 'scratchY':
                                                            lb.insert(END, 'Y Position')
                                                        elif str(x) == 'spriteInfo':
                                                            lb.insert(END, 'Sprite Info')
                                                        elif str(x) == 'isDraggable':
                                                            lb.insert(END, 'Is Draggable?')
                                                        elif str(x) == 'scale':
                                                            lb.insert(END, 'Size')
                                                        elif str(x) == 'penLayerMD5':
                                                            lb.insert(END, 'Pen Layer Image')
                                                        elif str(x) == 'indexInLibrary':
                                                            lb.insert(END, 'Image ID')
                                                        elif str(x) == 'penLayerID':
                                                            lb.insert(END, 'Pen Layer ID')
                                                        elif str(x) in scratchBlocks:
                                                            formatting = scratchBlocks[x]['s']
                                                            name = scratchBlocks[x]['t']
                                                            loopData = 0
                                                            for m in formatting:
                                                                try:
                                                                    ddt = str(getData(ls[m]))
                                                                except:
                                                                    ddt = str(ls[m])
                                                                name = name.replace('§' + str(loopData + 1), '[' + ddt + ']')
                                                                loopData = loopData + 1
                                                            lb.insert(END, name)
                                                        else:
                                                            try:
                                                                lb.insert(END, x['name'])
                                                            except:
                                                                if str(x) == '':
                                                                    lb.insert(END, '(Blank string)')
                                                                else:
                                                                    lb.insert(END, str(x))
                                if isinstance(ls, list):
                                    lst.append(lp)
                                else:
                                    lst.append(x)
                                lp = lp + 1
                        except:
                            crash('FATAL ERROR: LOOP FAILED! SHOW THIS LOG TO DYLAN5797! \n' + str(traceback.format_exc()))
                    else:
                        log.add('Editor Opened. Type difference caught with isinstance()')
                        ky = Tk()
                        ky.title('Value Editor')
                        locst = _ScrolledText(parent=ky, text=str(ls), edit=True)
                        while True:
                            try:
                                text = locst.gettext()
                                ky.update()
                            except:
                                break
                        st = ''
                        for z in dep:
                            try:
                                int(z)
                            except:
                                st = st + '[r"""' + str(z) + '"""]'
                            else:
                                st = st + '[' + str(z) + ']'
                        try:
                            itm = 'dat' + st + ' = ' + text
                        except:
                            text.replace('"', r'\"')
                            itm = r'dat' + st + r' = ' + text
                        try:
                            exec(itm)
                        except:
                            try:
                                itm = 'dat' + st + ' = """' + text + '"""'
                                exec(itm)
                            except:
                                log.add('Could not properly format string. This could be due to a malformed buffer object, or usage of triple quotes (""")', 'WARNING')
                                db.showwarning('Could not properly format string. This could be due to a malformed buffer object, or usage of triple quotes (""")')
                        del dep[-1]
                        regenerate_lb()
                else:
                    crash('[REGENERATE LB][ERROR]: E: Could Not format item:\n' + str(traceback.format_exc))
                if len(lb.curselection()) == 0:
                    rmv.config(state=DISABLED)
                else:
                    rmv.config(state=NORMAL)
                
                if len(dep) > 0:
                    back.config(state=NORMAL)
                else:
                    back.config(state=DISABLED)
                    
                if sets['Update JSON Window Every Edit'.upper()]:
                    txt.settext(dat)
                
            fil = os.path.splitext(os.path.split(zipf.filename)[1])[0] + '/project.json'
            try:
                global LOADITM
                stri = zipf.open(fil).read().decode('utf-8')
            except:
                try:
                    stri = zipf.open('project.json').read().decode('utf-8')
                except:
                    log.add('[corruptScratchFile] [' + str(traceback.format_exc()) + ']')
                    crash('ERROR: Invalid Scratch file:\n' + str(traceback.format_exc()))
                else:
                    LOADITM = 'project.json'
            else:
                LOADITM = fil
            global dat
            try:
                dat = json.loads(stri)
            except BaseException as error:
                close_file(areusure=False)
                crash('[LOAD][JSON][DECODER]: Malformed JSON object.\nRaised error as follows\n' + str(error) + '\nExact debug information and exception is below\n' + str(traceback.format_exc()))
            global dat__old
            dat__old = dat
            zipf.close()
            tk.title(fil + ' -ScratchEdit')
            global edw
            edw = Tk()
            edw.title('ScratchEdit (Object Explorer)')
            global areyousure
            def areyousure(e=None):
                if FILE_LOADED:
                    a = db.askyesnocancel('Save on close', 'Do you want to save your changes to ' + os.path.split(loadf)[1] + '?')
                    if a == True:
                        log.add('areYouSure.save()')
                        save()
                    if not (a == None):
                        forcekill(syst=False)
                        return True
                    else:
                        return False
            edw.protocol('WM_DELETE_WINDOW', areyousure)
            tk.protocol('WM_DELETE_WINDOW', areyousure)
            log.add('Protocols for WM_DELETE_WINDOW (X-Button Event) have been set')
            lbsb = Scrollbar(edw)
            try:
                lb = Listbox(edw, width=30, height=15, foreground=sets["TEXT COLOUR"], font=(sets["FONT"], sets['TEXT SIZE']))
            except:
                crash("Problem with Font, Text Size, or Font Colour in ScratchEdit.ini")
            lbsb.pack(side=RIGHT, fill=Y)
            lb.pack()
            dep = []
            lb.config(yscrollcommand=lbsb.set)
            lbsb.config(command=lb.yview)
            global back
            back = Button(edw, text='<Go Back', command=lambda: goback())
            back.pack(side=LEFT)
            rmv = Button(edw, text='Delete', command=lambda: delete())
            rmv.pack(side=RIGHT)
            rn = Button(edw, text='Rename', command=lambda: rename_key())
            rn.pack(side=RIGHT)
            nk = Button(edw, text='New Key', command=lambda: newvalue())
            nk.pack(side=RIGHT)
            bt1 = Button(edw, text='View Value>', command=lambda: select())
            bt1.config(state=DISABLED)
            bt1.pack(side=LEFT)
            regenerate_lb()
            txt.settext(dat)
            def select():
                try:
                    dep.append(lst[sel])
                except:
                    log.add('"View Value>" Button was clicked even though there was no selected item. The button was not disabled!')
                else:
                    regenerate_lb()
            def setsel(e):
                rmv.config(state=NORMAL)
                bt1.config(state=NORMAL)
                global sel
                sel = lb.curselection()[0]
            def goback():
                del dep[-1]
                regenerate_lb(goback=True)
            def delete():
                dep.append(lst[sel])
                st = ''
                for z in dep:
                    try:
                        int(z)
                    except:
                        st = st + '["' + str(z) + '"]'
                    else:
                        st = st + '[' + str(z) + ']'
                itm = 'del dat' + st
                exec(itm)
                del dep[-1]
                regenerate_lb(goback=True)
            def rename_key():
                if type(lst[sel]) == int:
                    db.showerror('Rename','Cannot Rename list item. To rename things like sprites, go into that item and change "Object Name", "Sound Name", etc')
                    return
                rnn = sd.askstring('Rename key', 'Enter a new name for key')
                st = ''
                for z in dep:
                    try:
                        int(z)
                    except:
                        st = st + '["' + str(z) + '"]'
                    else:
                        st = st + '[' + str(z) + ']'
                exec('dat' + st + '["' + rnn + '"] = dat' + st + '["' + lst[sel] + '"]')
                exec('del dat' + st + '["' + lst[sel] + '"]')
                regenerate_lb()
            def newvalue():
                if isinstance(ls, list):
                    ky = Tk()
                    ky.title('List Item #' + str(len(ls)) +  ' -Value Editor')
                    edi = _ScrolledText(ky, edit=True)
                    while True:
                        try:
                            text = edi.gettext()
                            ky.update()
                        except:
                            break
                    st = ''
                    for z in dep:
                        try:
                            int(z)
                        except: 
                            st = st + '["' + str(z) + '"]'
                        else:
                            st = st + '[' + str(z) + ']'
                    itm = 'dat' + st + '.append(' + text + ')'
                    print(itm)
                    try:
                        exec(itm)
                    except:
                        itm = 'dat' + st + '.append("' + text + '")'
                        print(itm)
                        exec(itm)
                    regenerate_lb()
                else:
                    if isinstance(ls, dict):
                        mydef = sd.askstring('Add dict() key', 'Enter the key for the value you are creating')
                        if mydef != None and mydef.rstrip() != '':
                            ky = Tk()
                            ky.title('Value Editor')
                            edi = _ScrolledText(ky, edit=True)
                            while True:
                                try:
                                    text = edi.gettext()
                                    ky.update()
                                except:
                                    break
                            st = ''
                            for z in dep:
                                try:
                                    int(z)
                                except: 
                                    st = st + '["' + str(z) + '"]'
                                else:
                                    st = st + '[' + str(z) + ']'
                            
                            itm = 'dat' + st + '[' + mydef + '] = '      
                            try:
                                exec(itm + '""')
                            except:
                                itm = 'dat' + st + '["' + mydef + '"] = '
                            print(itm + text)
                            try:
                                exec(itm + text)
                            except:
                                print(itm + "'" + text + "'")
                                exec(itm + r"'" + text + r"'")
                            regenerate_lb()
                    else:
                        db.showerror('Invalid object class', 'Sorry, the type of object you are trying to append to is unsupported or invalid')
                    
            lb.bind('<<ListboxSelect>>', setsel)
            back.config(state=DISABLED)
            rn.config(state=DISABLED)
        except:
            print('Exception during client update:')
            print('*' * 60)
            traceback.print_exc(file=sys.stdout)
            print('*' * 60)
            log.add('[GUI][CLIENT UPDATE]: E: EXCEPTION DURING CLIENT UPDATE:\n[' + str(traceback.format_exc()) + ']', header='ERROR')
    else:
        FILE_LOADED = False
def check(e=None):
    if FILE_LOADED == True:
        if areyousure() == True:
            global tk
            tk = Tk()
            tk.title('ScratchEdit')
            generatewidgets()
            load()
    else:
        load()
def save(e=None):
    if FILE_LOADED == True:
        try:
            log.add('Saving...')
            rd = zipfile.ZipFile(loadf, 'r')
            pth = os.path.splitext(os.path.split(loadf)[0] + '\\ ~ ' + os.path.split(loadf)[1])[0] + '.tmp'
            log.add('Saving from ' + str(pth) + ' is being used as reference') 
            zin = zipfile.ZipFile(pth, 'w')
            fn = 'c:\\file.txt'
            p = os.popen('attrib +h ' + pth)
            t = p.read()
            p.close()
            for item in rd.infolist():
                buffer = rd.read(item.filename)
                zin.writestr(item, buffer)
            rd.close()
            zin.close()
            zin = zipfile.ZipFile(pth, 'r')
            zout = zipfile.ZipFile (loadf, 'w')
            for item in zin.infolist():
                buffer = zin.read(item.filename)
                if (item.filename[-5:] != '.json'):
                    zout.writestr(item, buffer)
            try:
                ITEM = json.dumps(dat)
            except BaseException as error:
                crash('JSON ERROR: [\n' + str(traceback.format_exc()), 'JSON')
                #db.showerror('JSONEncoder Exception', 'Malformed JSON object.\nRaised error as follows\n' + str(error) + '\nExact debug information and exception is below\n' + str(traceback.format_exc()))
            zout.writestr(LOADITM, ITEM)
            zout.close()
            zin.close()
            os.remove(pth)
        except:
            crash('ERROR! CHANGES NOT SAVED!!! EXCEPTION: [\n' + str(traceback.format_exc()) + '\n')
        else:
            log.add('Sucessfully Saved')
    else:
        log.add('[SAVE]: E: There is no file loaded', 'CLIENT CATCH')
        db.showerror('Save', 'There is no file loaded')
def close_file(e=None, areusure=True):
    if FILE_LOADED:
        if areusure:
            a = areyousure()
        else:
            a = True
            forcekill(syst=False)
        if a:
            globals()['FILE_LOADED'] = False
            global tk
            tk = Tk()
            tk.title('ScratchEdit')
            generatewidgets()
            doMainLoop()
    else:
        log.add('[CLOSE FILE]: E: There is no file loaded', 'CLIENT CATCH')
        db.showerror('Close File', 'There is no file loaded')
def window_crd(e=None):
    global cm
    cm = Tk()
    cm.title('Credits')
    t = _ScrolledText(cm, text='Loading...', wrap=True)
    cm.update()
    credit = urllib.request.urlopen('https://raw.githubusercontent.com/Dylan5797/ScratchEdit/master/Credits.txt').read().decode()
    t.settext(credit)
def open_forum(e=None):
    webbrowser.open_new('http://scratch.mit.edu/discuss/topic/76008/?page=1')
def open_github(e=None):
    webbrowser.open_new('https://github.com/Dylan5797/ScratchEdit/')
def open_wiki(e=None):
    webbrowser.open_new('https://github.com/Dylan5797/ScratchEdit/wiki')
def open_website(e=None):
    webbrowser.open_new('http://dylan5797.github.io/ScratchEdit/')
def open_dylan5797(e=None):
    webbrowser.open_new('https://sites.google.com/site/dylan5797scratch/')
def forcekill(e=None, mtk=True, syst=True):
    log.add('Under forcekill() call. Destroying {"EditorWindow":"edw", "ValueEditor":"ky", "HelpScreen":"helps", "MainScratchEditWindow":"tk"}')
    try:
        edw.destroy()
    except:
        pass
    try:
        ky.destroy()
    except:
        pass
    try:
        helps.destroy()
    except:
        pass
    try:
        cm.destroy()
    except:
        pass
    try:
        if mtk:
            tk.destroy()
    except:
        pass
    if syst:
        sys.exit()
def quitit(e=None):
    log.add('Quitting.')
    if FILE_LOADED:
        areyousure()
    else:
        forcekill()
def doMainLoop():
    tk.mainloop()
def sedini():
    forcekill(syst=False)
    subprocess.call(['notepad','C:\ProgramData\ScratchEdit\ScratchEdit.ini'])
    os.startfile(__file__)
def generatewidgets():
    log.add('Attempting to make widgets')
    try:
        class hyperlink:
            def __init__(self, url='', text='', mode='down'):
                helpMenu.add_command(label=text, command=self._bind)
                self.url = url
                self.mode = mode
            def _bind(self, event=None):
                if self.mode == 'down':
                    self.rt = Tk()
                    self.rt.title('')
                    self.t = _ScrolledText(self.rt, text='Loading...', wrap=True)
                    self.rt.update()
                    self.credit = urllib.request.urlopen(self.url).read().decode()
                    self.t.settext(self.credit)
                elif self.mode == 'open':
                    webbrowser.open_new(self.url)
        menubar = Menu(tk)
        fileMenu = Menu(tk)
        forum = Menu(tk)
        helpMenu = Menu(tk)
        creditMenu = Menu(tk)
        toolMenu = Menu(tk)
        loggingMenu = Menu(tk)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Load", command=check)
        fileMenu.add_command(label="Save", command=save)
        fileMenu.add_command(label="Close File", command=close_file)
        fileMenu.add_command(label="Exit", command=quitit)
        menubar.add_cascade(label="Online", menu=forum)
        menubar.add_cascade(label="Help", menu=helpMenu)
        menubar.add_cascade(label="Credits", menu=creditMenu)
        creditMenu.add_command(label="Credits", command=window_crd)
        creditMenu.add_command(label="Dylan5797", command=open_dylan5797)
        forum.add_cascade(label="Forum", command=open_forum)
        forum.add_cascade(label="GitHub", command=open_github)
        forum.add_cascade(label="Wiki", command=open_wiki)
        forum.add_cascade(label="Website", command=open_website)
        menubar.add_cascade(label='Tools', menu=toolMenu)
        toolMenu.add_cascade(label='Logging', menu=loggingMenu)
        toolMenu.add_cascade(label='Settings', command=sedini)
        loggingMenu.add_command(label='Log Folder', command=lambda: os.startfile(os.path.split(log.name)[0]))
        dropdown = hyperlink('https://docs.google.com/spreadsheets/d/1uT1vHi6IUUaUix5y3k4p28p2No6pvLNKF_yrtrajEY4/view#gid=0', text='Hacking drop-down menus',mode='open')
        lists = hyperlink('https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdLURkNGNzaUVSYWc', text='List FAQ')
        dicts = hyperlink('https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdS0o3VU5lRGY3VGM', text='Dictionary FAQ')
        ints = hyperlink('https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdMmp0WFBOOGUwWXM', text='Integer FAQ')
        strs = hyperlink('https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdV2F6OVU1OWg2OE0', text='String FAQ')
        tk.configure(menu=menubar)
        global txt
        txt = _ScrolledText(tk)
    except:
        crash('Failed With Exception [\n' + str(traceback.format_exc()) + '\n]')
    else:
        log.add('Call ran.')
generatewidgets()
doMainLoop()
