from flask import Flask, render_template, request, make_response, Request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('setcookie.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID',user)
        return resp

if __name__ == '__main__':
    app.run(debug=True)
