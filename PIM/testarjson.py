import json


with open("conteudo_curso.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


print("\n--- Conteúdo do JSON ---\n")
print(json.dumps(dados, indent=4, ensure_ascii=False))