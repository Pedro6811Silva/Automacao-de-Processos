import os
import shutil
import hashlib

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Ferramenta de Automação Administrativa ===")
    print("1. Mover pastas com termos pré-definidos")
    print("2. Renomear arquivos/pastas em ordem")
    print("3. Apagar duplicatas")
    print("4. Separar pastas e documentos")
    print("5. Excluir termos de nomes")
    print("6. Procurar e filtrar por termos")
    print("0. Sair")

def mover_pastas(origem, destino, termos):
    for item in os.listdir(origem):
        if os.path.isdir(os.path.join(origem, item)):
            for termo in termos:
                if termo in item:
                    shutil.move(os.path.join(origem, item), destino)
    print("Pastas movidas com sucesso!")

def renomear_items(origem, nomes):
    items = os.listdir(origem)
    for i, item in enumerate(items):
        novo_nome = nomes[i]
        os.rename(os.path.join(origem, item), os.path.join(origem, novo_nome))
    print("Itens renomeados!")

def remover_duplicatas(origem):
    hashes = {}
    for item in os.listdir(origem):
        caminho = os.path.join(origem, item)
        if os.path.isfile(caminho):
            with open(caminho, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in hashes:
                os.remove(caminho)
            else:
                hashes[file_hash] = caminho
    print("Duplicatas removidas!")

def separar_pastas_docs(origem, destino):
    pastas = os.path.join(destino, "Pastas")
    docs = os.path.join(destino, "Documentos")
    os.makedirs(pastas, exist_ok=True)
    os.makedirs(docs, exist_ok=True)

    for item in os.listdir(origem):
        caminho = os.path.join(origem, item)
        if os.path.isdir(caminho):
            shutil.move(caminho, pastas)
        else:
            shutil.move(caminho, docs)
    print("Separação concluída!")

def excluir_termos(origem, termos):
    for item in os.listdir(origem):
        novo_nome = item
        for termo in termos:
            novo_nome = novo_nome.replace(termo, "")
        os.rename(os.path.join(origem, item), os.path.join(origem, novo_nome))
    print("Termos excluídos dos nomes!")

def filtrar_movercopiar(origem, destino, termos):
    for item in os.listdir(origem):
        for termo in termos:
            if termo in item:
                shutil.copy(os.path.join(origem, item), destino)
    print("Itens filtrados e copiados!")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            origem = input("Diretório de origem: ")
            destino = input("Diretório de destino: ")
            termos = input("Termos separados por vírgula: ").split(",")
            mover_pastas(origem, destino, termos)

        elif opcao == "2":
            origem = input("Diretório: ")
            nomes = input("Novos nomes separados por vírgula: ").split(",")
            renomear_items(origem, nomes)

        elif opcao == "3":
            origem = input("Diretório: ")
            remover_duplicatas(origem)

        elif opcao == "4":
            origem = input("Diretório de origem: ")
            destino = input("Diretório de destino: ")
            separar_pastas_docs(origem, destino)

        elif opcao == "5":
            origem = input("Diretório: ")
            termos = input("Termos a excluir separados por vírgula: ").split(",")
            excluir_termos(origem, termos)

        elif opcao == "6":
            origem = input("Diretório de origem: ")
            destino = input("Diretório de destino: ")
            termos = input("Termos separados por vírgula: ").split(",")
            filtrar_movercopiar(origem, destino, termos)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
