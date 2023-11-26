def area(arg1,arg2, forma):
  if forma == 'retangulo':
      area = arg1 * arg2
  else:
      area = arg1 * arg2 / 2
  print('O', forma, 'tem', int(area), 'de area')