# revisador_postagens_meta.py

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk
import requests
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# carregando as variaveis de ambiente
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  # TOKEN .ENV

USER_DATA_FILE = "usuarios.json"

class RevisadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Revisador de Postagens Instagram e Facebook")
        self.usuarios = self.carregar_usuarios()

        self.frame_topo = tk.Frame(root)
        self.frame_topo.pack(pady=10)

        self.input_usuario = tk.Entry(self.frame_topo, width=30)
        self.input_usuario.pack(side=tk.LEFT, padx=5)

        self.btn_adicionar = tk.Button(self.frame_topo, text="Adicionar Usuário", command=self.adicionar_usuario)
        self.btn_adicionar.pack(side=tk.LEFT)

        self.btn_revisar = tk.Button(root, text="REVISAR", command=self.revisar_postagens, bg="green", fg="white")
        self.btn_revisar.pack(pady=10)

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("nome", "instagram", "facebook")
        self.tree.column("#0", width=50, anchor="center")
        self.tree.column("nome", anchor="w", width=150)
        self.tree.column("instagram", anchor="center", width=200)
        self.tree.column("facebook", anchor="center", width=200)

        self.tree.heading("#0", text="#")
        self.tree.heading("nome", text="Usuário")
        self.tree.heading("instagram", text="Instagram")
        self.tree.heading("facebook", text="Facebook")

        self.tree.pack(padx=10, pady=10)

        self.carregar_na_interface()

    def carregar_usuarios(self):
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as f:
                return json.load(f)
        return []

    def salvar_usuarios(self):
        with open(USER_DATA_FILE, 'w') as f:
            json.dump(self.usuarios, f)

    def adicionar_usuario(self):
        usuario = self.input_usuario.get().strip()
        if not usuario:
            return
        if len(self.usuarios) >= 10:
            messagebox.showwarning("Limite", "Máximo de 10 usuários atingido.")
            return

        if usuario in [u['nome'] for u in self.usuarios]:
            messagebox.showinfo("Usuário existente", "Este usuário já foi adicionado.")
            return

        # Simula verificação básica
        self.usuarios.append({"nome": usuario})
        self.salvar_usuarios()
        self.carregar_na_interface()

    def carregar_na_interface(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, usuario in enumerate(self.usuarios):
            self.tree.insert("", "end", text=str(i+1), values=(usuario['nome'], "-", "-"))

    def revisar_postagens(self):
        for i, usuario in enumerate(self.usuarios):
            nome = usuario['nome']
            # Aqui deveria ir a chamada real à API da Meta com o token e o nome de usuário
            # Abaixo, dados mockados para simular a resposta

            data_instagram = datetime.now() - timedelta(days=i*2 + 1, hours=3)
            tipo_instagram = "Reels" if i % 2 == 0 else "Foto"
            curtidas_instagram = 150 + i * 10

            instagram_txt = f"{data_instagram.strftime('%d/%m/%Y')} ({(datetime.now() - data_instagram).days} dias) - {tipo_instagram} - {curtidas_instagram} ❤"
            facebook_txt = "FACEBOOK NAO VINCULADO"

            self.tree.item(self.tree.get_children()[i], values=(nome, instagram_txt, facebook_txt))


if __name__ == "__main__":
    root = tk.Tk()
    app = RevisadorApp(root)
    root.mainloop()