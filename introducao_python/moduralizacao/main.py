import minha_libs # Importa tudo do arquivo minha_lib mas tem que usar o minha_lib. (minha_lib.x)
from . import minha_libs # Importa tudo do arquivo minha_lib mas tem que usar o minha_lib. (minha_lib.x)
import .math # O ponto serve pra referenciar a nossa própria pasta e não dar conflito com as bibliotecas do python
from minha_libs import x,y # Importa diretamente e SOMENTE o x e o y do minha_lib
from minha_libs import * # Importa diretamente tudo do arquivo minha_lib 
from minha_libs import x as x_importado # Importa diretamente o x mas com outro nome, x_importado 
from minhas_funcoes.minha_lib import soma_numero # Importa diretamente a função, e agora o arquivo está dentro de outra pasta DENTRO dessa que estou
from ..minhas_balls.minha_lib import soma_numero # Importa diretamente a função, e agora o arquivo está dentro de outra pasta FORA dessa que estou


print(minha_libs.x)
print(x)
print(y)
print(soma_numero(1,2))