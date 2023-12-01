from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['get'])
def index():
    return render_template('index.html')

@app.route("/checkEven/<num>")
def checkEven(num):
    try:
        if int(num) & 1 == 0:
            return "True"
        return "False"
    except:
        return f"Error, only Integer values are allowed({num})"

@app.route("/checkPrime/<num>")
def checkPrime(num):
    try:
        num = int(num)

        if num in [0,1]:
            return "Composite Number"
        if num < 0:
            return "-ve Numbers are not Prime Number"
        
        for i in range(2,num // 2):
            if num % i == 0:
                return "not Prime Number"
        return "Prime Number"
    
    except Exception as e:
        return f"Error, not a valid input ({num})"

if __name__ == '__main__':
    app.run(port=8000,debug=True)