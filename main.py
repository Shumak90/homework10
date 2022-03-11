from flask import Flask
from candidates import candidates_json

app = Flask(__name__)

@app.route("/")
def hello():
    data = ""
    for candidate in candidates_json():
        data += f"Имя кандидата {candidate['name']}\n"
        data += f"Позиция кандидата {candidate['position']}\n"
        data += f"Навыки через запятую {candidate['skills']}\n\n"
    return f"<pre>{data}<pre>"


@app.route("/candidate/<x>")
def candidate(x):
    data = ""
    jepeg = ""
    for candidate in candidates_json():
        if int(x) == candidate["id"]:
            data += f"Имя кандидата {candidate['name']}\n"
            data += f"Позиция кандидата {candidate['position']}\n"
            data += f"Навыки через запятую {candidate['skills']}\n\n"
            jepeg += candidate["picture"]
    return f'<img src="{jepeg}">' \
           f'<pre>{data}<pre>'

@app.route("/skill/<x>")
def skill(x):
    data = ""
    for candidate in candidates_json():
        if x.lower() in candidate['skills'].lower():
            data += f"Имя кандидата {candidate['name']}\n"
            data += f"Позиция кандидата {candidate['position']}\n"
            data += f"Навыки через запятую {candidate['skills']}\n\n"
    return f"<pre>{data}<pre>"

if __name__ == "__main__":
    app.run()