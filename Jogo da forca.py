import tkinter as tk
import random

palavras = ["egito", "guatemala", "libano", "macedonia", "vaticano", "belgica"]

def reiniciar_jogo():
    global palavra_secreta, letras_adivinhadas, tentativas_restantes
    palavra_secreta = random.choice(palavras)
    letras_adivinhadas = []
    tentativas_restantes = 10
    atualizar_display()

def atualizar_display():
    display_palavra.set(" ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta]))
    display_tentativas.set(f"Tentativas restantes: {tentativas_restantes}")
    if tentativas_restantes == 0:
        display_palavra.set(f"Você perdeu! A palavra era: {palavra_secreta}")

def adivinhar():
    global tentativas_restantes
    letra = entry_letra.get().lower()
    entry_letra.delete(0, tk.END)

    if letra and letra not in letras_adivinhadas:
        letras_adivinhadas.append(letra)
        if letra not in palavra_secreta:
            tentativas_restantes -= 1
        atualizar_display()
    else :
        display_tentativas.set(f"Você já escolheu essa letra: {letras_adivinhadas} e você tem {tentativas_restantes},tentativas restantes ")
    if set(palavra_secreta).issubset(letras_adivinhadas):
        display_palavra.set(f"Você ganhou! A palavra era: {palavra_secreta}")

root = tk.Tk()
root.title("Jogo da Forca de países")

display_palavra = tk.StringVar()
display_tentativas = tk.StringVar()

tk.Label(root, textvariable=display_palavra, font=('Arial', 24)).pack(pady=20)
tk.Label(root, textvariable=display_tentativas, font=('Arial', 18)).pack(pady=20)

entry_letra = tk.Entry(root, font=('Arial', 24), width=2)
entry_letra.pack(pady=20)

tk.Button(root, text="Adivinhar", command=adivinhar, font=('Arial', 18)).pack(pady=20)
tk.Button(root, text="Reiniciar", command=reiniciar_jogo, font=('Arial', 18)).pack(pady=20)

reiniciar_jogo()

root.mainloop()
