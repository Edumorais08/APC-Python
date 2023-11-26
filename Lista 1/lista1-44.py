def ritmoMedio(h, m, s, d):
   tempo_d = ((h*3600)+(m*60)+s)/d
   min = int(tempo_d // 60)
   seg = int(tempo_d % 60)
   print('{:02d}:{:02d} min/km'.format(int(min), int(seg)))