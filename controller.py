# controller.py
from flask import Flask, render_template, request
from model import ModuloLivraria

app = Flask(__name__)

# Instancia o domínio de negócio isolado
sistema_livraria = ModuloLivraria()

@app.route("/", methods=["GET", "POST"])
def gerenciar_livraria():
    # Roteamento da ação do usuário (Computador -> Caixa Azul)
    if request.method == "POST":
        titulo = request.form.get("titulo_livro")
        autor = request.form.get("autor_livro")
        # Controlador aciona a lógica de dados
        sistema_livraria.registrar_livro(titulo, autor)
    
    # Controlador busca o estado atual (Caixa Azul -> Banco de Dados)
    acervo_atualizado = sistema_livraria.consultar_acervo()
    
    # Controlador devolve a resposta (Caixa Azul -> Computador)
    return render_template("index.html", livros=acervo_atualizado)

if __name__ == "__main__":
    app.run(debug=True)