from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/cloth/')
def cloth():
    return render_template('cloth.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jackets/')
def jackets():
    return render_template('jackets.html')


if __name__ == '__main__':
    app.run(debug=True)
