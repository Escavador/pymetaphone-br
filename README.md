# Pymetaphone-br
[![PyPI version](https://badge.fury.io/py/pymetaphone-br.svg)](https://badge.fury.io/py/pymetaphone-br)
Algoritmo de Metaphone ( alternativa ao Soundex) para a língua portuguesa em Python

### Créditos ###

Esse projeto é uma reescrita em Python do projeto de Carlos Costa Jordão. [metaphone-ptbr](https://github.com/carlosjordao/metaphone-ptbr)


### Como Usar? ###

```
from pymetaphone_br import convert_to_metaphone
print(convert_to_metaphone('Casas Bahia'))
```

### Como funciona? ###

Ele gera um token uníco para palavras que tenham a mesma pronúncia.

Por exemplo `Casas Bahia` e `Cazas Baia` geram o mesmo token KZSB.

É útil para pesquisar nomes e frases por similaridade ou quando tem a pronuncia incorreta.


## Instalação

```
pip install pymetaphone-br
```

Funções diversas para tratar dados juridicos
