'''
Exercício 5: O Crachá Falsificado (Função Assíncrona e Verificação)

Em um sistema de FastAPI, as funções que conversam com o banco de dados ou verificam a internet 
precisam ser assíncronas (async def) para não travar o servidor. 
Imagine que você precisa criar uma função assíncrona que recebe um crachá (token). 
Se o crachá for exatamente a palavra "CRIS_VIP", ela libera a entrada. 
Se for qualquer outra coisa, ela rejeita.

'''

import asyncio

async def verificar_cracha(token_recebido: str):
    await asyncio.sleep(0.5)

    if token_recebido == "CRIS_VIP":
        return "Acesso Autorizado : Bem-vindo à festa!"

    else:
        return "Acesso Negado: Crachá falso!"

async def main():
    resultado = await verificar_cracha("TOKEN_ERRADO_123")
    print(resultado)

asyncio.run(main())