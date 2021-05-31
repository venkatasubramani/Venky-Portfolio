from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)



@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    name = "Venkatasubramani Karthikeyan"
    return render_template("index.html",name = name)

@app.route("/home")
def home():
    name = "Venkatasubramani Karthikeyan"
    return render_template("index.html",name = name)

@app.route("/edu")
def edu():
    name = "Venkatasubramani Karthikeyan"
    return render_template("edu.html",name = name)

@app.route("/exp")
def exp():
    name = "Venkatasubramani Karthikeyan"
    return render_template("exp.html",name = name)

@app.route("/skillset")
def skillset():
    name = "Venkatasubramani Karthikeyan"
    return render_template("skillset.html",name = name)

@app.route("/hobbies")
def hobbies():
    name = "Venkatasubramani Karthikeyan"
    return render_template("hobbies.html",name = name)

@app.route("/edu_exp")
def venky():
    return render_template("edu_exp.html")

# @app.route('/files/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     return send_from_directory(directory=os.getcwd()+"/files", filename="/venky_resume.pdf")

# @app.route("/files/Venky_resume.pdf")
# def DownloadLogFile ():
#     try:
#         return send_file("/static/Venky_resume.pdf", as_attachment=True)
#     except Exception as e:
#         self.log.exception(e)
#         self.Error(400)

@app.route('/static/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    static = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=static, filename=filename)

# @app.route('/download')
# def downloadFile ():
#     #For windows you need to use drive name [ex: F:/Example.pdf]
#     path = "/static/Venky_resume.pdf"
#     return send_file(path, as_attachment=True)