import os, json


from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'dados/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        with open(destination) as f:
            data = json.load(f)
        print(data)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html", data=data)

#@app.route('/upload/<filename>')
#def send_image(filename):
#   return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run( debug=True)