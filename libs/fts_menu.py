import os

_CLEAR_="clear"

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

class menu():
    name=""
    text=""
    options=[["name Option","Menu name toGo"]]
    selected=0
    def __init__(self):
        self.name=""
        self.text=""
        self.options=[["name Option","Menu name toGo"]]
        self.selected=0
    def set(self,name,text,options):
        self.name=name
        self.text=text
        self.options=options
        self.selected=0
    def draw(self):
        os.system(_CLEAR_)
        print self.name
        print " "
        print self.text
        print " "
        i=0
        for op in self.options:
            print i+1 , ". " , op[0]
            i+=1
    def select(self):
        self.selected=raw_input("Select: ")
        if(check_int(self.selected)):
            self.selected=int(self.selected)
        if(self.selected>0 and self.selected<=len(self.options)):
            a=self.options[self.selected-1]
            if(len(a)>1):
                return a[1];            
        return -1
    def fanOption(self,option_name):
        i=0
        for op in self.options:
            if(option_name==op[0]):
                return i
            i+=1
        return -1


class fts_menu():
    menu_Actual=0
    menus=[]
    def __init__(self):
        self.menu_Actual=0
        self.menus=[]
    def addMenu(self, name, text, options):
        data=self.fanMenu(name)
        if(data!=-1):
            self.menus[data].set(name,text,options)
        else:
            x=menu()
            x.set(name,text,options)
            self.menus.append(x)
    def fanMenu(self, name):
        i=0
        for (a) in self.menus:
            if(a.name==name):
                return i
            i+=1
        return -1
    def run(self):
        self.menus[self.menu_Actual].draw()
        ac=self.fanMenu(self.menus[self.menu_Actual].select())
        ant=self.menu_Actual
        if(ac!=-1):
            self.menu_Actual=ac
        return [ant,self.menus[ant].selected]
    def goto(self,name):
        data=self.fanMenu(name)
        if(data!=-1):
            self.menu_Actual=data
    def fanselected(self,name,opcion_name):
        data=self.fanMenu(name)
        op=-1
        if(data!=-1):
            op=self.menus[data].fanOption(opcion_name)+1            
        return [data,op]


def validator(title,msg,data=[]):
    a=[-1,-1]
    m=fts_menu()
    m.addMenu(title,msg,data)
    while(a==[-1,-1]):
        a=m.run()
        if(a[1]!=-1):
            return data[a[1]-1][0]