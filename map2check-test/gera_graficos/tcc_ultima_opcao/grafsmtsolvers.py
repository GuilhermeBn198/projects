import matplotlib.pyplot as plt
import numpy as np

# Dados
solvers = ['Z3', 'Yices2', 'Boolector']
falses = [15, 14, 15]  # Quantidade de falses detectados
total_tests = 25  # Total de testes
additional_falses = [9, 9, 9]  # Dados adicionais

# Calcular o número de testes não atingidos (unknown)
unknowns = [total_tests - false for false in falses]
additional_unknowns = [total_tests - additional for additional in additional_falses]

# Configuração da largura das barras
bar_width = 0.35
index = np.arange(len(solvers))

# Criação do gráfico de barras empilhadas
fig, ax = plt.subplots()

# Barras para os falses e unknowns originais
ax.bar(index, unknowns, bar_width, bottom=falses, label='Unknowns', color='darkgray')
ax.bar(index, falses, bar_width, label='Falses(Exec. Symbol.)', color=['blue'])

# Barras para os falses e unknowns adicionais
ax.bar(index + bar_width, additional_falses, bar_width, label='Falses(Fuzzing)', color=['darkblue'])
ax.bar(index + bar_width, additional_unknowns, bar_width, bottom=additional_falses, color='darkgray')

# Título e rótulos
plt.title('Quantidade de testes feitos pelo Map2Check')
plt.xlabel('Solvers + Execução simbólica')
plt.ylabel('Total de Testes')

# Ajustar a posição das legendas
plt.xticks(index + bar_width / 2, solvers)

# Adicionar os números inteiros nas barras
for i in range(len(solvers)):
    ax.text(i, falses[i] / 2, str(falses[i]), ha='center', va='center', color='white')
    ax.text(i + bar_width, additional_falses[i] / 2, str(additional_falses[i]), ha='center', va='center', color='white')

# Adicionar a legenda
plt.legend()

# Mostrar o gráfico
plt.show()
