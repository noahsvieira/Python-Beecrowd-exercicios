'''
O Segurança da Porta

Imagine que você é o segurança da porta de uma festa exclusiva. 
Um convidado tenta entrar dizendo um número de crachá, mas se o número não estiver na sua lista VIP, 
 sistema não pode quebrar nem chorar: 
 ele deve acionar o alarme silencioso e dizer que a entrada foi negada com segurança, 
 sem crashar o computador.

Simule a tentativa de buscar um usuário que não existe no dicionário.

Use o escudo protetor (try / except) para capturar o erro e imprimir: 
Alerta de Segurança: Usuário não encontrado!

'''

lista_vip = {"mariana" : "admin" , "pedro" : "usuario"}

usuario_tentando_entrar = "joao_intruso"

try:
    cargo = lista_vip[usuario_tentando_entrar]
    print(f"Bem vindo, {usuario_tentando_entrar}!")

except KeyError:
    print("Alerta de Segurança: Usuário não encontrado!")
