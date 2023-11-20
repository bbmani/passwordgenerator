from flask import Flask, render_template, request, jsonify
import rstr as r

app = Flask(__name__)

def generate_password():
    output = '{0}-{1}@{2}'.format(
        r.domainsafe(5,10),
        r.domainsafe(5,10),
        r.domainsafe(5)
    )
    return output

def main():
    return_value = generate_password()
    return return_value

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        customInput = main()
        return jsonify({'output': customInput})

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=6969)
