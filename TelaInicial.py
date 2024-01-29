import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(500, 500))

        # Cria um painel
        self.panel = wx.Panel(self)

        # Carrega a imagem
        self.image = wx.Image("imagens\TI.png")

        # Cria um bitmap da imagem
        self.bitmap = wx.Bitmap(self.image)

        # Cria um fundo com a imagem
        self.background = wx.StaticBitmap(self.panel, bitmap=self.bitmap)

        # Cria um botão
        self.btn = wx.Button(self.panel, label="Clique aqui")
        self.btn.Bind(wx.EVT_BUTTON, self.on_click)

        # Cria um texto
        self.txt = wx.StaticText(self.panel, label="Texto")

        # Organiza os elementos na tela
        self.btn.SetPosition((250, 200))
        self.background.SetPosition((0, 0))
        self.txt.SetPosition((250, 100))

        self.btn.Raise()

        self.Centre()

    def on_click(self, event):
        print("O botão foi clicado!")

app = wx.App()
frame = MyFrame(None, title="Tela com botão")
frame.Show()
app.MainLoop()
