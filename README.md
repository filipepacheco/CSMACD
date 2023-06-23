# CSMACD
Desenvolvimento dos conceitos adquiridos na disciplina de Redes de Computadores: Internetworking, Roteamento e Transmissão, tais como controle de acesso ao meio da camada dois do modelo OSI

Desenvolver os conceitos de controle de acesso ao meio utilizando a técnica CSMA/CD, isto é, Carrier Sense Multiple Access with Colision Detection. O trabalho consiste em desenvolver uma simulação para o controle de acesso ao meio utilizado em redes IEEE 802.3. A implementação deve possuir no mínimo dois transmissores que utilizam a tecnologia citada. Cada transmissor antes de enviar um quadro deverá verificar (sensing), por um determinado intervalo de tempo, se o meio de transmissão está ocupado, ou ocorreu colisões.
Caso o meio de transmissão estiver ocupado, deve-se implementar o algoritmo de backoff, isto é, esperar um tempo exponencial truncado
