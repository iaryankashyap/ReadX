from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)

gr = 0


def grade(text):
    letters = 0
    words = 0
    sentences = 0
    counter = 0

    for i in text:
        counter += 1

    for i in range(counter):
        # counts the letters using ascii code
        if (ord(text[i]) >= 65 and ord(text[i]) <= 122):
            letters += 1

        # counts the words by reading spaces
        elif (ord(text[i]) == 32 and (ord(text[i - 1]) != 33 and ord(text[i - 1]) != 46 and ord(text[i - 1]) != 63)):
            words += 1

        # counts the sentences by finding dots, exclamation marks and interrogatives
        elif (ord(text[i]) == 33 or ord(text[i]) == 46 or ord(text[i]) == 63):
            sentences += 1
            words += 1
    if words == 0:
        words = 1

    L = letters * 100 / words
    S = sentences * 100 / words
    # Coleman-Liau index is computed using the formula
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Finally outputs the result to the user
    if (index < 1):
        return "Before Grade 1"

    elif (index >= 16):
        return "Grade 16+"

    else:
        return index


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/para_details", methods=["GET", "POST"])
def detpara():
    if request.method == "POST":
        var = request.form.get("subject")
        gr = grade(var)
        return render_template("grade.html", grade=gr)


if __name__ == "__main__":
    app.run(debug=True)
