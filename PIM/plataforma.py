import os
import time

def pensamento_logico():
    while True:
        print("\n--- Pensamento Lógico ---")
import os
import time

def pensamento_logico():
    while True:
        print("\n--- Pensamento Lógico ---")
        print("1 - Aula 1: O que é pensamento lógico? ")
        print("2 - Aula 2: Sequência e ordem lógica ")
        print("3 - Aula 3: Condições: 'se e senão' ")
        print("4 - Aula 4: Repetições e padrões ")
        print("5 - Aula 5: Pensamento lógico no dia a dia ")
        print("6 - Exercício 1")
        print("7 - Exercício 2")
        print("8 - Exercício 3")
        print("9 - Exercício 4")
        print("10 - Exercício 5")
        print("11 - Voltar ao menu principal")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if escolha == 1:
            print("Aula 1: O que é pensamento lógico? ")
            print("--- Objetivos ---\n Entender o que é pensamento lógico e por que ele é importante para resolver problemas. ")
            print()
            print("Pensamento lógico é a habilidade de raciocinar de forma organizada e coerente, usando regras e passos claros para chegar a uma conclusão. É como montar um quebra-cabeça: você observa as peças, testa encaixes, e segue uma linha de raciocínio até completar a figura.")
            print()
            print("Imagine que você quer fazer um café. O que você faz primeiro? \n 1. Pega o pó de café. \n 2. Coloca a água no. bule \n 3. Liga o fogo. \n 4. Espera a água ferver. \n 5. Coloca o pó no coador. \n 6. Passa água quente no pó.")
            print()
            print("Essa sequência é um exemplo de lógica: você segue passos específicos para alcançar um objetivo. Se inverter os passos, o café não dá certo.")
        
        elif escolha == 2:
            print("Aula 2: Sequência e ordem lógica. ")
            print("--- Objetivos --- \n Compreender a importância de seguir uma ordem correta para alcançar um resultado.")
            print()
            print("A sequência lógica é quando você realiza ações numa ordem correta para que tudo funcione bem. Em lógica, a ordem importa!")
            print()
            print("Imagine que você está se vestindo: \n 1. primeiro as roupas íntimas. \n 2. Depois a calça. \n 3. E por fim, o cinto.")
            print()
            print("Se você colocar o cinto antes da calça, algo está errado, não?")
        
        elif escolha == 3:
            print("Aula 3: Condições: 'se e senão'. ")
            print("--- Objetvos --- \n Entender como funcionam as decisões lógicas usando a estrutura “Se... então...”.")
            print()
            print("Muitas vezes, tomamos decisões com base em condições.")
            print()
            print("Se estiver chovendo, então levo guarda-chuva. \n Se tiver estudado, então posso fazer a prova tranquilo.")
        
        elif escolha == 4:
            print("Aula 4: Repetições e padrões. ")
            print("--- Objetivo --- \n Perceber padrões e como usá-los para resolver problemas repetitivos.")
            print()
            print("Muitas vezes, realizamos tarefas repetidas, e podemos encontrar padrões para facilitar.")
            print()
            print("Imagine que você está colocando cadeiras em uma sala para um evento: \n Você pega uma cadeira, anda até o lugar, coloca. \n Volta, pega outra cadeira, anda, coloca...")
            print()
            print("Você está repetindo a mesma ação várias vezes. Isso é um padrão de repetição.")
        
        elif escolha == 5:
            print("Aula 5: Pensamento lógico no dia a dia. ")
            print("--- Objetivo --- \n Perceber como usamos o pensamento lógico em diversas situações cotidianas e como ele nos ajuda a tomar decisões melhores.")
            print()
            print("Você já parou para pensar que usamos lógica o tempo todo, mesmo sem perceber? O pensamento lógico não serve só para resolver problemas difíceis, ele está presente nas decisões simples do dia a dia.")
            print()
            print('Organizar o tempo: \n “Tenho que sair às 8h. Se demoro 30 minutos para me arrumar, então preciso começar às 7h30. E se ainda quiser tomar café, preciso acordar às 7h." \n Fazer compras: \n “Se tenho 20 reais e o pão custa 5, o leite custa 7, e a manteiga custa 10… então não consigo comprar tudo. Qual combinação cabe no meu orçamento?”')
            print()
            print('Isso é lógica!')        
        elif escolha == 6:
            print()
            print("Exercício 1: Pense em outra atividade do dia a dia (como escovar os dentes) e escreva o passo a passo")
            print('A) Pegar escova de dente, colocar pasta, molhar a escova e escovar os dentes')
            print('B) abrir a torneira, colocar pasta de dente, pegar a escova e escovar.')
            print('C) escovar os dentes, abrir a torneira, colocar pasta e pegar a escova')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'A':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 7:
            print()
            print("Exercício 2: Organize as seguintes ações em uma ordem lógca: \n Pedir pizza \n Pegar o celular \n comer a pizza \n entrar no aplicativo de delivery ")
            print('A) Pedir pizza, pegar o celular, comer a pizza, entrar no aplicativo de delivery.')
            print('B) pegar o celular, entrar no aplicativo de delivery, pedir pizza e comer a pizza')
            print('C) comer pizza, pegar o celular, pedir a pizza, entrar no aplicativo de delivery')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 8:
            print()
            print("Exercício 3: Complete as frases: \n Se eu estiver com fome, então _____ \n Se eu quero andar mais rápido, então _____ \n Se eu quero aprender, então _____")
            print('A) Corro, estudo, como')
            print('B) Estudo, corro, como')
            print('C) Como, corro, estudo')
        
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'C':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 9:
            print()
            print("Exercício 4: Observe a sequência: \n 2, 4, 6, 8 ,__")
            print('Qual o padrão? E qual número vem depois?')
            print('A) 2, 4, 6, 8, 11.')
            print('B) 2, 4, 6, 8, 10.')
            print('C) 2, 4, 6, 8, 9.')

            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif escolha == 10:
            print()
            print("Exercício 5: Pense em uma situação da vida em que você precisa tomar uma decisão simples (qual roupa usar, por exemplo) \n 1. O que você precisa decidir. \n 2. Que informações você leva em conta. ")
            print('A) Preciso decidir qual roupa utilizar e levo em conta o local. ')
            print('B) Preciso decidir o local e levo em conta a cor da roupa.')
            print('C) Preciso decidir o dia e levo em conta o clima.')
       
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'A':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')     

        elif escolha == 11:
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

def seguranca_digital():
    while True:
        print("\n--- Segurança Digital ---")
        print("1 - Aula 1: O que é segurança digital?")
        print("2 - Aula 2: Senhas fortes e autenticação")
        print("3 - Aula 3: Phishing e engenharia social")
        print("4 - Aula 4: Segurança em redes Wi-Fi")
        print("5 - Aula 5: Proteção de dados pessoais")
        print("6 - Exercício 1")
        print("7 - Exercício 2")
        print("8 - Exercício 3")
        print("9 - Exercício 4")
        print("10 - Exercício 5")
        print("11 - Voltar ao menu principal")

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if escolha == 1:
            print("\nAula 1: Introdução aos conceitos de segurança digital.")
            print("--- OBJETIVOS ---\n Apresentar os conceitos básicos de segurança digital, sua importância no mundo digital e as principais ameaças.")
            print("--- Conteúdo ---\n Segurança digital é o conjunto de práticas e ferramentas usadas para proteger dados, dispositivos e redes contra acessos não autorizados. " \
            "As principais ameaças incluem malwares (como vírus e trojans), ataques de phishing (fraudes que tentam roubar senhas e dados) e engenharia social, onde o criminoso engana a vítima para obter informações. " \
            "Para se proteger, é importante usar antivírus atualizado, manter o firewall ativado, evitar clicar em links suspeitos e usar criptografia para proteger dados sensíveis. " \
            "Essas medidas ajudam a manter seus dispositivos e informações mais seguros.")
        
        elif escolha == 2:
            print("\nAula 2: Como criar senhas fortes e seguras.")
            print("--- OBJETIVOS ---\n Ensinar sobre a importância de senhas fortes e técnicas de autenticação para garantir a segurança dos sistemas.")
            print("--- Conteúdo ---\n Manter a segurança digital exige o uso de senhas fortes, únicas e difíceis de adivinhar, com pelo menos 12 caracteres misturando letras, números e símbolos. " \
            "É importante usar um gerenciador de senhas e nunca reutilizar a mesma senha em vários sites. " \
            "Ativar a autenticação multifatorial (2FA) adiciona uma camada extra de proteção, exigindo um segundo fator além da senha, como um código no celular. " \
            "Também é essencial adotar bons hábitos, como não clicar em links suspeitos e não compartilhar senhas com ninguém. " \
            "Esses cuidados simples ajudam a proteger suas contas e informações pessoais.")
        elif escolha == 3:
            print("\nAula 3: Como reconhecer ataques de phishing.")
            print("--- OBJETIVOS ---\n Explorar as técnicas de ataque de phishing e engenharia social, e como evitá-las.")
            print("--- Conteúdo ---\n Phishing é um tipo de golpe em que criminosos fingem ser empresas ou pessoas confiáveis para enganar a vítima e roubar dados, como senhas ou números de cartão. " \
            "Eles costumam usar e-mails falsos com links ou anexos perigosos. " \
            "É possível identificar esses e-mails por erros de ortografia, endereços suspeitos e mensagens que pressionam a vítima a agir rápido." \

            "Já a engenharia social é uma técnica usada por hackers para manipular pessoas e fazê-las entregar informações confidenciais. " \
            "Em vez de atacar sistemas, eles exploram a confiança e o descuido das vítimas." 
            "Ficar atento a mensagens estranhas e não clicar em links desconhecidos são formas importantes de se proteger..")
        
        elif escolha == 4:
            print("\nAula 4: Como manter sua rede Wi-Fi segura.")
            print("--- OBJETIVOS ---\n Ensinar sobre a importância de proteger redes Wi-Fi e como configurar redes seguras.")
            print("--- Conteúdo ---\n Redes Wi-Fi devem usar criptografia para proteger os dados transmitidos. " \
            "Os padrões mais seguros hoje são o WPA2 e o mais recente WPA3, que oferecem proteção contra invasões. " \
            "Usar senhas fortes na rede é essencial para impedir acessos não autorizados. Redes públicas, como as de cafés ou shoppings, apresentam riscos, pois podem ser monitoradas por terceiros. " \
            "Por isso, evite acessar dados sensíveis nelas e, se possível, use uma VPN para maior segurança.")
       
        elif escolha == 5:
            print("\nAula 5: Boas práticas para proteger dados pessoais.")
            print("--- OBJETIVOS ---\n Abordar as melhores práticas para proteger dados pessoais e a privacidade online.")
            print("--- Conteúdo ---\n A Lei Geral de Proteção de Dados (LGPD) protege os dados pessoais dos usuários no Brasil, garantindo mais controle sobre como essas informações são coletadas e usadas. " \
            "Em plataformas online, é importante revisar permissões, limitar o que é compartilhado e evitar fornecer dados desnecessários. " \
            "Nas redes sociais, configure a privacidade para restringir quem pode ver suas publicações, informações de perfil e localização. " \
            "Essas medidas ajudam a manter seus dados mais seguros e evitar abusos.")
        
       
        elif escolha == 6:
            print("\nExercício 1: Identifique práticas inseguras em senhas.")
            print('A) Usar combinações de letras, números e símbolos')
            print('B) Utilizar a mesma senha para várias contas')
            print('C) Alterar as senhas regularmente')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 7:
            print("\nExercício 2: Avalie se um e-mail é phishing.")
            print('A) Endereço de e-mail legítimo da empresa')
            print('B) Pedidos urgentes de atualização de informações financeiras')
            print('C) Avisos de promoções e descontos')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 8:
            print("\nExercício 3: Liste medidas de segurança para redes.")
            print('A) Utilizar WEP como método de criptografia')
            print('B) Configurar uma senha forte para a rede')
            print('C) Deixar a rede aberta para facilitar o acesso')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 9:
            print("\nExercício 4: Crie um plano de segurança digital pessoal.")
            print('A) Instalar um software antivírus')
            print('B) Criar senhas fortes e únicas')
            print('C) Usar autenticação de dois fatores')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 10:
            print("\nExercício 5: Classifique tipos de ataques e suas defesas.")
            print('A) Usar criptografia em e-mails')
            print('B) Evitar clicar em links desconhecidos e verificar a autenticidade do remetente')
            print('C) Instalar um firewall no computador')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == 11:
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

def programacao_python():
    while True:
        print("\n--- Programação com Python ---")
        print("1 - Aula 1: O que é Python")
        print("2 - Aula 2: Introdução ao Python e variáveis")
        print("3 - Aula 3: Condições (if/else)")
        print("4 - Aula 4: Laços de repetição")
        print("5 - Aula 5: Funções")
        print("6 - Exercício 1")
        print("7 - Exercício 2")
        print("8 - Exercício 3")
        print("9 - Exercício 4")
        print("10 - Exercício 5")
        print("11 - Voltar ao menu principal")

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if escolha == 1:
            print("\nAula 1: O que é Python?")
            print("\nO que é programação? Programar é dar instruções para o computador executar tarefas. É como ensinar uma receita passo a passo.")
            print("Programar é dar instruções para o computador executar tarefas. É como ensinar uma receita passo a passo.")
            print("\nPor que Python? ")
            print("É uma linguagem simples, fácil de ler e muito usada por iniciantes e profissionais (empresas como Google, Netflix e Instagram usam Python).")

        elif escolha == 2:
            print("Aula 2: Introdução à variáveis e à função print()")
            print('O que são Variáveis?\n')
            print('Uma variável é como uma caixa onde você pode guardar informações. Essa "caixa" pode armazenar números, \ntextos ou até listas de coisas. O legal das variáveis é que você pode mudar o conteúdo delas a qualquer momento, como se estivesse colocando algo novo dentro da caixa.\n')
            print("Como Criar uma Variável?\n")
            print("Em Python, criar uma variável é bem simples. Você só precisa escolher um nome para a variável e usar o sinal de igual (=) para atribuir um valor a ela.\n")
            print('Exemplo: idade = 25')
            
            print("\nA função print() é uma das mais usadas em Python.")
            print("Ela serve para exibir mensagens, números ou resultados na tela do programa.")
            print("Sempre que você quiser mostrar alguma coisa para o usuário, use o print().\n")

            print("Sintaxe básica:")
            print("Você deve escrever a palavra print, abrir e fechar parênteses, e colocar o que deseja mostrar dentro deles.")
            print("Se for um texto, coloque entre aspas duplas (\") ou simples (').\n")

            print("Exemplos:")
            print('print("Olá, mundo!")  → Vai mostrar: Olá, mundo!')
            print("print('Python é legal!')  → Vai mostrar: Python é legal!")
            print("print(123)  → Vai mostrar: 123 (sem aspas porque é número)\n")

            print("Dicas importantes:")
            print("- Sempre use os parênteses, mesmo que seja só um texto simples.")
            print('- Use aspas para textos. Tanto aspas duplas ("") quanto simples (\'\') funcionam.')
            print("- Você pode usar o print para mostrar variáveis também.")
            print("Por exemplo: ")
            print("idade = 25")
            print('print(idade)')
            print('neste caso vai mostrar: 25.')
            print("- Se quiser mostrar várias coisas ao mesmo tempo, separe por vírgulas dentro do print().")
    
            print("\nExemplo com várias informações:")
            print('print("Seu nome é", "Ana", "e você tem", 18, "anos.")')
            print("Saída: Seu nome é Ana e você tem 18 anos.")

        elif escolha == 3:
            print("Aula 3: O que são if e else?")
            print("\nEm Python, usamos o 'if' para fazer verificações de condição.")
            print("Ou seja, o programa vai checar se algo é verdadeiro. Se for, ele executa um bloco de código.")
            print("Se a condição não for verdadeira, usamos o 'else' para dizer o que fazer no caso contrário.\n")

            print("Explicando de forma simples:")
            print("- if = 'se' alguma coisa for verdadeira, faça isso")
            print("- else = 'senão', ou seja, caso a condição do if seja falsa, faça outra coisa\n")

            print("Exemplo prático:")
            print("idade = 18")
            print("if idade >= 18:")
            print("    print('Você é maior de idade.')")
            print("else:")
            print("    print('Você é menor de idade.')\n")

            print("Dica fácil para lembrar:")
            print("Se (if) isso for verdade, faça isso.")
            print("Senão (else), faça aquilo.")

        elif escolha == 4:
            print("Aula 4: Criando loops com for e while")
            print("\nEm Python, usamos os loops para repetir ações automaticamente.")
            
            print("\nO que é o loop for?")
            print("- O 'for' serve para repetir algo um número específico de vezes.")
            print("- É usado quando você já sabe quantas vezes quer repetir.")
            
            print("Exemplo com for:")
            print("for i in range(5):")
            print("print('Repetindo...')  #Isso será exibido 5 vezes\n")

            print("O que é o loop while?")
            print("- O 'while' repete algo enquanto uma condição for verdadeira.")
            print("- Quando a condição se torna falsa, ele para automaticamente.")
            
            print("Exemplo com while:")
            print("contador = 0")
            print("while contador < 3:")
            print("print('Contando...')  #Será exibido enquanto contador for menor que 3")
            print("contador += 1  # Vai somando 1 até parar\n")

            print("Dica importante:")
            print("- Use 'for' quando souber o número de repetições.")
            print("- Use 'while' quando quiser repetir até que algo mude.")

        elif escolha == 5:
            print("Aula 5: Definindo e utilizando funções")
            
            print("\nO que é uma função?")
            print("Uma função em Python é um bloco de código que só executa quando você chama.")
            print("Ela serve para organizar o código, reutilizar trechos e deixá-lo mais limpo e fácil de entender.")
            
            print("\nComo criar uma função?")
            print("- Use a palavra-chave 'def', seguida do nome da função e parênteses ().")
            print("- Depois, escreva os comandos que você quer que essa função execute.")
            
            print("\nExemplo de definição de função:")
            print("def saudacao():")
            print("    print('Olá, seja bem-vindo!')")

            print("\nComo chamar uma função?")
            print("- Basta escrever o nome da função com parênteses.")
            print("Exemplo:")
            print("saudacao()  # Isso vai mostrar: Olá, seja bem-vindo!\n")

            print("Dica:")
            print("- Você pode criar funções com ou sem parâmetros (valores que você passa para a função).")
            print("- Vamos ver isso melhor em aulas futuras!")

        elif escolha == 6:
            print("Exercício 1: Como exibir a frase 'Olá, mundo!' na tela utilizando a função print em Python?")
            print('A) print(Olá Mundo!)')
            print('B) print("Olá Mundo!")')
            print('C) print"(Olá Mundo!)"')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif escolha == 7:
            print("Exercício 2: crie 2 variavies e some-as")
            print('A) numero1 = 2, numero2 = 2, print(numero1 + numero2)')
            print('B) numero1 = 2, numero2 = 2, print(numero1 = numero2)')
            print('C) numero1 = 2, numero2 = 2, print(numero1 - numero2)')
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'A':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif escolha == 8:
            print("Exercício 3: Utilizando if e else faça um programa que se o usuario tiver 18 anos esta liberado, caso contrário repovado")
            print('A) idade = int(input("Digite sua idade: "))\n if idade <= 18 \n print("Liberado") \n else: \n print("negado")')
            print('B) if idade => 18 \n print("Liberado") \n else: \n print("negado")')
            print('C) idade = int(input("Digite sua idade: "))\n if idade => 18 \n print("Liberado") \n else: \n print("negado")') 
            
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'C':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif escolha == 9:
            print("Exercício 4: Utilizando for i in range faça-o contar ate 5.")
            print('A) for i in range(5)')
            print('B) for i in range(1, 6): \n  print(i)')
            print('C) for i in range(7) \n print(for i in range)') 
             
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif escolha == 10:
            print("Exercício 5: Crie uma função de soma.")
            print('A) def somar(2, 2): \n return 2, 2')
            print('B) def somar(a, b): \n return a + b')
            print('C) def somar(1, 2): \n return def') 
             
            resposta = input("Digite a alternativa correta (A, B ou C): ").strip().upper()
            if resposta == 'B':
                print('Parabéns, você acertou!')
            else:
                print('Tente revisar as aulas novamente')

            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif escolha == 11:
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print('\n--- Menu Principal ---')
        print('1 - Pensamento lógico')
        print('2 - Segurança digital')
        print('3 - Introdução à programação com Python')
        print('4 - Sair')

        try:
            opcao = int(input('Digite a opção: '))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            pensamento_logico()
        elif opcao == 2:
            seguranca_digital()
        elif opcao == 3:
            programacao_python()
        elif opcao == 4:
            print('Obrigado e até a próxima.')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()