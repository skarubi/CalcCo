from flask import Flask
from flask import request
from Calculator import calculator
from Calculator import factorial

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to CalcuCo!"

@app.route("/Add", methods=['POST'])
def add():
    var_1 = request.args.get("var_1",type=float)
    var_2 = request.args.get("var_2",type=float)
    result=calculator ("Add", var_1, var_2)
    result= str(result)
    return "{status:200, result:"+result+"}"

@app.route("/Subtract", methods=['POST'])
def subtract():
    var_1 = request.args.get("var_1",type=float)
    var_2 = request.args.get("var_2",type=float)
    result=calculator ("Subtract",var_1,var_2)
    result= str(result)
    return "{status:200, result:"+result+"}"

@app.route("/Multiply", methods=['POST'])
def multiply():
    var_1 = request.args.get("var_1",type=float)
    var_2 = request.args.get("var_2",type=float)
    result=calculator ("Multiply",var_1,var_2)
    result= str(result)
    return "{status:200, result:"+result+"}"

@app.route("/Divide", methods=['POST'])
def divide():
    var_1 = request.args.get("var_1",type=float)
    var_2 = request.args.get("var_2",type=float)
    result=calculator ("Divide",var_1,var_2)
    result= str(result) 
    return "{status:200, result:"+result+"}"

@app.route("/Factorial", methods=['POST'])
def factorial_1():
    var_1 = request.args.get("var_1",type=int)
    if var_1 < 0:
        result = "Factorial cannot be found for negative numbers"
    elif var_1 == 0:
        result= 1
    else:
        result= factorial (var_1)
    result= str(result)
    return "{status:200, result:"+result+"}"