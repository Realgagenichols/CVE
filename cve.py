import tkinter as tk
import tkinter.font as tkFont
from urllib import request
from urllib.error import HTTPError
from urllib.request import urlopen, Request
import re
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def getCVEs(url):
    pattern = "CVE-\d\d\d\d-\d{3,}"

    try:
        req = request.Request(url, headers={'User-Agent' : "Magic Browser"})
        page = urlopen(req)
    except HTTPError:
        print(HTTPError)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    cves = re.findall(pattern, html, re.IGNORECASE)
    cves = list(set(cves))
    cves = ','.join(cves)

    return cves

root = tk.Tk()

def clicked():
    urlToGet = urlEntry.get()
    output.delete(0.0, tk.END)
    try:
        listCVE = getCVEs(urlToGet)
    except:
        listCVE = "ERR: Unable to get CVEs"
    output.insert(tk.END, listCVE)

#setting title
root.title("Get CVEs")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

lbl=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
lbl["font"] = ft
lbl["fg"] = "#333333"
lbl["justify"] = "center"
lbl["text"] = "URL"
lbl.place(x=250,y=40,width=70,height=25)

urlEntry=tk.Entry(root)
urlEntry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
urlEntry["font"] = ft
urlEntry["fg"] = "#333333"
urlEntry["justify"] = "center"
urlEntry["text"] = ""
urlEntry.place(x=150,y=70,width=278,height=30)

getCVEButton=tk.Button(root)
getCVEButton["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
getCVEButton["font"] = ft
getCVEButton["fg"] = "#000000"
getCVEButton["justify"] = "center"
getCVEButton["text"] = "get CVEs"
getCVEButton.place(x=250,y=120,width=70,height=25)
getCVEButton["command"] = clicked

output=tk.Text(root)
output["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
output["font"] = ft
output["fg"] = "#333333"
#output["justify"] = "center"
output["wrap"] = "word"
output.place(x=80,y=190,width=413,height=182)

root.mainloop()