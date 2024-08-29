import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.geometry("320x576")
#janela.overrideredirect(True) #remover barra de fechar
janela.resizable(width=False, height=False)
#janela.iconify() #Fecha a janela

janela.title("EasyALB")
btn = ctk.CTkButton(janela, text="Hoi")
btn.pack()

def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("200x200")

btn_novatela = ctk.CTkButton(master = janela, text = "Abrir nova janela", command = nova_tela).place(x=125, y=300)





janela.mainloop() #Roda janela