from flask import Flask, render_template, request, redirect, url_for
import  bacnd
import dbf
app = Flask(
    __name__,
    template_folder = 'template'
)

@app.route("/")
def index():
    bacnd.main()
    texts=dbf.select_titles_fromtable("NASAclimate")
    urls=dbf.select_link_fromtable("NASAclimate")
    texts1=dbf.select_titles_fromtable("thegaurdian")
    urls1=dbf.select_link_fromtable("thegaurdian")
    texts2=dbf.select_titles_fromtable("greenpeace")
    urls2=dbf.select_link_fromtable("greenpeace")
    return render_template('index.html',urls=urls,texts=texts,urls1=urls1,texts1=texts1,urls2=urls2,texts2=texts2)


if __name__ == '__main__':
    app.run(debug=True)
