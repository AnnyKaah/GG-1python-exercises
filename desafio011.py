larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('-'*12)
área = larg*alt
print('Sua parede tem a dimensão de {}mx{}m e sua área é de {}m².'.format(larg,alt,área))
tinta = área/2
print('Para pintar sua parede você irá precisar de {}l de tinta.'.format(tinta))
print('-'*12)