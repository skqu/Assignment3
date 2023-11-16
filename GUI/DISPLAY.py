from .GUI import GUI

class DISPLAY(GUI):

    def __init__(self, frame, name):
        super().__init__()
        self.master = frame.obj
        self.config["text"] = ""
        self.config["relief"] = "solid"
        self.config["width"] = 80
        self.config["height"] = 3
        self.config["font"] = 20
        self.construct()
        self.placement(0, 0)
        self.padding(10)
        self.build()

    def append(self, content):
        content = self.get() + content
        self.set(content=content)

    def build(self):
        self.obj.config(text=self.config["text"])
        self.obj.grid(column=self.col,  row=self.row, padx=self.padx, pady=self.pady)
        
    def get(self) -> str:
        return self.config["text"]
    
    def set(self, content):
        self.config["text"] = content
        self.build()

