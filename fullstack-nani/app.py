import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        location = request.form["location"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(location),
            temperature=1,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(location):
    return """Sugiere tres nombres para una startup en

Industrias: Tecnología
Nombres: TechWave, CodeHive, DigitalDream
Industrias: Comida
Nombres: FlavorFusion, KitchenKraze, PlatePals
Industrias: {}
Nombres:""".format(
        location.capitalize()
    )

