from flask import Flask,render_template,request
# create object
app = Flask(__name__)

@app.route('/calculate', methods =['GET','POST'])
def math_operator():
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']

    if operation =="add":
        result = number1 + number2
    elif operation=="multiply":
        result = number1 * number2
    elif operation == "divide":
        result = number1/number2
    elif operation == "subtract":
        result = number1 - number2
    else:
        result = "incorrect number"
    return result

if __name__=='__main__':
    app.run() 