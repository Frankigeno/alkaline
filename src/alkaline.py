import xml.etree.ElementTree as ET
import sys
from os import system, name

class Engine:

    def __init__(self, path: str):
        '''
        Specify the path to HTML template.
        NB: close all the tags on HTML file.
        '''
        self.keywords = {}
        self.vars = {}
        self.content = open(path).read()

    def replace(self):
        '''
        Replace keywords in template with the values in vars dict 
        '''
        cont = self.content.split("\n")

        for i in self.keywords:
            if i not in self.vars:
                raise Exception(f"Variable {i} not declared!")

            cont[self.keywords[i]["line"]] = cont[self.keywords[i]["line"]].replace(f"${i}$", str(self.vars[i]))

        self.content = ""
        for line in cont:
            self.content += line + "\n"
        
        return self.content

    def execPython(self):
        '''
        Execute all the Python code in the template.
        '''
        root = ET.parse("template.html").getroot()
        pyCode = ""
        for tag in root.findall("python"):
            for i in str(tag.text).splitlines():
                pyCode += i[4:] + "\n"
            root.remove(tag)
            
        for tag in root.findall("head/python"):
            for i in str(tag.text).splitlines():
                pyCode += i[4:] + "\n"
            root.remove(tag)

        for tag in root.findall("body/python"):
            for i in str(tag.text).splitlines():
                pyCode += i[4:] + "\n"
            root.remove(tag)
        
        self.content = ET.tostring(root, encoding='unicode', method='xml')
        for line in self.content.split("\n"):
            start = 0
            end = 0
            for char in range(len(line)):
                if line[char] == "$" and start == 0:
                    start = char

                elif line[char] == "$" and start > 0:
                    end = char
                    self.keywords[line[start + 1: end]] = {"start": start, "end": end, "line": self.content.split("\n").index(line)}
                    start = 0
                    end = 0

        def tag(type: str, innerText: str = "", attributes: dict = {}) -> str:
            attrs = ""
            for i in attributes:
                attrs += f' {i}="{attributes[i]}"'
            return f"<{type}{attrs}>{innerText}</{type}>"

        exec(pyCode)

    def compile(self, var: dict = {}):
        '''
        Do all the actions to compile an entire template. Accept as argument the content of vars
        '''
        self.vars = var
        self.execPython()
        self.replace()
        return self.content

if __name__ == "__main__":
    # for windows
    if name == 'nt':
       system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

    # titles
    print("""
     █████╗ ██╗     ██╗  ██╗ █████╗ ██╗     ██╗███╗   ██╗███████╗
    ██╔══██╗██║     ██║ ██╔╝██╔══██╗██║     ██║████╗  ██║██╔════╝
    ███████║██║     █████╔╝ ███████║██║     ██║██╔██╗ ██║█████╗  
    ██╔══██║██║     ██╔═██╗ ██╔══██║██║     ██║██║╚██╗██║██╔══╝  
    ██║  ██║███████╗██║  ██╗██║  ██║███████╗██║██║ ╚████║███████╗
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
    """)
    print("## version 1.0 debugger ##")
    print("All the changes will automatically detected and rendered")

    # initial rendering
    print("rendering...")

    try:
        prev = open(sys.argv[1]).read()

    except IndexError:
        print("Write a valid file path")
        exit()

    except FileNotFoundError:
        print("Enter a valid file name")
        exit()
    
    path = sys.argv[1]
    eng = Engine(path)
    open("index.html", "w").write(eng.compile())
    print("done")
        
    while 1:
        if prev != open(sys.argv[1]).read():
            try:
                print("re-rendering...")
                path = sys.argv[1]
                eng = Engine(path)
                open("index.html", "w").write(eng.compile())
                prev = open(sys.argv[1]).read()
                print("done!")

            except Exception as e:
                print(e)
                prev = open(sys.argv[1]).read()

