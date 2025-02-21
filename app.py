from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods= ['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form[operation]

    # Perform the calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
    # Return the result to the HTML template
    return render_template('calculator.html', result=result, num1=num1, num2=num2, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)