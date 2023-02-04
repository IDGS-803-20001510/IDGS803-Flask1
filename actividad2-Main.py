from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/cine")
def cine():
    return render_template("actividad2-Cine.html")

@app.route("/ticket",methods=["POST"])
def ticket():
    nombre=request.form.get("txtNombre")
    cantidad=int(request.form.get("txtCantidad"))
    tarjeta=request.form.get("txtTarjeta")
    cantidadB=int(request.form.get("txtCantidadB"))
    opc=int(request.form.get("opc"))
    valorB=int(12)

    if (cantidad < 2):
        per=cantidad*7
        if (opc == 1):
            if(cantidadB >per):
                res="No se puede hacer el pago \n por que la cantidad excede de lo permitido el máximo de compra es {}".format(per)
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,res=res,per=per)
            elif (cantidadB >5 and cantidadB <=per):
                pago=int(cantidadB)*valorB
                des=pago*0.15
                des2=pago-des
                PRes=des2*0.10
                res=des2-PRes
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,des2=des2,PRes=PRes,res=res,per=per)   
            elif (cantidadB >2 and cantidadB <6):
                pago=int(cantidadB)*valorB
                des=pago*0.10
                des2=pago-des
                PRes=des2*0.10
                res=des2-PRes
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,des2=des2,PRes=PRes,res=res,per=per)   
            elif (cantidadB <=2):
                pago=int(cantidadB)*valorB
                des=pago*0.10
                res=pago-des
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,res=res,per=per)   
        elif (opc == 2):
            if (cantidadB >5 and cantidadB <per):
                pago=int(cantidadB)*valorB
                des=pago*0.15
                res=pago-des
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,res=res,per=per)   
            elif (cantidadB >2 and cantidadB <6):
                pago=int(cantidadB)*valorB
                des=pago*0.10
                res=pago-des
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,res=res,per=per)   
            elif (cantidadB <=2):
                res=int(cantidadB)*valorB
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,res=res,per=per)
    elif (cantidad >=2):
        per=cantidad*7
        if (opc == 1):
            if(cantidadB >per):
                per=cantidad*7
                res="No se puede hacer el pago \n por que la cantidad excede de lo permitido, el máximo de compra es {}".format(per)
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,res=res,per=per)
            elif (cantidadB >5 and cantidadB <=per):
                pago=int(cantidadB)*valorB
                des=pago*0.15
                des2=pago-des
                PRes=des2*0.10
                res=des2-PRes
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,des2=des2,PRes=PRes,res=res,per=per)   
            elif (cantidadB >2 and cantidadB <6):
                pago=int(cantidadB)*valorB
                des=pago*0.10
                des2=pago-des
                PRes=des2*0.10
                res=des2-PRes
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,des2=des2,PRes=PRes,res=res,per=per)   
            elif (cantidadB <=2):
                pago=int(cantidadB)*valorB
                des=pago*0.10
                res=pago-des
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,res=res,per=per)   
        elif (opc == 2):
            per=cantidad*7
            if(cantidadB >per):
                res="No se puede hacer el pago \n por que la cantidad excede de lo permitido el máximo de compra es {}".format(per)
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,res=res,per=per)
            elif (cantidadB >5 and cantidadB <=per):
                pago=int(cantidadB)*valorB
                des=pago*0.15
                res=pago-des
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,res=res,per=per)   
            elif (cantidadB >2 and cantidadB <6):
                pago=int(cantidadB)*valorB
                des=pago*0.10
                res=pago-des
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,pago=pago,des=des,res=res,per=per)   
            elif (cantidadB <=2):
                res=int(cantidadB)*valorB
                return render_template("actividad2-Ticket.html",nombre=nombre,cantidad=cantidad,tarjeta=tarjeta,cantidadB=cantidadB,opc=opc,valorB=valorB,res=res,per=per)



if __name__=="__main__":
    app.run(debug=True)    