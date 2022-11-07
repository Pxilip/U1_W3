import math                               # built-in module per usare il pi greco

def square():
    square_input = int(input("Inserisci il valore dal lato: "))
    print(f"Perimetro: {square_input * 4}")

def rectangle():
    x = int(input("Inserisci il valore della base: "))
    y = int(input("Inserisci il valore dell'altezza: "))
    print(f"Perimetro: {x * 2 + y * 2}")

def circle():
    circle_input = int(input("Inserisci il valore dal raggio: "))
    print(f"Circonferenza: {circle_input * math.pi * 2}")


program_running = True
while program_running == True:            # dovuto darli una condizione per non creare infinite loop
    user_input = input("\nScrivere 1 perimetro del quadrato\t|\tScrivere 2 perimetro del rettangolo\t|\tScrivere 3 per circonferenza cerchio\n\t\t\t\t\t\t\t\t\t\t\t\tScrivere 0 per Uscire\n") #non so perchè l'ho fatto..
    if user_input == "1":
        square()
    elif user_input == "2":
        rectangle()
    elif user_input == "3":
        circle()
    elif user_input == "0":               # per uscire dal loop
        program_running = False
        print("Programma Chiuso!")
                                          # non ho messo else, visto che non è obbligatorio
