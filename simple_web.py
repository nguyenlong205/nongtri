from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Sum Calculator</title>
        </head>
        <body>
            <h2>Simple Sum Calculator</h2>
            <form action="/calculate" method="post">
                <label>Enter first number:</label>
                <input type="number" name="num1" required><br><br>
                <label>Enter second number:</label>
                <input type="number" name="num2" required><br><br>
                <input type="submit" value="Calculate Sum">
            </form>
        </body>
    </html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return f"<h2>Result: {num1} + {num2} = {result}</h2><br><a href='/'>Go Back</a>"
    except ValueError:
        return "<h2>Invalid Input! Please enter valid numbers.</h2><br><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)

