from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

session_token = "12345"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/puzzle-1")
def puzzle_1():
    return render_template("puzzle_1.html")

@app.route("/puzzle-2")
def puzzle_2():
    return render_template("puzzle_2.html")

@app.route("/puzzle-3")
def puzzle_3():
    return render_template("puzzle_3.html")

@app.route("/puzzle-4")
def puzzle_4():
    return render_template("puzzle_4.html")

@app.route("/puzzle-5")
def puzzle_5():
    return render_template("puzzle_5.html")

@app.route("/puzzle-6-113")
def puzzle_6():
    return render_template("puzzle_6.html")

@app.route("/puzzle-7")
def puzzle_7():
    return render_template("puzzle_7.html")

@app.route("/solved-page")
def solved_page():
    return render_template("solved_page.html")

@app.route("/7")
def prime():
    return jsonify({True})

@app.route("/puzzle-code", methods=['POST'])
def puzzle_code():
    data = request.get_json()
    puzzle = data["puzzle"]
    code = data["code"]

    if puzzle == "o":
        if code != "thesecretsofgamedesign":
            return jsonify({"correct": False})
    elif puzzle == "1":
        if code != "142045":
            return jsonify({"correct": False})
    elif puzzle == "2":
        if code != "325965":
            return jsonify({"correct": False})
    elif puzzle == "3":
        if code != "130367":
            return jsonify({"correct": False})
    elif puzzle == "4":
        if code != "410283":
            return jsonify({"correct": False})
    elif puzzle == "5":
        if code != "856391":
            return jsonify({"correct": False})
    elif puzzle == "6":
        if code != "458547":
            return jsonify({"correct": False})
    elif puzzle == "7":
        if code != "PARADOX":
            return jsonify({"correct": False})

    return jsonify({"correct": True})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
