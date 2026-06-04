import os.path, time

def convert_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024

list = os.listdir("public/music")
total_size = 0
for i in list:
    total_size = total_size + os.path.getsize("public/music/"+i)
total_size = convert_size(total_size)
file = open("src/pages/music/index/index.astro", "w")
file.writelines([
    "---\n",
    "import Head from \"../../../components/Head.astro\";\n",
    "import Header from \"../../../components/Header.astro\";\n",
    "import Footer from \"../../../components/Footer.astro\";\n",
    "---\n",
    "<html>\n",
    "   <head>\n",
    "       <Head title=\"Music Index\" author=\"Clickerty\" />\n",
    "   </head>\n",
    "   <body>\n",
    "       <style>.indexWarning { display: none; } @media screen and (max-width: 636px) { .indexWarning { display:block; } }</style>",
    "       <Header />\n",
    "       <div style=\"padding: 0 20px; min-height: calc(100vh - 229px);\">\n",
    "           <h1>Music Index</h1>\n",
    "           <p><a href=\"/music\">{\"\\u{2190} Back\"}</a></p>",
    "           <p>Files: "+str(len(list))+"</p>\n",
    "           <p>Total size: "+str(total_size)+"</p>\n",
    "            <p class=\"indexWarning\">Your device is too thin, so the table probably isn't rendering too well. Try turning it into landscape mode, if possible.</p>",
    "           <div style=\"padding-bottom: 30px;\">\n",
    "               <table style=\"padding: 0 20px; width: 100%;\">\n",
    "                   <tr><th style=\"width: 50%\">Name</th><th>Modified</th><th>Size</th></tr>\n"])

for i in list:
    file.write("                    <tr><td style=\"text-align: left; padding: 0 10px; word-wrap: break-word; word-break: break-all;\"><a href=\"/music/"+i+"\" style=\"word-wrap: break-word; display: block;\">"+i+"</a></td><td>"+str(time.ctime(os.path.getmtime("public/music/"+i)))+"</td><td>"+str(convert_size(os.path.getsize("public/music/"+i)))+"</td></tr>\n")

file.writelines([
    "               </table>\n",
    "           </div>\n",
    "       </div>\n",
    "       <Footer />\n",
    "   </body>\n",
    "</html>"
])
file.close()