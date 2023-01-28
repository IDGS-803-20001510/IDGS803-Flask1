from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/operasBas",methods={"GET","POST"})
def operasBas():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opc=request.form.get("opc")
        if (opc == '1'):
            return "La suma es: {}".format(str(int(num1)+int(num2)))
        elif (opc == '2'):
            return "La resta es: {}".format(str(int(num1)-int(num2)))
        elif (opc == '3'):
            return "La multiplicación es: {}".format(str(int(num1)*int(num2)))
        elif (opc == '4'):
            return "La división es: {}".format(str(int(num1)/int(num2)))
    else:
        return '''
            <h1> Operaciones Basicas </h1>
            <form action="/operasBas" method="POST">
            <label> N1: </label>
            <input type="text" name="num1"/></br></br>
            <label> N2: </label>
            <input type="text" name="num2"/></br></br>
            <label> Suma </label>
            <input type="radio" value="1" name="opc"/></br
            <label> Resta </label>
            <input type="radio" value="2" name="opc"/></br
            <label> Multiplicación</label>
            <input type="radio" value="3" name="opc"/></br
            <label> División </label>
            <input type="radio" value="4" name="opc"/> </br>
            <input type="submit" value="operasBas"/>
            </form>
    '''

if __name__=="__main__":
    app.run(debug=True)    