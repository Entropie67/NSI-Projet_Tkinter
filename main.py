import tkinter as tk


# On crée la fenêtre principale avec un titre et un fond
fenetre = tk.Tk()
fenetre.title("CryptoSturm")
fenetre['bg'] = '#FA8072'


def chiffrement():
    m = message.get()
    m = "TRTR" + m + "TRTR"
    message_c.set(m)


def dechiffrer():
    ##variable.set("something")
    return True

# Nous allons créer deux frames
message_clair = tk.LabelFrame (fenetre,text="Message en clair", bg="green", width=500, height=500)
message_clair.grid(row=0, column=0, sticky='W')
message_chiffre = tk.LabelFrame (fenetre,text="Message chiffré", bg="red", width=500, height=500)
message_chiffre.grid(row=0, column=1, sticky='W')
# à l'interieur de chacune des frames
bouton_chiffre = tk.Button(message_clair, text="Chiffrer !", command=lambda: chiffrement())
bouton_chiffre.grid(row=2, column=0, sticky='N', pady=2)
bouton_clair = tk.Button(message_chiffre, text="Dechiffrer", command=lambda: dechiffrer())
bouton_clair.grid(row=2, column=1, sticky='N', pady=2)
# Les inputs
message = tk.StringVar()
message.set("Taper le message que vous souhaitez chiffrer.")
message_c = tk.StringVar()
message_c.set("lkdjfqlghqsiefjskldsj:fkdngv,.")
e1 = tk.Entry(message_clair, textvariable=message, width=50, fg='blue')
e2 = tk.Entry(message_chiffre, textvariable=message_c, bg='#999999', width=50)
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
