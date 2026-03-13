import turtle
import time

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Ping Pong con Turtle")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)  # Controla la animación manualmente

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))

# Instrucciones
instrucciones = turtle.Turtle()
instrucciones.speed(0)
instrucciones.color("yellow")
instrucciones.penup()
instrucciones.hideturtle()
instrucciones.goto(0, -280)
instrucciones.write("Jugador A: W (arriba) / S (abajo) | Jugador B: ↑ / ↓", 
                    align="center", font=("Courier", 12, "normal"))

# Jugador 1 (izquierda)
jugador_a = turtle.Turtle()
jugador_a.speed(0)
jugador_a.shape("square")
jugador_a.color("white")
jugador_a.shapesize(stretch_wid=6, stretch_len=1)
jugador_a.penup()
jugador_a.goto(-350, 0)

# Jugador 2 (derecha)
jugador_b = turtle.Turtle()
jugador_b.speed(0)
jugador_b.shape("square")
jugador_b.color("white")
jugador_b.shapesize(stretch_wid=6, stretch_len=1)
jugador_b.penup()
jugador_b.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 2 # Velocidad MÁS LENTA en x
pelota.dy = 2  # Velocidad MÁS LENTA en y

# Línea central (opcional, para que se vea más profesional)
linea = turtle.Turtle()
linea.speed(0)
linea.color("gray")
linea.penup()
linea.goto(0, -300)
linea.pendown()
linea.goto(0, 300)
linea.hideturtle()

# Puntuaciones
puntos_a = 0
puntos_b = 0

# Funciones para mover las paletas
def paleta_a_arriba():
    y = jugador_a.ycor()
    if y < 250:  # Límite superior
        jugador_a.sety(y + 30)
        ventana.update()  # Actualizar inmediatamente

def paleta_a_abajo():
    y = jugador_a.ycor()
    if y > -240:  # Límite inferior
        jugador_a.sety(y - 30)
        ventana.update()  # Actualizar inmediatamente

def paleta_b_arriba():
    y = jugador_b.ycor()
    if y < 250:
        jugador_b.sety(y + 30)
        ventana.update()  # Actualizar inmediatamente

def paleta_b_abajo():
    y = jugador_b.ycor()
    if y > -240:
        jugador_b.sety(y - 30)
        ventana.update()  # Actualizar inmediatamente

# Teclado - IMPORTANTE: usamos onkeypress para respuesta inmediata
ventana.listen()
ventana.onkeypress(paleta_a_arriba, "w")
ventana.onkeypress(paleta_a_abajo, "s")
ventana.onkeypress(paleta_a_arriba, "W")  # También mayúsculas
ventana.onkeypress(paleta_a_abajo, "S")
ventana.onkeypress(paleta_b_arriba, "Up")
ventana.onkeypress(paleta_b_abajo, "Down")

# Función para actualizar el marcador
def actualizar_marcador():
    marcador.clear()
    marcador.write(f"Jugador A: {puntos_a}  Jugador B: {puntos_b}", 
                   align="center", font=("Courier", 24, "normal"))

# Pequeña pausa para que todo cargue
time.sleep(1)

# Bucle principal del juego
print("¡Juego iniciado! Usa las teclas para mover las paletas.")

while True:
    ventana.update()
    
    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    # Rebote en bordes superior/inferior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
    
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
    
    # Rebote en bordes laterales (puntos)
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntos_a += 1
        actualizar_marcador()
        print(f"¡PUNTO! Jugador A: {puntos_a} | Jugador B: {puntos_b}")
    
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntos_b += 1
        actualizar_marcador()
        print(f"¡PUNTO! Jugador A: {puntos_a} | Jugador B: {puntos_b}")
    
    # Rebote con las paletas (más preciso ahora)
    # Paleta derecha (Jugador B)
    if (340 < pelota.xcor() < 360) and (jugador_b.ycor() - 50 < pelota.ycor() < jugador_b.ycor() + 50):
        pelota.setx(340)
        pelota.dx *= -1
    
    # Paleta izquierda (Jugador A)
    if (-360 < pelota.xcor() < -340) and (jugador_a.ycor() - 50 < pelota.ycor() < jugador_a.ycor() + 50):
        pelota.setx(-340)
        pelota.dx *= -1
    
    # Pequeña pausa para controlar la velocidad
    time.sleep(0.01)