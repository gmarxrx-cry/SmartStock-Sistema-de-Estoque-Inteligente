import customtkinter as ctk
import estoque

app = ctk.CTk()

frame = estoque.cadastrarItens(app)
frame.pack(fill="both", expand=True)

app.mainloop()