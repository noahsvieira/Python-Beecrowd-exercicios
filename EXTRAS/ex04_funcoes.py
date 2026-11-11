'''
A Fábrica do Crachá VIP

Imagine que você tem uma maquininha mágica na entrada do clubinho. 
Ela precisa receber dois ingredientes secretos: o nome do membro e o cargo dele.
A maquininha mistura os dois ingredientes e cospe um crachá digital bonitinho 
com a mensagem oficial para colar na blusa.
'''

def gerar_cracha_vip (nome_pessoa, cargo_pessoa):
    cracha_pronto = (
        f"---CRACHÁ DIGITAL ---\nMembro: {nome_pessoa}  \nCargo : {cargo_pessoa}"
    )

    return cracha_pronto

meu_cracha = gerador = gerar_cracha_vip ("Lucas" , "admin")

print(meu_cracha)