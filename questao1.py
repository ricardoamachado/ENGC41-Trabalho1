import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def main():
    dados = pd.read_csv('questao1.txt',sep='\t')
    corrente_diodo = dados['I(D1)']
    tensao_diodo = dados['v1']

    #Ajuste da caracteristica exponencial
    corrente_diodo_ln = np.log(corrente_diodo)
    d, c = np.polynomial.polynomial.polyfit(tensao_diodo,corrente_diodo_ln,1)

    #Determinação dos valores de eta, Is e da corrente do modelo exponencial.
    eta = 1/(0.026*c)
    Is = np.exp(d)
    corrente_diodo_exp = Is*np.exp(tensao_diodo/(0.026*eta))

    #Print dos valores de eta e Is
    print(f"Para o modelo exponencial, temos que eta:{eta:.3f} V e Is:{Is*10**9:.3f} nV.")

    #Plot comparando a caracteristica simulada com o modelo exponencial.
    plt.figure(1)
    plt.plot(tensao_diodo,corrente_diodo_exp,label='Curva Ajustada')
    plt.plot(tensao_diodo,corrente_diodo,label='Curva Simulada')
    plt.xlabel('Tensão(V)')
    plt.ylabel('Corrente(A)')
    plt.legend()
    plt.savefig('output1.png')
    plt.show()

    #Fatiar o vetores de forma a pegar apenas o ultimo oitavo com a função array_split.
    #Detalhe: Em python os índices dos vetores começam em zero. Por isso, o índice 7 foi escolhido para pegar o ultimo oitavo.
    tensao_diodo_oitavo = np.array_split(tensao_diodo,8)[7]
    corrente_diodo_oitavo = np.array_split(corrente_diodo,8)[7]

    #Linearizando a característica no último oitavo. Reta da forma y = ax+b.
    b, a = np.polynomial.polynomial.polyfit(tensao_diodo_oitavo,corrente_diodo_oitavo,1)

    #Determinação dos valores de rd, Vd0 e da corrente linearizada.
    rd = 1/a
    Vd0 = -b/a
    corrente_diodo_linear = tensao_diodo_oitavo/rd - Vd0/rd

    #Print dos valores de rd e Vd0
    print(f"Para o modelo linearizado, temos que rd:{rd:.3f} Ohm e Vd0:{Vd0:.3f} V.")

    #Plot comparando a caracteristica simulada com o modelo linearizado
    plt.figure(2)
    plt.plot(tensao_diodo_oitavo,corrente_diodo_linear,label='Curva Linearizada')
    plt.plot(tensao_diodo,corrente_diodo,label='Curva Simulada')
    plt.xlabel('Tensão(V)')
    plt.ylabel('Corrente(A)')
    plt.legend()
    plt.savefig('output2.png')
    plt.show()

if __name__ == "__main__":
    main()