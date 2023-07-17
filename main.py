lis_nome = []
lis_cpf = []
lis_contato = []
lis_email = []
lis_endereco = []
from time import sleep 

def login():
    print(f'{">>>>>> BEM VINDO AO BANCO PRISTEN <<<<<<":~^40}')
    print(f'{" LOGIN ":~^40}')
    print('\n')
    conta = str(input('Você já tem conta? [S] / [N]: ')) .upper() .strip()
    if conta not in 'SN':
        print('Digite uma opçãoa válida!')
        return login()
    elif conta == 'S':
        return menu()
    else:
        cadastrar()
    print('~' * 40)



def menu():
    print(f'{" BANCO PRISTEN ":~^40}')
    print(f'{"MENU ":-^40}')
    print('[1] VOLTAR A TELA DE LOGIN')
    print('[2] CONSULTAR')
    print('[3] ATUALIZAR')
    print('[4] EXCLUIR')
    print('[5] ENCERRAR')
    print(f'{"-":-^40}')
    opcao = str(input('Digite uma opção que deseja acessar: '))
    if opcao == "1":
        return login()
    elif opcao == "2":
        return consulta()
    elif opcao  in "3":
        return atualizar()
    elif opcao == '4':
        return excluir()
    elif opcao == '5':
        return encerrar()
    else:
        print('Escolha uma opcão válida!')
    return menu()


def cadastrar():       
    print(f'{" CADASTRO ":~^40}') 
    nome = (str(input('NOME: '))) .upper()
    lis_nome.append(nome)
    cpf = str(input('CPF: '))
    lis_cpf.append(cpf)
    email = str(input('E-MAIL: '))
    lis_email.append(email)
    contato = str(input('CONTATO: '))
    lis_contato.append(contato)
    endereco = str(input('ENDEREÇO: '))
    lis_endereco.append(endereco)
    print('Cadastrado com sucesso!!!')
    print('\n')
    menu()


def consulta():
    pessoa = str(input('Nome da pessoa que deseja consultar: ')) .upper() # colocar um validador se caso nao tiver o nome na alista
    if pessoa in lis_nome:
        cliente = lis_nome.index(pessoa)
    print(f'{"CONSULTAR CLIENTE":~^40}')
    print()
    print(f'Nome:     \t{lis_nome[cliente]}')
    print(f'CPF:      \t{lis_cpf[cliente]}')
    print(f'E-mail: \t{lis_email[cliente]}')
    print(f'Contato: \t{lis_contato[cliente]}')
    print(f'Endereço: \t{lis_endereco[cliente]}')
    return menu()


def atualizar():
    print(f'{" ATUALIZAR ":~^40}')
    pessoa = input('Informe o nome da conta que deseja atualizar: ') .upper()
    mudar = lis_nome.index(pessoa)
    print(f'[1] Nome: {lis_nome[mudar]}')
    print(f'[2] CPF: {lis_cpf[mudar]}')
    print(f'[3] E-mail: {lis_email[mudar]}')
    print(f'[4] Contato: {lis_contato[mudar]}')
    print(f'[5] Endereço: {lis_endereco[mudar]}')
    print('-' * 30)
    resp = 1
    while resp != '2':
        att = int(input('Digite o numero do dado para atualizar: '))
        if att == 1:
            lis_nome[mudar] = str(input('Nome: '))
        elif att == 2:    
            lis_cpf[mudar] = int(input('CPF: '))
        elif att == 3:    
            lis_email[mudar] = str(input('E-mail: '))
        elif att == 4:    
            lis_contato[mudar] = int(input('Contato: '))
        elif att == 5:    
            lis_endereco[mudar] = str(input('Endereço: '))
        else:
            print('DIGITE UMA OPÇAO VÁLIDA!')
            return atualizar()
        resp = str(input('Quer atualizar outra informação? [1]Sim / [2]Não'))
    print(f'<<<<<<< DADOS ATUALIZADOS >>>>>>>')
    print(f'Nome:     \t{lis_nome[mudar]}')
    print(f'CPF:      \t{lis_cpf[mudar]}')
    print(f'E-mail: \t{lis_email[mudar]}')
    print(f'Contato: \t{lis_contato[mudar]}')
    print(f'Endereço: \t{lis_endereco[mudar]}')
    print('-=' * 40)
    print('\n')
    return menu()
    

def excluir():
    print()
    print('\n')
    print(f'{"EXCLUIR CONTA":~^40}')
    nome_cliente = input('Digite o nome da conta que deseja excluir: ') .upper() .strip()
    print('-' * 27)
    d = lis_nome.index(nome_cliente) 
    print(f'Nome:     \t{lis_nome[d]}')
    print(f'CPF:      \t{lis_cpf[d]}')
    print(f'E-mail: \t{lis_email[d]}')
    print(f'Contato: \t{lis_contato[d]}')
    print(f'Endereço: \t{lis_endereco[d]}')
    print('-' * 27)
    ctz = str(input('Tem certeza que deseja excluir essa conta? [S] / [N]')) .upper()
    print('\n')   
    if ctz == 'S':
        del lis_nome[d]
        del lis_contato[d]
        del lis_cpf[d]
        del lis_endereco[d]
        del lis_email[d]
        print('Conta excluída com sucesso!!!') .upper()
        return menu()
    elif ctz == 'N':
        return menu()
    else:
        print('Por favor digite [S] ou [N]')
        return excluir()
    
def encerrar():
    print(f'{"  ENCERRANDO PROGRAMA... ":~^40}')
    sleep(3)
    print(f'{"<<< PROGRAMA ENCERRADO >>>":^38}')



login()