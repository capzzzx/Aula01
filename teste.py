usuario = input('qual o seu nome? ')
print('ola ',usuario,' seja bem vindo')
senha = input('coloque sua senha' )
print(senha)
dominio = input('digite seu email ')
print('seu email é:',dominio,)
email = (usuario + '@' + dominio)

print('bem vindo' ,usuario, 'seu email é', usuario + "@" + dominio)

palavra = "jaca"
#dolocar a string como toda maiuscula
print('Colocando o texto em maiuscula: ',palavra.upper())

PALAVRA = "JACA"
#colocar a string como toda minuscula
print("Colocando o texto em minuscula: ",PALAVRA.lower())

#contar caracter da string
palavra_contar = 'banana'
print('contar a letra b', palavra_contar.count('b') )
print('contar a letra a', palavra_contar.count('a') )
print('contar a letra n', palavra_contar.count('n') )

#exercicio
print('contar a letra a', email.count('a') )
print('contar a letra e', email.count('e') )
print('contar a letra i', email.count('i') )
print('contar a letra o', email.count('o') )
print('contar a letra u', email.count('u') )

print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e' str(e_c) + 'i' str(i_c) + 'o' str(o_c) + u str(u_c)
print(nova_senha) 
