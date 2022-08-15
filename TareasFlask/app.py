from flask import Flask, render_template, url_for, redirect, request #instalar libreria flask: pip install flask
from models import User, Task

app = Flask(__name__)# crear instancia de flask

user = User("Ed")

@app.route("/")
def index():
    # envian las variables user y currentT al html para que muestre la info
    return render_template('index.html', user=user, currentTask=user.currentTask)
    #return "Hola Mundo!"

@app.route("/end-task", methods=["GET", "POST"])
def endTask():
    print("Eliminando Tarea")
    user.endTask()
    return redirect('/')

@app.route("/add-task", methods=["GET", "POST"])
def addTask():
    if request.method == "GET": # usuario apenas llega a ruta, retorna el html de la pagina
        return render_template('task.html')
    elif request.method == "POST": # usuario envia datos de forma incognita
        print(request.form)
        description = request.form["descripcion"]
        date = request.form["fecha"]
        newTask = Task(description=description, dueDate=date)
        user.addTask(newTask)
        print(newTask)
        return redirect("/")
    




# Permite se ejecute auto con 'run' funciona como ciclo while True
if __name__ == "__main__":
    app.run(debug=True)