from mako.template import Template
import json
import pyperclip

def generateAbb(words):

    s = "" 
    for word in words:
        s += "\\textbf{" + word[0] + "}" + word[1:] +" "
    return s


f = open('abb.json')
data = json.load(f)

results:str = ""

for key in data:
    results += Template("""
    \sortitem[${abbrev}]{
            \\begin{minipage}[l]{0.15\columnwidth}
                \\textbf{${abbrev}}
            \end{minipage}
            \\begin{minipage}[l]{0.05\columnwidth}
                \\textbf{=}
            \end{minipage}
            \\begin{minipage}[l]{0.8\columnwidth}
                ${text}
            \end{minipage}}
    """).render(abbrev=key,text=generateAbb(data[key].split()))

pyperclip.copy(results)