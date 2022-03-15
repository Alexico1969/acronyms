from flask import Flask, render_template, request
from acronym import acronym

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    method = request.method
    if method == "POST":
        inp = request.form["words_input"]
        acronyms = acronym(inp)
        return render_template("acronyms.html", inp=inp, acronyms=acronyms)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)