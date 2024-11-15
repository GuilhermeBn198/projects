import matplotlib.pyplot as plt
import numpy as np

# Dados
categories = ['c/ReachSafety-Arrays', 'c/ReachSafety-BitVectors', 'c/ReachSafety-Loops']
esbmc = [2, 0, 5]        # Resultados ESBMC
map2check = [7, 5, 5]     # Resultados Map2Check
klee = [8, 6, 7]          # Resultados KLEE
fusebmc = [9, 7, 9]       # Resultados FuseBMC
max_height = 9            # Altura máxima do gráfico

# Configuração de largura das barras
bar_width = 0.2  # Largura das barras
index = np.arange(len(categories))

# Criação do gráfico de barras sobrepostas
fig, ax = plt.subplots()

# Desenhando as barras sobrepostas
bar_esbmc = ax.bar(index - bar_width*1.5, esbmc, bar_width, label='ESBMC', color='darkblue')
bar_map2check = ax.bar(index - bar_width/2, map2check, bar_width, label='Map2Check', color='blue')
bar_klee = ax.bar(index + bar_width/2, klee, bar_width, label='KLEE', color='darkgreen')
bar_fusebmc = ax.bar(index + bar_width*1.5, fusebmc, bar_width, label='FuseBMC', color='darkcyan')

# Título e rótulos
plt.title('Resultados obtidos das ferramentas, categorias separadas.')
plt.xlabel('Categorias')
plt.ylabel('Total de Testes (até 9)')

# Ajustar a posição das legendas e rótulos do eixo x
plt.xticks(index, categories, rotation=15, ha='right')

# Definir limite máximo do eixo y
ax.set_ylim(0, max_height)

# Adicionar os números inteiros nas barras
def add_bar_labels(bars):
    """Adiciona os valores nas barras."""
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, height - 0.5, f'{height:.0f}',
                    ha='center', va='bottom', color='white')

# Adicionar os valores nas colunas
add_bar_labels(bar_esbmc)
add_bar_labels(bar_map2check)
add_bar_labels(bar_klee)
add_bar_labels(bar_fusebmc)

# Adicionar a legenda fora do gráfico
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Ajustar margens para evitar sobreposição
plt.subplots_adjust(left=0.1, right=0.75, top=0.9, bottom=0.25)

# Mostrar o gráfico
plt.show()
