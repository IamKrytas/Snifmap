from flask import Flask, Response, request, render_template, redirect, url_for
import os
import snifmap

app = Flask(__name__)
app.secret_key = "0123456789"

# service home page
@app.route("/")
def home():
    return render_template("home.html")

# service upload file
@app.route("/", methods=["POST"])
def map():
    try:
        file = request.files["file"]
        jsons = os.path.join("jsons")
        if not os.path.exists(jsons):
            os.makedirs(jsons)

        file.save(os.path.join(jsons, file.filename))

        path = f"jsons/{file.filename}"

        directory = snifmap.get_map(path)

        with open(directory, "r") as f: # read html file with map
            content = f.read()
        return Response(content, content_type="text/html")
    except:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)