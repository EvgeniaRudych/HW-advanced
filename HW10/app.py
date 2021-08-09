from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/calc/<int:x>/<int:y>/<string:operation>')
def calc(x, y, operation):
    if operation == "sum":
        return render_template('calc.html', x=x, y=y, operation="+", result=x + y)
    elif operation == "sub":
        return render_template('calc.html', x=x, y=y, operation="-", result=x - y)
    elif operation == "mult":
        return render_template('calc.html', x=x, y=y, operation="*", result=x * y)
    elif operation == "div":
        return render_template('calc.html', x=x, y=y, operation="/", result=x / y)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
