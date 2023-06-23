import random
import time

cont_colisoes = 0
cont_descartes = 0
cont_transmitido = 0


class Dispositivo:
    def __init__(self, id):
        self.id = id
        self.tempo_espera = 0
        self.colisoes = 0
        # self.multiplicador = 1
        self.multiplicador = random.randint(1, 9)

    def quer_transmitir(self):
        return random.randint(0, 100) < 50

    def detectou_colisao(self):
        global cont_colisoes
        global cont_descartes
        if self.colisoes < 10:
            cont_colisoes += 1
            self.colisoes += 1
            # self.tempo_espera = random.randint(1, 10)
            self.tempo_espera = self.multiplicador * 2
            # self.tempo_espera = self.multiplicador * 3
            self.multiplicador += 1
        else:
            cont_descartes += 1
            self.descartar_quadro()

    def tempo_espera_nao_passou(self):
        if self.tempo_espera > 0:
            self.tempo_espera -= 1
            return False
        return True

    def descartar_quadro(self):
        self.colisoes = 0
        self.tempo_espera = 0
        print(f"Quadro descartado após 10 colisões, Máquina: ", self.id)


def simulador(dispositivos, tempo_simulacao):
    for t in range(tempo_simulacao):
        print("Tempo:", t)

        # Seleciona dispositivos que não estejam em backoff e queiram transmitir
        transmissores = [
            dispositivo for dispositivo in dispositivos
            if dispositivo.tempo_espera_nao_passou() and dispositivo.quer_transmitir()
        ]

        # Se mais de um transmissor desejar transmitir, significa que houve uma colisão
        if len(transmissores) > 1:
            for dispositivo in transmissores:
                # Coloca os transmissores colididos em backoff
                dispositivo.detectou_colisao()
            print("Colidiu! ", end=" ")
            for transmissor in transmissores:
                print(transmissor.id, end=", ")
            print()
        # Senão, tá liberado para transmitir
        else:
            if transmissores:
                global cont_transmitido
                cont_transmitido += 1
                print("Transmitiu:", transmissores[0].id)


def main():
    n_dispositivos = 24
    tempo_simulacao = 100000

    dispositivos = [Dispositivo(id) for id in range(n_dispositivos)]
    start = time.time()
    simulador(dispositivos, tempo_simulacao)
    end = time.time()
    elapsed = round(end - start, 3)

    cont_total = cont_transmitido + cont_colisoes + cont_descartes
    print(f"Simulação CSMA/CD com {n_dispositivos} dispositivos por {tempo_simulacao} unidades de tempo.")
    print(f"Total de quadros: \t\t\t {cont_total} (100%)")
    print(f"Total de consumo da banda: \t {round((cont_total / tempo_simulacao) * 100, 2)}%")
    print(f"Transmissões ocorridas: \t {cont_transmitido} ({round((cont_transmitido / cont_total) * 100, 2)}%)")
    print(f"Colisões ocorridas: \t\t {cont_colisoes} ({round((cont_colisoes / cont_total) * 100, 2)}%)")
    print(f"Descartes ocorridos: \t\t {cont_descartes} ({round((cont_descartes / cont_total) * 100, 2)}%)")
    print(f"Tempo decorrido: \t\t\t {elapsed}s")
    print(f"Quadros por segundo: \t\t {round(cont_transmitido / elapsed, 2)}")


main()

# TODO: Ao detectar rede ociosa, retomar algum pacote que está em backoff para melhorar uso da banda
# TODO: Ao detectar colisão, escolher um quadro para transmitir e outro para entrar em backoff, para diminuir o número de colisões
