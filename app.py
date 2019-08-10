from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    return jsonify({"about": "Hello World!"})


@app.route('/<int:num>',methods=['GET'])
def get_env(num):
    return('dev '+str(num))


if __name__ == '__main__':
    app.run(debug=True)
