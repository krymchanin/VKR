from flask import Flask


app = Flask(_name_)


@app.route('/') #127.1.1.0:5000/
def index():
    return "Hello!"

if __name__ == ('__main__'):
    app.run()