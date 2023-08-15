from flask import Flask,render_template,request,jsonify
# create object
app = Flask(__name__)

@app.route('/calculate', methods =['GET','POST'])
def math_operator():
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']

    if operation =="add":
        result = int(number1) + int(number2)
    elif operation=="multiply":
        result = int(number1) * int(number2)
    elif operation == "divide":
        result = int(number1)/int(number2)
    elif operation == "subtract":
        result = int(number1) - int(number2)
    else:
        result = "incorrect number"
    return "the operation is {} and result is {}".format(operation,result)

if __name__=='__main__':
    app.run() 