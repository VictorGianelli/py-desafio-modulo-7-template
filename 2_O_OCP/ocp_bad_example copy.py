'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''
import time

class AprovaExame:
    def aprovar_solicitacao(self, solicitacao: any) -> None:
        solicitacao.aprovar_exame()

    def aprovar_solicitacao_exame(self, exame):
        if clinica.verifica_condicoes(exame,verificacao_feita=False):
            print("Exame aprovado!")
            time.sleep(1)
            exame_feito = clinica.do_exame(exame,exame_feito=False)
            if exame_feito:
                print("Exame executado com sucesso!")     
    

class Raio_X:
    def fazer_exame(self, exame_feito: bool):
        # implemente as condições específicas do exame de raio-x
        if exame == exame_raio_x:
            print("Fazendo exame de raio-x...")
            time.sleep(2)
            exame_feito = True
            return exame_feito
        else:
            return False

    def verifica_condicoes(self, verificacao_feita: bool):
        if exame == exame_raio_x:
            print("Aguardando aprovação do Raio-X!")
            time.sleep(2)
            verificacao_feita = True
            return verificacao_feita

class Sangue:
    def fazer_exame(self, exame_feito: bool):
        # implemente as condições específicas do exame de sangue
        if exame == exame_sangue:
            print("Fazendo exame de sangue...")
            time.sleep(2)
            exame_feito = True
            return exame_feito
        else:
            return False

    def verifica_condicoes(self, verificacao_feita: bool):
        print("Aguardando aprovação do exame de sangue!")
        time.sleep(2)
        verificacao_feita = True
        return verificacao_feita
        

class Clinica:

    def do_exame(self, exame: any, exame_feito: bool) -> None:
        exame_feito = exame.fazer_exame(exame_feito)
        return exame_feito

    def verifica_condicoes(self, exame: any, verificacao_feita: bool) -> bool:
        verificacao_feita = exame.verifica_condicoes(verificacao_feita)
        return verificacao_feita

clinica = Clinica()
# aprovar_exame = AprovaExame()
exame_sangue = Sangue()
exame_raio_x = Raio_X()

aprovador = AprovaExame()

exame: Clinica = exame_raio_x
# clinica.do_exame(exame)
aprovador.aprovar_solicitacao_exame(exame)


