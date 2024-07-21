import requests
from fastapi import status


class ListOfUser:
    def __init__(self, username):
        self._username = username

    def requisition_api(self):
        answer = requests.get(f'https://api.github.com/users/{self._username}')
        if answer.status_code == status.HTTP_200_OK:
            return answer.json()
        else:
            return answer.status_code

    def print_user(self):
        data_api = self.requisition_api()
        if type(data_api) is not int:
            print("--------------------------------------- [ GitHub Usuário ] ---------------------------------------")
            print()

            print(f"Nome: {data_api['name']}")
            print(f"Foto: {data_api['avatar_url']}")
            if {data_api['company']} is not None:
                print(f"Empresa: {data_api['company']}")
            if {data_api['blog']} is not None:
                print(f"Site: {data_api['blog']}")
            if {data_api['public_repos']} != 0:
                print(f"Quantidade de Repositórios Públicos: {data_api['public_repos']}")
            else:
                print("Quantidade de Repositórios Públicos: 0")

        else:
            print(data_api)


class ListOfRepo:
    def __init__(self, username):
        self._username = username

    def requisition_api(self):
        answer = requests.get(f'https://api.github.com/users/{self._username}/repos')
        if answer.status_code == status.HTTP_200_OK:
            return answer.json()
        else:
            return answer.status_code

    def print_repositories(self):
        data_api = self.requisition_api()
        if type(data_api) is not int:
            print("--------------------------------------- [ GitHub Repositórios ] ---------------------------------------")
            print()

            for i in range(len(data_api)):
                print(f"{i} - Nome: {data_api[i]['name']}")
                print(f"Criado em: {data_api[i]['created_at']}")
                print(f"Atualizado em: {data_api[i]['updated_at']}")
                print()

        else:
            print(data_api)


class MenuOpcoes:
    def __init__(self, username):
        self._username = username

    def selectOption(self, username):
        self._username = username

        while True:
            print()
            print('--------------------------------- [ Menu de Opções ] ---------------------------------')
            print()

            options = {
                1: "Perfil do Usuário",
                2: "Consultar Repositórios",
                3: "Finalizar Programa",
            }

            for i in range(len(options)):
                print(f"{i+1} - {options[i+1]}")
            print()

            try:
                optionConsult = int(input('Digite a opção desejada (somente número): '))
                print()
                while optionConsult <= 0 or optionConsult > 3:
                    optionConsult = int(input('Opção inexistente, digite novamente: '))
                    print()

                if optionConsult == 1:
                    ListOfUser(username).print_user()

                if optionConsult == 2:
                    ListOfRepo(username).print_repositories()

                if optionConsult == 3:
                    opcao = input('Deseja realmente finalizar a consulta (S/N)? ').lower()
                    if opcao == 's':
                        print('Este programa foi finalizada com sucesso!')
                        break
                    else:
                        continue

            except ValueError:
                print(f'Ocorreu um erro: Não digitar caracteres como letra, especiais e outros, somente números!!')


if __name__ == '__main__':
    user = input('Digite o nome do usuário que deseja consultar: ')
    MenuOpcoes(user).selectOption(user)
