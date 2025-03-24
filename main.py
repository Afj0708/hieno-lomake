from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    return render_template('vastaus.html', väri=request.args['color'])
















if __name__=='__main__':
    app.run(debug=True)

