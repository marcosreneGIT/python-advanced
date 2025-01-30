"""
CONSTANTE = "variáveis" que não vão mudar
muitas condições no mesmo if = ruim
.............. Contagem de complexidade = ruim
"""
velocidade = 100 # velocidade atual do carro
local_carro =  99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if (LOCAL_1 - RADAR_1) <= local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
        print('Você receberá uma multa!')


carro_multado = (LOCAL_1 - RADAR_1) <= local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1

if carro_multado:
        print('Você receberá uma multa!')