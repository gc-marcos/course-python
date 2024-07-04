medida = float(input('Digite a quantidade em metros: '))
cm = medida*100
mm = medida*100
print('A conversão de {} em CM é {}cm e em MM é{}mm'.format(medida, cm, mm))
print('A quantidade de {} em CM é {:.0f} '.format(medida, medida*100))
print('A quantidade de {} em MM é {:.0f} '.format(medida, medida*1000))
