'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class TaskHandler:
    def handle_task(self):
        if self.__conect_api:
            option = self.__option_selector()
            
            self.__options(option)
    
    def __conect_api(self):
        # conecta a API
        print("Conectado à API")
        return True

    def __option_selector(self):
        print("Selecione o que deve ser feito")
        print("1 - Criar Tarefa")
        print("2 - Atualizar Tarefa")
        print("3 - Remover Tarefa")
        print("4 - Enviar Notificação")
        print("5 - Gerar Relatório")
        print("6 - Enviar Relatório")
        option = int(input())
        return option

    def __options(self, option ):
        if option == 1:
            self.__create_task(self,)
        elif option == 2:
            self.__update_task(self)
        elif option == 3:
            self.__remove_task(self)
        elif option == 4:
            self.__send_notification(self)
        elif option == 5:
            self.__generate_report(self)
        elif option == 6:
            self.__send_report(self)

    def __create_task(self, task):
        # cria uma tarefa
        print("Criando tarefa...")
        print("Tarefa criada com sucesso!")
        pass

    def __update_task(self, task):
        # atualiza uma tarefa
        print("Atualizando tarefa...")
        print("Tarefa atualizada com sucesso!")
        pass

    def __remove_task(self, task):
        # remove uma tarefa
        print("Removendo tarefa...")
        print("Tarefa removida com sucesso!")
        pass

    def __send_notification(self, task):
        # envia uma notificação
        print("Enviando notificação...")
        print("Notificação enviada com sucesso!")
        pass

    def __generate_report(self, task):
        # gera um relatório
        print("Gerando relatório...")
        print("Relatório gerado com sucesso!")
        pass

    def __send_report(self, task):
        # envia um relatório
        print("Enviando relatório...")
        print("Relatório enviado com sucesso!")
        pass

taskhandler = TaskHandler()
taskhandler.handle_task()
