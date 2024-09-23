import tkinter as tk
import requests
from PIL import Image
from io import BytesIO
from tkinter import ttk

tela = tk.Tk()
tela.title('Bulbasaur')
canvas = tk.Canvas(tela, width=500, height=500)
canvas.pack()

def buscarPokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    lista_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
    lista_pokemon = lista_pokemon.json()
    pokemons = lista_pokemon["results"]
    pokedex = []
    for pokemon in pokemons:
        pokedex.append(pokemon["name"])
    return pokedex

def poke_combobox(event):
    pegar_pokemonn = pc.get()
    url= pegar_pokemon(pegar_pokemonn)
    abrirImagem1(url)

pokedex = buscarPokemon()
pc = ttk.Combobox(tela,values=pokedex)
pc.bind("<<ComboboxSelected>>",poke_combobox)
pc.pack()

def pegar_pokemon(pokemon):
    url =("http://pokeapi.co/api/v2/pokemon/"+ pokemon)
    qual_pokemon = requests.get(url)
    qual_pokemon = qual_pokemon.json()
    imagem = qual_pokemon["sprites"]["front_default"]
    return imagem

caixa_texto=tk.Entry(tela)
caixa_texto.pack(pady=5)

print(pegar_pokemon("bulbasaur"))
imgCanvas = canvas.create_image(300, 400)
def pegaImagemNet(linkImagem):
    respostaSite = requests.get(linkImagem)
    imagemSite = BytesIO(respostaSite.content)
    imagem = Image.open(imagemSite)
    imagem = imagem.convert('RGB')
    return imagem

def converterImagem(imagem):
    with BytesIO() as output:
        imagem.save(output, format='PPM')
        ppmImagem = output.getvalue()
    return ppmImagem

def abrirImagem1(imgUrl):
    novaImg = pegaImagemNet(imgUrl)
    novaImgPPM = converterImagem(novaImg)
    novaImg = tk.PhotoImage(data=novaImgPPM)
    canvas.itemconfig(imgCanvas, image=novaImg)

    canvas.image = novaImg

def pokemon():
    pegar_pokemon1 = caixa_texto.get()
    imgUrl1 = pegar_pokemon(pegar_pokemon1)
    abrirImagem1(imgUrl1)

botao = tk.Button(tela,text="Botao",command=pokemon)
botao.pack(pady=5)



tela.mainloop()
