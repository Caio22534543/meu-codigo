import tkinter as tk
import random

emojis = ["🤫", "😍"]

mensagens = [
    "Eu sei que a gente não está se falando muito... É até estranho falar isso, porque a gente praticamente se falava todos os dias, mas o tempo muda, né? E, com essa mudança, parte dela está me doendo muito. Eu sei que agora a gente está em uma nova fase das nossas vidas, e essa separação entre a gente, uma hora ou outra, ia acontecer. Mas eu entendo que tinha que acontecer, principalmente para a gente organizar melhor nossas vidas. Temos muitas responsabilidades agora, e eu compreendo tudo que está acontecendo. E está tudo bem...",
    "Espero que, nesse tempo em que a gente não se vê e não se fala, você tenha conseguido \"respirar\" um pouco kkkk. Porque eu sei o quanto eu te deixava preocupada, nervosa, chateada, ansiosa... por minha causa. E eu juro, nunca foi minha intenção te deixar assim. Nunca foi. Você sabe das minhas intenções, sabe o quanto eu fazia de tudo pra te ver feliz — tudo mesmo. Fiz até algumas loucuras que você nunca vai saber kkkk.\n\nMas enfim... esse tempo longe de você me deixou com um vazio profundo. Sinto que falta alguma coisa em mim. Vou ser bem sincero com você: penso em você todos os dias. Nunca deixei de pensar, mesmo tentando evitar. Mas é inútil... sempre acabo pensando em você, uma hora ou outra, não importa o que eu faça.",
    "Tudo me lembra você... Desde uma “florzinha pequenininha, maravilhosa, da cor de rosa”, até quando eu estou fazendo a barba e penso: “Ela preferia sem barba, né?”. É incrível como tudo me lembra você kkkkkkkkkkkkkk.\n\nAté ano passado, quando a gente estudava junto, uma das formas de eu te ver era pelo colégio. E eu não mentia quando falava: “Só vou por sua causa.” Eu lembro que dizia isso lá no 9º ano e no 1º ano kkk. Mas não pense que era da boca pra fora, não viu? Era verdade. Você era minha motivação, você iluminava meu dia e sempre conseguia transformar o meu dia no melhor do mundo.\n\nTinha vezes que você falava coisas tipo:\n“Eu só dou trabalho pros outros.”\n“Eu sou a pior pessoa do mundo.”\n“Eu não faço nada certo.”\n“Eu fud@ tua vida, Caio... ”\n\nEntre outras besteiras. Mas tu só pode estar de brincadeira, né, Bruna? Como é que você pode dizer isso — logo pra mim? Logo pra pessoa que você ajudou a encontrar a felicidade. A pessoa que é quem é hoje por sua causa.\n\nVocê me ajudou a ter maturidade. Você fez com que eu me amasse. E a gente sabe: não dá pra amar os outros se a gente mesmo não se ama, né?\n\nVocê foi — e é — a melhor coisa que já me aconteceu. Eu poderia falar infinitamente sobre o quanto você me faz bem...",
    "Até hoje eu carrego sua foto na minha carteira. E, sempre que olho pra ela, é como se um pedacinho seu estivesse comigo. Meu celular, de vez em quando, coloca sua foto bem na tela principal, como se ele mesmo soubesse do que meu coração sente falta. E toda vez que entro na galeria, lá está você... Não tive coragem de apagar nenhuma das suas fotos. Simplesmente não consigo.\nEngraçado o amor, né? Ele transforma a gente de um jeito que nem dá pra explicar.\n\nQuem diria... Aqui estou eu, às 4h da manhã do dia 26/05/2025, colocando em prática o que aprendi na faculdade — e não é pra fazer um trabalho ou projeto. É pra desabafar. É pra escrever pra você, Bruna. O amor da minha vida. É pra dizer o quanto eu sinto sua falta, o quanto meu coração te procura em cada detalhe do meu dia.\n\nQue saudade de olhar pra você, admirando sua beleza como se fosse a primeira vez. Seus olhos... ah, seus olhos... Eles me hipnotizam sempre que cruzam com os meus. Você é a única pessoa capaz de quebrar toda a minha postura só com um olhar.\n\nSua boca suave. Seus cabelos de seda. Seu rosto angelical. Sua pele macia. Seus dentes perfeitamente perfeitos... Mas quer saber? Nada disso é o que mais me faz te amar.\n\nO que mais me faz te amar é o seu jeito, Bruna. Sua personalidade, seu jeito único de ser. É isso que me conquista todos os dias, mesmo à distância. Sua inteligência me atrai de uma forma que você nem imagina. O seu cuidado comigo, suas preocupações, até suas bobagens... Tudo isso me faz te amar ainda mais.\n\nVocê é o tipo de amor que não some. Que não se apaga. Que vive em mim, mesmo nos silêncios, mesmo nas madrugadas solitárias.\nE tudo isso... tudo isso é pra dizer que você continua sendo o amor da minha vida."
]

class Emoji:
    def __init__(self, canvas, emoji):
        self.canvas = canvas
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 100:
            w = 1000
        if h < 100:
            h = 700
        margin = 40
        self.id = canvas.create_text(
            random.randint(margin, w - margin),
            random.randint(margin, h - margin),
            text=emoji,
            font=("Arial", 30)
        )
        self.vx = random.choice([-3, -2, -1, 1, 2, 3])
        self.vy = random.choice([-3, -2, -1, 1, 2, 3])

    def move(self):
        self.canvas.move(self.id, self.vx, self.vy)
        x, y = self.canvas.coords(self.id)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        margin = 40
        if x <= margin or x >= width - margin:
            self.vx = -self.vx
        if y <= margin or y >= height - margin:
            self.vy = -self.vy

def mover_emojis():
    for e in emojis_na_tela:
        e.move()
    janela.after(50, mover_emojis)

def centralizar_botao(event=None):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    if tela_atual == "inicial":
        canvas.coords(botao_window, width // 2, height // 2)
    elif tela_atual == "mensagem":
        canvas.coords(botao_voltar_window, 10, 10)
        canvas.coords(botao_proximo_window, width - 10, height - 10)

def mostrar_mensagem():
    global emojis_na_tela, tela_atual, mensagem_index
    tela_atual = "mensagem"
    mensagem_index = 0
    emojis_na_tela.clear()
    canvas.delete("all")
    mostrar_texto(mensagem_index)

def mostrar_texto(index):
    global botao_voltar, botao_proximo, botao_voltar_window, botao_proximo_window
    canvas.delete("all")
    texto = mensagens[index]
    canvas.create_text(
        canvas.winfo_width() // 2,
        canvas.winfo_height() // 2,
        text=texto,
        font=("Arial", 20),
        fill="black",
        width=canvas.winfo_width() - 40,
        justify="center"
    )

    # Botão Voltar
    botao_voltar = tk.Button(canvas, text="Voltar", font=("Arial", 12), command=mostrar_tela_inicial)
    botao_voltar_window = canvas.create_window(10, 10, window=botao_voltar, anchor="nw")

    # Botão Anterior (se não for a primeira mensagem)
    if index > 0:
        botao_anterior = tk.Button(canvas, text="Anterior", font=("Arial", 12), command=lambda: mostrar_texto(index - 1))
        canvas.create_window(110, 10, window=botao_anterior, anchor="nw")

    # Botão Próximo (se não for a última mensagem)
    if index < len(mensagens) - 1:
        botao_proximo = tk.Button(canvas, text="Próximo", font=("Arial", 12), command=lambda: mostrar_texto(index + 1))
        botao_proximo_window = canvas.create_window(canvas.winfo_width() - 10, canvas.winfo_height() - 10, window=botao_proximo, anchor="se")
    else:
        botao_proximo = None

def mostrar_tela_inicial():
    global tela_atual
    tela_atual = "inicial"
    canvas.delete("all")
    criar_emojis()
    global botao_window
    botao_window = canvas.create_window(canvas.winfo_width() // 2, canvas.winfo_height() // 2, window=botao)
    centralizar_botao()

janela = tk.Tk()
janela.title("Emojis vagando")
janela.configure(bg="white")

canvas = tk.Canvas(janela, bg="white", highlightthickness=0, width=1000, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

botao = tk.Button(canvas, text="aperte", font=("Arial", 14), fg="black", bg="red", command=mostrar_mensagem)
botao_window = canvas.create_window(500, 350, window=botao)

canvas.bind("<Configure>", centralizar_botao)

tela_atual = "inicial"
emojis_na_tela = []

def criar_emojis():
    global emojis_na_tela
    emojis_na_tela = []
    for _ in range(50):
        emoji = random.choice(emojis)
        emojis_na_tela.append(Emoji(canvas, emoji))
    mover_emojis()

janela.after(300, criar_emojis)

janela.mainloop()