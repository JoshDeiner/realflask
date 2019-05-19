''' render routes'''
import app

@app.app.route("/")
@app.app.route("/index")
def index():
    ''' return html user info '''
    user = {"username": "miguel"}
    return (
        """
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, """
        + user["username"]
        + """!</h1>
        </body>
    </html>"""
    )
