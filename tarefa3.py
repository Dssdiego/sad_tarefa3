import pandas as pd
import numpy as np

# Calcula a entropia
def entropia(atributo):
    ent = 0

    # Busca os atributos (unicos, sem repetir)
    atribs, cont = np.unique(atributo, return_counts=True)
    
    for i in range(len(atribs)):
        prob = cont[i]/np.sum(cont)
        ent -= prob*np.log2(prob)
        
    # Arredonda o resultado para 4 casas decimais
    return round(ent,4)

# Calcula o ganho de determinado atributo
def ganho(atributo):
    # Calcula a entropia da coluna resultado
    ent = entropia(df[colunaResultado])
    ganho_medio = 0

    atribs, count = np.unique(df[atributo], return_counts=True)
    for i in range(len(atribs)):
        split_data = df.where(df[atributo] == atribs[i]).dropna()[colunaResultado]
        ganho_medio += (count[i]/np.sum(count)) * entropia(split_data)
    
    ganho_final = ent - ganho_medio
    
    # Arredonda o resultado para 4 casas decimais
    return round(ganho_final,4)


if __name__ == "__main__":
    # Le os dados de treino (arquivo .csv)
    df = pd.read_csv('treino.csv')

    # Busca lista de colunas
    colunas = list(df.columns)    

    # Coluna de resultado eh sempre a ultima
    colunaResultado = colunas[-1] 

    # Colunas de atributos sao todas exceto a ultima (de resultado)
    atributos = colunas[:-1]

    # Mostra os atributos disponiveis
    print('Atributos Disponiveis:')
    print(atributos)

    # Pede ao usuario o nome da coluna
    atributo = input('\nEscolha o atributo a ser calculado:\n')
    print('\nEntropia: ' + str(entropia(df[colunaResultado])))
    print('Ganho [' + atributo + ']: ' + str(ganho(atributo)))
