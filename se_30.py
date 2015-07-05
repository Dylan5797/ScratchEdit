import shutil
import sys
import traceback
import tkinter.messagebox as mb
import zipfile
import getpass
import time
import urllib.request
import io
import tkinter.messagebox as db
import os
from tkinter import *
class _ScrolledText(Frame):
	def __init__(self, parent=None, text=''):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN, background='Black', foreground='White', selectbackground='Green', font=('Arial'))
        sbar.config(command=text.yview)               
        text.config(yscrollcommand=sbar.set)           
        text.config(state=NORMAL)
        sbar.pack(side=RIGHT, fill=Y)                 
        text.pack(side=LEFT, expand=YES, fill=BOTH)  
        self.text = text
    def settext(self, text=''):
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.insert('1.0', text) 
        self.text.mark_set(INSERT, END)          
        self.text.focus()
        self.text.config(state=DISABLED)
    def gettext(self):                             
        return self.text.get('1.0', END+'-1c')      
    def print(self, value, end='\n'):
        self.settext(text=self.gettext() + value + end)
        self.text.see(END)
def install():
    tk = Tk()
    tk.title('ScratchEdit Installer')
    st = _ScrolledText(parent=tk)
    st.print('ScratchEdit Installer 1.0. Running...')
    try:
        shutil.rmtree('C:\\ProgramData\\ScratchEdit', ignore_errors=True)
    except:
        pass
    st.print('Libraries configured.')
    st.print('Downloading queue jobs...')
    try:
        tk.update()
        queue = urllib.request.urlopen('https://raw.githubusercontent.com/Dylan5797/ScratchEdit/master/sedit_update_update_root.json')
    except:
        st.print('Failed.')
        st.print('Could not download queue jobs.')
        tk.update()
        time.sleep(2)
        tk.destroy()
        sys.exit()
    else:
        st.print('Queue jobs loaded.')
        queue = eval(queue.read().decode('utf-8'))
        tk.update()
        time.sleep(0.5)
        st.print('')
        st.print(queue["installationComment"].replace('.nl', '\n'))
        st.print('')
        tk.update()
        time.sleep(0.5)
        st.print("Processing Queued Downloads...")
        st.print("- Libraries and Resources -")
        tk.update()
        try:
            print(queue["downloads"]["installationUrl"])
            rq = urllib.request.urlopen(queue["downloads"]["installationUrl"]).read()
        except:
            st.print("Failed: Retrieve Root Libraries")
            tk.update()
            time.sleep(2)
            sys.exit()
        else:
            st.print('Libraries and Resources: Read cached URL contents. Writing data to IO (BytesIO) file buffer to be decoded and extracted')
            try:
                zipf = zipfile.ZipFile(io.BytesIO(rq))
                zipf.extractall('C:\\ProgramData')
            except:
                st.print('Buffer failed.')
                tk.update()
                time.sleep(2)
                sys.exit()
            else:
                st.print('Libraries and Resources: Job Done')
            st.print('- ScratchEdit ' + queue["updateAvailable"] + ' -')
            try:
                sEdit = urllib.request.urlopen(queue["downloads"]["updatedScratchEditUrl"]).read().decode('utf-8')
            except:
                st.print('ScratchEdit ' + queue["updateAvailable"] + ': Download Failed')
                tk.update()
                time.sleep(2)
                sys.exit()
            else:
                st.print('ScratchEdit ' + queue["updateAvailable"] + ': Download Ran.')
                st.print('ScratchEdit ' + queue["updateAvailable"] + ': Writing Files...')
                f = open('C:\\ProgramData\\ScratchEdit\\ScratchEdit.pyw', 'w', encoding='utf-8')
                f.write(sEdit)
                f.close()
                f = open('C:\\ProgramData\\ScratchEdit\\Version.txt', 'w')
                f.write(str(queue["updateAvailable"]))
                f.close()
                st.print('ScratchEdit ' + queue["updateAvailable"] + ': Done')
                st.print('- Shortcut -')
                #if mb.askyesno('ScratchEdit Installer', r"Do you want to put a shortcut on you desktop? ScratchEdit can still be accessed in C:\ProgramData\ScratchEdit\ScratchEdit.pyw if you don't have a shortcut"):
                a = open('C:\\Users\\' + getpass.getuser() + '\\Desktop\\ScratchEdit.pyw', 'w', encoding='utf-8')
                a.write('import os\nos.startfile("C:\\ProgramData\\ScratchEdit\\ScratchEdit.pyw")')
                a.close()
                st.print('Shortcut: Done')
                st.print('ScratchEdit has been installed')

if __name__ == "__main__":
    install()
