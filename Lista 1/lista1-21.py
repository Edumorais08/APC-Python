#, sep='' para tirar os espaços ou print(str(DD) + '-' + str(MM) + '-' + str(AA))
DD,MM,AA = input().split('/')

print(DD,'-',MM,'-',AA, sep='')
print(MM,'-',DD,'-',AA, sep='')
print(AA,'/',MM,'/',DD, sep='')