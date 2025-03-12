from flask import Flask, render_template, request

app = Flask(__name__)

def decimal_to_binary(n):
    return bin(n)[2:]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    number = None
    if request.method == "POST":
        number = int(request.form["number"])
        result = decimal_to_binary(number)
    return render_template("index.html", result=result, number=number)

if __name__ == "__main__":
    app.run(debug=True)
