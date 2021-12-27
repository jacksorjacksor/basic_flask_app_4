from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "0e6c689ff68789aca979ecaec7742a69482e4cc39814a4ef"

# Form
class PythonForm(FlaskForm):
    text_input = StringField(label="Text input")
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    form = PythonForm()
    if form.is_submitted():
        dictionary_of_winning_moves = {"R": "P", "P": "S", "S": "R"}
        output = "".join(
            [dictionary_of_winning_moves[move] for move in form.text_input.data]
        )
    else:
        output = None

    return render_template("home.html", form=form, output=output)
