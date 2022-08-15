#implementar un sistema de gestión de tareas
#un usuario debe tener un nombre, una lista de tareas y una tarea en curso
#los elementos de la lista de tareas son de una clase Tarea
#la clase Tarea tiene los siguientes atributos:
    #descripción de la tarea
    #fecha límite de la tarea
#la clase usuario tiene los siguientes atributos:
    #nombre
    #tareaActual
    #listaTareas
#la clase usuario tiene los siguientes métodos:
    #agregar una tarea:
        #si el usuario no tiene tarea actual, la agrega como tarea actual
        #si el usuario ya tiene tarea actual, la agrega a la lista de tareas pendientes
    #finalizar una tarea
        #saca la siguiente tarea de la lista y la pone en "tarea actual"

#1. hacer una clase Tarea

class Task:
    def __init__(self, description, dueDate): #atributos de la clase definidos en init
        self.description = description
        self.dueDate = dueDate
        
    def __str__(self):
        return self.description + " - " + self.dueDate

#2. hacer la clase usuario
class User:
    def __init__(self, name):
        self.name = name
        self.currentTask = ''
        self.taskList = []
        
    def addTask(self, newTask):
        """
        Metodo para agregar una tarea
        """
        #revisar si el user ya tiene una tarea actual
        if self.currentTask == '':
            self.currentTask = newTask
        else:
            self.taskList.append(newTask)
        
    def printTask(self):
        if not self.currentTask == '':
            print("Tarea actual: ", self.currentTask)
        if len(self.taskList) != 0:
            print("Cola de lista de Tareas por realizar: ")
            for task in self.taskList:
                print(task)
        else: print("Lista de tareas en cola Vacia!")
    
    def endTask(self):
        """
        Metodo para finalizar una tarea
        """
        taskDelete = self.currentTask # task a eliminar, no esta en la lista, esta en otro atributo (head o primera)
        if len(self.taskList) > 0:            
            self.currentTask = self.taskList.pop(0)# 1ra tarea de la cola
        else: # sino hay elementos en la lista de cola de tareas, solo existe la actual
            self.currentTask = ''      
        return taskDelete
             
        
    def __str__(self):
        return self.name + " - " + self.currentTask + " - " + self.taskList
    
#3. hacer la lógica de la aplicación
user = User("Edwin")

while True:
    operaciones = """
        Ingrese A para Registrar una nueva tarea.
        Ingrese F para Finalizar la tarea actual.
        Ingrese I para Imprimir la lista de tareas.
    """
    inputUsuario = input(operaciones).upper()
    if inputUsuario == "A":
        #pedir la descripcion de la tarea y su fecha
        descripcion = input("Ingrese la descripcion de la tarea: ")
        fecha = input("Ingrese la fecha de la tarea: ")
        #crear la nueva tarea
        nuevaTarea = Task(description=descripcion, dueDate=fecha)
        #implementar el metodo addTask de la clase User
        user.addTask(nuevaTarea)
        print("Nueva tarea agregada!")
    elif inputUsuario == 'I': 
        user.printTask()
    elif inputUsuario == "F":
        print(f'La tarea "{user.endTask()}" ha sido finalizada!')
        user.printTask()