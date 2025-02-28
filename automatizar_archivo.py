#Abrir el archivo de texto
with open('tareas.txt', 'r') as file:
    tareas = file.readlines()

#Mostrar las tareas
print("Tareas en el archivo:")
for tarea in tareas:
    print(tarea.strip())

#Modificar el archivo, añadiendo una tarea nueva
with open('tareas.txt', 'a') as file:
    file.write("Tarea 4: Reunion de equipo\n")

print("Tarea 4 añadida al archivo.")