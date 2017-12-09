#!python3.4
"""ScratchEdit editor by Dylan Beswick and wizzwizz4"""
global scratchBlocks
global version
version = '4.0.0-beta'
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
import io
import collections
import zipfile
import subprocess
import traceback
import random
import pprint
import json
import webbrowser
import argparse
import configparser
# Done imports (except for some later on)

parser = argparse.ArgumentParser(add_help = False)
parser.add_argument('--error', required = False)
args = parser.parse_args()
del parser  # Possibly suggests that this should be a utility function.

if args.error is not None:
    print(args.error)
    sys.stdin.readline(0)  # Wait for user.
    sys.exit(1)

#########
# utils #
#########

def fatal_error(errors):
    err_text = '\n'.join(errors) + '\nPress return to close'
    subprocess.call([sys.executable.replace('pythonw', 'python'),
                     __file__, '--error', err_text])
    sys.exit()

def crash(error,header='ERROR',raw=False,c=True,sysexit=True,openlogfile=True):
    log.add(error,header,raw=raw,c=c)
    if openlogfile:
        os.startfile(log.name)
    if sysexit:
        os._exit(1)

def create_data_files(base_path = r'C:\ProgramData\ScratchEdit'):
    # TODO: Don't hardcode base_path's default value - use `is None` idiom.
    # PORT: base_path should autodetect based on OS.
    for subdir in ('.logging',):  # Must contain at least one directory!
        path = os.path.join(base_path, subdir)
        if not os.path.isdir(path):
            os.makedirs(path)
    config_path = os.path.join(base_path, 'ScratchEdit.ini')
    if not os.path.isfile(config_path):
        with open(config_path, 'w') as fh:
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

def check_for_update(url = 'https://raw.githubusercontent.com/Dylan5797/'
                           'ScratchEdit/current-update/latestupdate.txt',
                     current_version = version):
    def run_in_thread(url, version):
        try:
            r = (urllib.request.urlopen(url).read()
                 .decode('utf-8').replace('\n', ''))
        except:
            log.add('Update check failed.',header='ERROR')
            return
        log.add(('Latest version is v{}. '
                 'Current version is v{}.').format(r, version))
        if str(r) == version:
            log.add('No update available.')
            os._exit()
        log.add('Update available. Prompting user.')
        t = Tk()
        t.withdraw()
        if db.askyesno('ScratchEdit Update',
                       'A Newer version of ScratchEdit is available: ' +
                       r + '\nDo you want to install it?', master = t):
            f = urllib.request.urlopen('https://raw.githubusercontent.com/'
                                       'Dylan5797/ScratchEdit/master/'
                                       'ScratchEdit.pyw').read()
            with open(__file__, 'wb') as fr:
                fr.write(f)
            
            os.startfile(__file__)
            os._exit()
    threading.Thread(target=run_in_thread,
                     args=(url, version)).start()

########## These exist solely to cushion the blow
# Legacy # of having a full refactor all at once.
########## Remove them once they're no longer used.

def old_load_settings():
    """This function is deprecated. We're trying to migrate away from it."""
    BOOLS = ("show", "check", "update")
    INTS = ("size")
    
    class LegacyMapView:
        """Do not ever use this class outside of its function."""
        
        def __init__(self, config):
            self.config = config

        def __getitem__(self, key):
            for section_name in config.sections():
                if key in config[section_name]:
                    section = config[section_name]
                    break
            else:
                raise KeyError(key)
            # Here be dragons.
            # Actually, heuristics. (Same thing.)
            if any(subkey in key.casefold() for subkey in BOOLS):
                return section.getboolean(key)
            if any(subkey in key for subkey in INTS):
                return section.getint(key)
            return section[key]
    
    config = configparser.ConfigParser()
    config.read(r"C:\ProgramData\ScratchEdit\ScratchEdit.ini")
    return LegacyMapView(config)

#####################
# Check environment #
#####################

errors = []
if not int(platform.python_branch().replace('.','')[1:]) > 339:
    errors.append(('ScratchEdit is made for Python "v3.4.0" but your '
                   'Python version is "{}"').format(platform.python_branch()))

try:
    import tkinter
except ImportError:
    errors.append("tkinter wasn't installed during Python installation!! "
                  "ScratchEdit cannot be used if Python has not been "
                  "installed with the official installer OR you have "
                  'unchecked "Tcl/IDLE" in the installer. '
                  "Please reinstall Python and do it right.")
else:
    del tkinter

if not platform.uname().system == 'Windows':
    errors.append('You have to be using Windows to run ScratchEdit!')

if errors:
    fatal_error(errors)

del errors

global pp
pp = pprint.PrettyPrinter(indent=4, compact=True)
from tkinter import *
from tkinter.ttk import *
class _ScrolledText(Frame):
    # TODO: tkinter.scrolledtext exists, but has different API.
    #       Avoid reimplementing the wheel.
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

create_data_files()

time.sleep(0.01)  # TODO: What is this for?!

sets = old_load_settings()

class Log():
    def __init__(self, text='ScratchEdit ' + str(version),
                 base_path = r'C:\ProgramData\ScratchEdit'):
        self.time = self.timestamp()
        self.name = os.path.join(base_path, '.logging', self.time + '.txt')
        with open(self.name, 'w') as a:
            a.write(text + ' --' + self.timestamp(False) + '\n')
    
    def add(self, value, header='INFO', raw=False, c=True):
        with open(self.name, 'a') as f:
            if raw:
                f.write(str(value))
            else:
                if c:
                    f.write("{} [{}]: {}\n".format(self.timestamp(False),
                                                   header, value))
                else:
                    f.write("\n{} [{}]: {}\n".format(self.timestamp(False),
                                                     header, value))

    @staticmethod
    def get_current_time(file_safe = True):
        if file_safe:
            return time.strftime('[%H.%M.%S]')
        else:
            return time.strftime('[%H:%M:%S]')
    
    @staticmethod
    def get_current_date(file_safe = True):
        if file_safe:
            return time.strftime('[%y-%m-%d]')
        else:
            return time.strftime('[%y/%m/%d]')

    @staticmethod
    def timestamp(file_safe = True):
        if file_safe:
            return time.strftime('[%y-%m-%d %H.%M.%S]')
        else:
            return time.strftime('[%y/%m/%d %H:%M:%S]')

import tkinter.messagebox as db
import tkinter.filedialog
import tkinter.simpledialog as sd
if sets["Check For Update at Startup"]:
    check_for_update()
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
            crash('[corruptScratchFile]: Could not read archive [\n' + str(traceback.format_exc()) + ']')
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
                    except KeyError:
                        # TODO: Log this.
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
                    tk.config(cursor='wait')
                    txt.settext('Loading...')
                    txt.update()
                    txt.settext(pp.pformat(dat))
                tk.config(cursor='')
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
            def areyousure(e=None, fc=True):
                if FILE_LOADED:
                    a = db.askyesnocancel('Save on close', 'Do you want to save your changes to ' + os.path.split(loadf)[1] + '?')
                    if a == True:
                        log.add('areYouSure.save()')
                        save()
                    if (not (a == None)) and fc: 
                        forcekill(syst=False)
                    return a
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
            tk.config(cursor='wait')
            txt.settext(pp.pformat(dat))
            txt.update()
            tk.config(cursor='')
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
            log.add('Callback Error:\n[' + str(traceback.format_exc()) + ']', header='ERROR')
    else:
        FILE_LOADED = False
def check(e=None):
    if FILE_LOADED == True:
        if areyousure(fc=False) != None:
            forcekill(syst=False)
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
            blank_zip = b'PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            log.add('Saving...')
            rd = zipfile.ZipFile(loadf, 'r')
            i = io.BytesIO(blank_zip)
            log.add('Saving file. ' + str(i) + ' is being used as reference') 
            zin = zipfile.ZipFile(i, 'w')
            for item in rd.infolist():
                buffer = rd.read(item.filename)
                zin.writestr(item, buffer)
            rd.close()
            zin.close()
            zin = zipfile.ZipFile(i, 'r')
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
        except:
            rec = 'C:\\ProgramData\\ScratchEdit\\recoveredJSON-' + str(random.randint(100000000, 999999999)) + '.json'
            x = open(rec, 'w')
            x.write(str(dat))
            x.close()
            crash('ERROR! CHANGES NOT SAVED!!! EXCEPTION: [\n' + str(traceback.format_exc()) + '\n JSON For Recovery follows: ' + rec)
        else:
            log.add('Sucessfully Saved')
    else:
        log.add('[SAVE]: E: There is no file loaded', 'CRITICAL STOP')
        db.showerror('Save', 'There is no file loaded')
def close_file(e=None, areusure=True):
    if FILE_LOADED:
        a = areyousure(fc=False)
        if a != None:
            a = True
            forcekill(syst=False)
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
def delete_logs(e=None):
    yesno = db.askyesno('Delete logs', 'Are you sure you want to delete the logs?')
    if yesno:
        for x in os.listdir(os.path.split(log.name)[0]):
            if not (os.path.split(log.name)[0] + '\\' + x == log.name):
                os.remove(os.path.split(log.name)[0] + '\\' + x)
def sedini():
    if FILE_LOADED:
        a = areyousure()
        if a == False:
            a = True
    else:
        a = True
    if a:
        subprocess.call(['notepad','C:\ProgramData\ScratchEdit\ScratchEdit.ini'])
        os.startfile(__file__)
def generatewidgets():
    log.add('Attempting to make widgets')
    try:
        class hyperlink:
            def __init__(self, menu, url='', text='', mode='down'):
                menu.add_command(label=text, command=self._bind)
                self.url = url
                self.mode = mode
            def _bind(self, event=None):
                if self.mode == 'down':
                    self.rt = Tk()
                    self.rt.title('')
                    self.t = _ScrolledText(self.rt, text='Loading...', wrap=True)
                    self.rt.update()
                    try:
                        self.credit = urllib.request.urlopen(self.url).read().decode()
                    except:
                        db.showerror('Could Not Connect', 'Could not download help.')
                        self.rt.destroy()
                        return
                    self.t.settext(self.credit)
                elif self.mode == 'open':
                    webbrowser.open_new(self.url)
        menubar = Menu(tk)

        fileMenu = Menu(tk)
        online = Menu(tk)
        creditMenu = Menu(tk)
        toolMenu = Menu(tk)
        helpMenu = Menu(tk)
        loggingMenu = Menu(tk)
        
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Online", menu=online)
        menubar.add_cascade(label="Credits", menu=creditMenu)
        menubar.add_cascade(label='Tools', menu=toolMenu)
        menubar.add_cascade(label="Help", menu=helpMenu)
        
        fileMenu.add_command(label="Load", command=check)
        fileMenu.add_command(label="Save", command=save)
        fileMenu.add_command(label="Close File", command=close_file)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=quitit)
        
        creditMenu.add_command(label="Credits", command=window_crd)
        dylan5797 = hyperlink(menu=creditMenu, url='https://sites.google.com/site/dylan5797scratch/', text='Dylan5797', mode='open')
        wizzwizz4 = hyperlink(menu=creditMenu, url='https://github.com/wizzwizz4', text='wizzwizz4', mode='open')

        forumLink = hyperlink(menu=online, url='http://scratch.mit.edu/discuss/topic/76008/?page=1', text='Forum', mode='open')
        githubLink = hyperlink(menu=online, url='https://github.com/Dylan5797/ScratchEdit/', text='GitHub', mode='open')
        wikiLink = hyperlink(menu=online, url='https://github.com/Dylan5797/ScratchEdit/wiki', text='Wiki', mode='open')
        webLink = hyperlink(menu=online, url='http://dylan5797.github.io/ScratchEdit/', text='Website', mode='open')
        
        toolMenu.add_cascade(label='Logging', menu=loggingMenu)
        toolMenu.add_command(label='Settings', command=sedini)
        toolMenu.add_separator()
        toolMenu.add_command(label='Version ' + str(version))
        toolMenu.entryconfig(4, state=DISABLED)
        
        loggingMenu.add_command(label='Log Folder', command=lambda: os.startfile(os.path.split(log.name)[0]))
        loggingMenu.add_command(label='Delete Logs', command=delete_logs)
        
        dropdown = hyperlink(helpMenu, 'https://docs.google.com/spreadsheets/d/1uT1vHi6IUUaUix5y3k4p28p2No6pvLNKF_yrtrajEY4/view#gid=0', text='Hacking drop-down menus', mode='open')
        helpMenu.add_separator()
        lists = hyperlink(menu=helpMenu, url='https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdLURkNGNzaUVSYWc', text='List FAQ')
        dicts = hyperlink(menu=helpMenu, url='https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdS0o3VU5lRGY3VGM', text='Dictionary FAQ')
        ints = hyperlink(menu=helpMenu, url='https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdMmp0WFBOOGUwWXM', text='Integer FAQ')
        strs = hyperlink(menu=helpMenu, url='https://drive.google.com/uc?export=download&id=0B_v6u8n56nAdV2F6OVU1OWg2OE0', text='String FAQ')
        
        tk.configure(menu=menubar)
        global txt
        txt = _ScrolledText(tk)
    except:
        crash('Failed With Exception [\n' + str(traceback.format_exc()) + '\n]')
    else:
        log.add('Call ran.')
generatewidgets()
doMainLoop()
