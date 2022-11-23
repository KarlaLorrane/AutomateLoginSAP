import win32com.client
import subprocess
import sys
import time
from tkinter import *
from tkinter import messagebox

class SapGui(object):
    def __init_(self):
        self.path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(self.path)

        self.SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine

        self.connection = application.OpenConnection("description conection sap", True)
        time.sleep(3)
        self.session = self.connectionChildren(0)
        self.session.findById("wnd[0]").maximize

    def sapLogin(self):
        try:
            self.sessionfindById("wnd[0]/usr/txtRSYST-MANDT").text = "mandante"
            self.sessionfindById("wnd[0]/usr/txtRSYST-BNAME").text = "user"
            self.sessionfindById("wnd[0]/usr/pwdRSYST-BCODE").text = "password"
            self.sessionfindById("wnd[0]/usr/txtRSYST-LANGU").text = "EN"
            self.sessionfindById("wnd[0]").sendVKey(0)

        except:
            print(sys.exc_info()[0])
        messagebox.showinfo("showinfo","Login realizado com sucesso!")
if __name__ == '__main__':
    window = Tk()
    window.geometry("200x50")
    button = Button(window, text="Login SAP", command= lambda :SapGui().sapLogin())
    button.pack()
    mainloop()
