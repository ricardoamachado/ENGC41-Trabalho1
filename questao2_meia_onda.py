import pandas as pd
import numpy as np

def main():
    dados = pd.read_csv('questao2_meia_onda.txt',sep='\t')
    tensao_diodo = dados['V(vin)-V(vout)']
    tensao_saida = dados['V(vout)']
    
    print(f"Para a simulação, temos vdmax = {tensao_diodo.max()} V, vdmin = {tensao_diodo.min()} V, vout = {tensao_saida.max()} V")

if __name__ == '__main__':
    main()
