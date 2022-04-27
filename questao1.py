import pandas as pd
import numpy as np

def main():
    dados = pd.read_table('questao1.txt')
    corrente_diodo = dados['I(D1)']
    tensao_diodo = dados['v1']
    #Fatiar o vetores de forma a pegar apenas o ultimo oitavo com a função array_split.
    #Detalhe: Em python os índices dos vetores começam em zero. Por isso, o índice 7 foi escolhido para pegar o ultimo oitavo.
    tensao_diodo_oitavo = np.array_split(tensao_diodo,8)[7]
    corrente_diodo_oitavo = np.array_split(corrente_diodo,8)[7]


if __name__ == "__main__":
    main()