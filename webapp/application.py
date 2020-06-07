from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)

gr = 0
home_main = "homev7.html"
home_dark = "home-darkv7.html"
grade_main = "gradev7.html"
grade_main_dark = "grade-darkv7.html"
contact_us = "contactv7.html"
contact_us_dark = "contact-darkv7.html"
fin = "finv7.html"
findr = "findarkv7.html"


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
        return "Before 1"

    elif (index >= 16):
        return "16+"

    else:
        return index


@app.route("/")
def home():
    return render_template(home_main)


@app.route("/home-dark")
def homedark():
    return render_template(home_dark)


@app.route("/para_details", methods=["GET", "POST"])
def detpara():
    if request.method == "POST":
        var = request.form.get("subject")
        gr = grade(var)
        return render_template(grade_main, grade=gr)


@app.route("/para_details-dark", methods=["GET", "POST"])
def detparadark():
    if request.method == "POST":
        var = request.form.get("subject")
        gr = grade(var)
        return render_template(grade_main_dark, grade=gr)


@app.route("/contact")
def cont_us():
    return render_template(contact_us)


@app.route("/contact-dark")
def cont_us_dark():
    return render_template(contact_us_dark)


@app.route("/contact_details", methods=["GET", "POST"])
def condet():
    if request.method == "POST":
        mes = request.form.get("message")
        nm = request.form.get("name")
        f = open("messages.txt", "a")
        content = "Name: "+nm+"  Message:"+mes+"\n"
        f.write(content)
        f.close()
    return render_template(fin)


@app.route("/contact_details_dark", methods=["GET", "POST"])
def condetdark():
    if request.method == "POST":
        mes = request.form.get("message")
        nm = request.form.get("name")
        f = open("messages.txt", "a")
        content = "Name: "+nm+"  Message:"+mes+"\n"
        f.write(content)
        f.close()
    return render_template(findr)

'''
if __name__ == "__main__":
    app.run(debug=True)
'''