import customtkinter as ctk
from tkinter import *
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk(fg_color="#4C4966")
janela.geometry("320x576")
#janela.overrideredirect(True) #remover barra de fechar
janela.resizable(width=False, height=False)
#janela.iconify() #Fecha a janela
janela.title("EasyALB")

logo_image = ctk.CTkImage(light_image=Image.open("EasyALB1.png"), 
                          dark_image=Image.open("EasyALB1.png"),
                          size=(181,55))

fExterno = ctk.CTkFrame(janela, 
                        width=315, 
                        height=572, 
                        fg_color="#8D85E6", 
                        corner_radius=15, 
                        bg_color="transparent", 
                        border_width=3, 
                        border_color="#4C4966"
                        ).place(x=0,y=0)

fAtalhos = ctk.CTkFrame(janela, 
                     width=284, 
                     height=43, 
                     fg_color="#8C8AA6", 
                     corner_radius=15, 
                     bg_color="#8D85E6", 
                     border_width=3, 
                     border_color="#656472",
                     
                     ).place(x=14,y=89)

fTela = ctk.CTkFrame(janela, 
                     width=284, 
                     height=358, 
                     fg_color="#8C8AA6", 
                     corner_radius=15, 
                     bg_color="#8D85E6", 
                     border_width=3,
                     border_color="#656472"
                     ).place(x=14,y=143)

fbarra = ctk.CTkFrame(janela,
                      width=286,
                      height=2,
                      fg_color="#E6D785",
                      bg_color="#8D85E6"
                      ).place(x=15,y=67)

ftbn = ctk.CTkFrame(janela, 
                     width=123, 
                     height=38, 
                     fg_color="#4C4966", 
                     corner_radius=10, 
                     bg_color="#8D85E6", 
                     border_width=0, 
                     border_color="#656472",
                     
                     ).place(x=177,y=15)

ftbn1 = ctk.CTkFrame(janela, 
                     width=39, 
                     height=34, 
                     fg_color="#E6D785", 
                     corner_radius=10, 
                     bg_color="#4C4966", 
                     border_width=0, 
                     border_color="#656472",
                     
                     ).place(x=179,y=17)

ftbn2 = ctk.CTkFrame(janela, 
                     width=39, 
                     height=34, 
                     fg_color="#E6D785", 
                     corner_radius=10, 
                     bg_color="#4C4966", 
                     border_width=0, 
                     border_color="#656472",
                     
                     ).place(x=219,y=17)

ftbn3 = ctk.CTkFrame(janela, 
                     width=39, 
                     height=34, 
                     fg_color="#E6D785", 
                     corner_radius=10, 
                     bg_color="#4C4966", 
                     border_width=0, 
                     border_color="#656472",
                     
                     ).place(x=259,y=17)

logo = ctk.CTkLabel(janela, 
                    text= "",
                    image=logo_image
                    ).place(x=117, y=512)



janela.mainloop() #Roda janela  