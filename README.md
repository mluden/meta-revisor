# Revisador de Postagens Instagram e Facebook (Versão Beta)

**Revisador de Postagens** é uma ferramenta desenvolvida em Python com o objetivo de auxiliar agências, analistas e social media a monitorar as postagens mais recentes de contas comerciais no Instagram e Facebook, utilizando a API da Meta.

> 🔄 Projeto em desenvolvimento — versão **beta** funcional com simulação de dados.

---

## 🧠 Funcionalidades

- ✅ Interface gráfica com Tkinter.
- ✅ Adição de até **10 usuários do Instagram** para revisão.
- ✅ Armazenamento dos usuários localmente (`usuarios.json`).
- ✅ Simulação de revisão de postagens com:
  - Data da última publicação (formato `dd/mm/aaaa`)
  - Tempo desde a publicação (em dias)
  - Tipo de conteúdo (Reels ou Foto)
  - Número de curtidas
- 🚫 Indicação clara de quando **não há Facebook vinculado**.
- 🖼️ (Em breve) Exibição da **foto de perfil** ao lado de cada usuário.
- 🔒 Uso de token via `.env` (com suporte a API real da Meta).
- ⚙️ Preparado para ser empacotado como **executável (.exe)** usando `PyInstaller`.

---

## 🚧 Em desenvolvimento

- Integração real com a API Graph da Meta.
- Consulta automatizada da conta vinculada ao Facebook.
- Exibição expandida com detalhes da última postagem ao clicar no usuário.
- Cache de imagens de perfil.

---

## 🔗 Versão em inglês

👉 [English version of this README]

---

## 📦 Executável

Você pode compilar o código com `PyInstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed revisador_postagens_meta.py
