import tkinter as tk


# On crée la fenêtre principale avec un titre et un fond
fenetre = tk.Tk()
fenetre.title("CryptoSturm")
fenetre['bg'] = '#FA8072'


def negatif(im):
    for i in range(H): # On parcours les lignes de pixels de l'image
        for j in range(L): # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (255 - r, 255 - v, 255 - b))
    nouvelle_image.save("image/negatif.jpg", "JPEG")
    variable.set("image/negatif.jpg")
    im.tkimage = ImageTk.PhotoImage(nouvelle_image)
    canvas2.itemconfig(1, image=im.tkimage)


def claire(n, im):
    for i in range(H):  # On parcours les lignes de pixels de l'image
        for j in range(L):  # On parcours les pixels de la ligne i
            (r, v, b) = originale.getpixel((j, i))
            nouvelle_image.putpixel((j, i), (r + n, v + n, b + n))
    nouvelle_image.save("image/plusclair.jpg", "JPEG")
    variable.set("image/plusclair.jpg")
    im.tkimage = ImageTk.PhotoImage(nouvelle_image)
    canvas2.itemconfig(1, image=im.tkimage)


# Nous allons créer deux frames
message_clair = tk.LabelFrame (fenetre,text="Message en clair", bg="green", width=500, height=500)
message_clair.grid(row=0, column=0, sticky='W')
message_chiffre = tk.LabelFrame (fenetre,text="Message chiffré", bg="red", width=500, height=500)
message_chiffre.grid(row=0, column=1, sticky='W')
# à l'interieur de chacune des frames
bouton_negatif = tk.Button(message_clair, text="Hash", command=lambda: negatif(mon_image))
bouton_negatif.grid(row=2, column=0, sticky='N', pady=2)
bouton_clair = tk.Button(message_chiffre, text="Check hash", command=lambda: claire(200, mon_image))
bouton_clair.grid(row=2, column=1, sticky='N', pady=2)
# Les inputs
variable = tk.StringVar()
variable.set("")
e1 = tk.Entry(message_clair, textvariable=variable, width=50, fg='blue')
e2 = tk.Entry(message_chiffre, bg='#999999', width=50)
e1.grid(row=0, column=0, columnspan=6, sticky='W', ipadx=10, ipady=50)
e2.grid(row=0, column=0, columnspan=6, sticky='W', ipadx=10, ipady=50)
# Le bouton de chiffrement
bouton = tk.Button(fenetre, text="process", fg="red", bg="white", relief="raised",
                overrelief="sunken")
bouton.grid(row=1, column=0, columnspan=2, sticky='N'+'W'+'E', pady=2)
# Le bouton qui permet de quitter l'application.
bouton = tk.Button(fenetre, text="Quit", fg="red", bg="white", relief="raised",
                overrelief="sunken", command=fenetre.destroy)
bouton.grid(row=2, column=0, columnspan=2, sticky='N'+'W'+'E', pady=2)
fenetre.mainloop()
