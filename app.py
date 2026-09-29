#!/usr/bin/env python3
from flask import Flask, request, render_template_string
from pathlib import Path
import os

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="sv">
<head>
    <meta charset="utf-8">
    <title>Sårbar filvisare</title>
    <style>
        body {
            font-family: sans-serif;
            max-width: 900px;
            margin: 40px auto;
        }

        .files {
            padding: 20px;
            background: #eee;
        }

        pre {
            padding: 20px;
            background: #222;
            color: #eee;
            overflow-x: auto;
        }
    </style>
</head>

<body>

<h1>Sårbar filvisare</h1>

<h2>Filer</h2>

<div class="files">
    <ul>
    {% for file in files %}
        <li>
            <a href="/?file={{ file }}">{{ file }}</a>
        </li>
    {% endfor %}
    </ul>
</div>

{% if filename %}
    <h2>{{ filename }}</h2>
    <pre>{{ content }}</pre>
{% endif %}

</body>
</html>
"""


@app.route("/")
def index():

    # Lista endast filer i aktuell katalog
    files = [
        f for f in os.listdir(".")
        if os.path.isfile(f)
    ]

    filename = request.args.get("file")
    content = None

    if filename:
        try:
            # AVSIKTLIGT SÅRBART!
            with open(filename, "r") as f:
                content = f.read()
        except Exception as e:
            content = str(e)

    return render_template_string(
        HTML,
        files=files,
        filename=filename,
        content=content
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
