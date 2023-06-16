import tkinter as tk
import pyshorteners
import pyperclip

def shortner_url():
    lurl = entry.get()
    shortener = pyshorteners.Shortener()
    try:
        if lurl:
            surl = shortener.tinyurl.short(lurl)
            output.config(text=surl)
            return surl
        else:
            output.config(text="Enter the URL")
    except:
        output.config(text="URL is already shorten")
def copy_text():
    pyperclip.copy(shortner_url())
t = tk.Tk()
t.title("URL Shortener")

entry = tk.Entry(t, width=40)
entry.pack(pady=10)

button = tk.Button(t, text="Short URL", command=shortner_url)
button.pack()

output = tk.Label(t, text="")
output.pack(pady=10)
Copy = tk.Button(t, text="Copy URL", command=copy_text)
Copy.pack()

t.mainloop()
