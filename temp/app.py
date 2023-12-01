
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index() :
    return '''
    <script>
        const jsFun = () => {
            const val = document.querySelector("input");
            alert(val.value);
        }
    </script>

    <button>ok</button>
    <input class="value" type="number" placeholder="Value"/>
    <button>Is Even</button>
    '''

@app.route("/isEven/<num>",methods=['get'])
def isEven(num):
    try:
        if int(num) & 1 == 0:
            result = {
                "IsEven" : "True",
                "Number" : num
            }
        else :
            result = {
                "IsEven" : "False",
                "Number" : num
            }
        return jsonify(result)
    except Exception as e:
        return "Valid for Integer only"

def check(num):
    if num in [0,1]:
        return False
    for i in range(2,num) : 
        if num % i == 0:
            return False
    return True

@app.route("/isPrime/<num>",methods=['get'])
def isPrime(num):
    try:
        if check(int(num)):
            result = {
                "IsPrime" : "True",
                "Number" : num
            }
        else :
            result = {
                "IsPrime" : "False",
                "Number" : num
            }
        return jsonify(result)
    except Exception as e:
        print(e)
        return "Valid for Integer only"

@app.route("/post",methods=['post'])
def postMethod():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=8000)