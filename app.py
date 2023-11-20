from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        # customInput = request.form['customInput']
        customInput = "Your New Password is aabbccssdddd"
        return jsonify({'output': customInput})

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
