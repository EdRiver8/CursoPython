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