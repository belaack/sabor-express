import os

restaurantes = [{'nome':'Hiroshi' , 'categoria':'Japonesa' , 'ativo': False} , 
                {'nome':'Frutaria SP' , 'categoria':'Comida Saudável' , 'ativo': True}
                ]


def exibir_nome_programa():
    '''Funcao que exibe o nome do programa no console'''
    print("""
        
    █▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 █▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ▀▀█ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 █▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▀▀▀ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀
        """)

def exibir_opcoes():
    '''Exibe as opcoes da aplicacao sabor express'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Finalizar app\n')

def finalizar_app():
    '''Finaliza o aplicativo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Volta ao menu principal com as opcoes'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    '''Mostra a mensagem de opcao invalida caso o usuario inpute uma opcao / valor que nao existe '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Comando padrão assim que a opcao é escolhida, limpa a tela e mostra o subtítulo'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Cadastra um restaurante novo pelo seu nome'''
    exibir_subtitulo('Cadastro de restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante , 'categoria' : categoria , 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista os restaurantes cadastrados'''
    exibir_subtitulo('Listar restaurantes')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False 
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True 
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''Permite escolher a funcao'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))      

        if opcao_escolhida == 1:    
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Funcao principal/geral da aplicacao'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()