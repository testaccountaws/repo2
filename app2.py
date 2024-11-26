from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/application2")
def Application2():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Application 2</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f8f8f8;
            }
            .application {
                font-size: 24px;
                text-align: center;
                padding: 20px;
                border: 2px solid #4a90e2;
                background-color: #e0f7fa;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>

        <div class="application">
            When in doubt, fish!
        </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
