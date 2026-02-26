nome = input('digite seu primeiro nome ').upper().strip()
sobrenome = input('digite seu Sobrenome ').upper().strip()
dia_nascimento = input('digite seu dia de nascimento ' ) 
Mês_nascimento = input('digite seu mês de nascimento ' )
ano_nascimento = input('digite seu Ano de nascimento ' )
universidade = input('digite Sua Universidade ')

e_mail = nome.lower() + '.' + sobrenome.lower() + '@' + universidade + '.br'
senha = 'a' + str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))

print('seu email é ', e_mail)
print('sua senha é ', senha) 
print(' seu email é: {} e sua senha é: {}' .format(e_mail,senha))
