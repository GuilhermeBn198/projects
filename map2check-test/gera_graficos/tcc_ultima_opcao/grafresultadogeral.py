import matplotlib.pyplot as plt

# Dados
tools = ['ESBMC', 'Map2Check', 'KLEE', 'FuseBMC']
quantities = [7, 15, 20, 25]  # Quantidade alcançada por cada ferramenta
max_height = 25  # Altura máxima do gráfico

# Calcular o número de testes não alcançados (unknown)
not_achieved = [max_height - quantity for quantity in quantities]

# Configuração da largura das barras
bar_width = 0.35
index = range(len(tools))

# Criação do gráfico de barras empilhadas
fig, ax = plt.subplots()

# Barras para as quantidades alcançadas e não alcançadas
ax.bar(index, quantities, bar_width, label='Alcançados', color='blue')
ax.bar(index, not_achieved, bar_width, bottom=quantities, label='Não Alcançados', color='lightgray')

# Título e rótulos
plt.title('Resultados obtidos das ferramentas, categorias combinadas.')
plt.xlabel('Ferramentas')
plt.ylabel('Total de Testes (até 25)')

# Ajustar a posição das legendas
plt.xticks(index, tools, rotation=45, ha='right')

# Adicionar os números inteiros nas barras
for i in range(len(tools)):
    ax.text(i, quantities[i] / 2, str(quantities[i]), ha='center', va='center', color='white')

# Definir limite máximo do eixo y
ax.set_ylim(0, max_height)

# Adicionar a legenda
plt.legend()

# Mostrar o gráfico
plt.tight_layout()  # Ajustar o layout para evitar sobreposição
plt.show()
