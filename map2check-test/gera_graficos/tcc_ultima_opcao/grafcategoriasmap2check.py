import matplotlib.pyplot as plt

# Dados
towers = ['c/ReachSafety-Arrays', 'c/ReachSafety-BitVectors', 'c/ReachSafety-Loops']
total = [9, 7, 9]  # Total de testes
achieved = [7, 5, 5]  # Testes alcançados pelo Map2Check

# Calcular o número de testes não alcançados (unknown)
not_achieved = [total[i] - achieved[i] for i in range(len(total))]

# Configuração da largura das barras
bar_width = 0.35
index = range(len(towers))

# Criação do gráfico de barras empilhadas
fig, ax = plt.subplots()

# Barras para os testes alcançados e não alcançados
ax.bar(index, achieved, bar_width, label='Alcançados', color='blue')
ax.bar(index, not_achieved, bar_width, bottom=achieved, label='Não Alcançados', color='lightgray')

# Título e rótulos
plt.title('Desempenho do Map2Check em Testes')
plt.xlabel('Execução da ferramenta')
plt.ylabel('Total de Testes')

# Ajustar a posição das legendas
plt.xticks(index, towers, rotation=45, ha='right')

# Adicionar os números inteiros nas barras
for i in range(len(towers)):
    ax.text(i, achieved[i] / 2, str(achieved[i]), ha='center', va='center', color='white')
    ax.text(i, achieved[i] + not_achieved[i] / 2, str(not_achieved[i]), ha='center', va='center')

# Adicionar a legenda
plt.legend()

# Mostrar o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição
plt.show()
