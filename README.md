# Estudos Python 🐍🎉💙

<a href="https://marketplace.visualstudio.com/items?itemName=EliazBobadilla.python-ultiextension-pack" title="Python UltiExtension Pack" target="__blank">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

</a>

<details>
<summary>🌐 <strong>.venv</strong> | Ambiente Virtual</summary></br>
  O ambiente virtual possibilita executar diferentes tipos de projetos com diferentes versões de bibliotecas, sem o risco de conflitar com a maquina local, e todas as bibilotecas do projeto atual estarão sendo instalados dentro desse ambiente.
  
  <br/>


```bash
# ___________________________
# 🚀 cria o ambiente virtual
  python3 -m venv .venv
# ___________________________

# ___________________________
# 🔛 ativa o ambiente virtual
  source .venv/bin/activate
# ___________________________

# ___________________________
# 🧰 instalar as dependências no ambiente virtual
# 🔎 dev-requirements.txt contém todas as dependências utilizadas no projeto
python3 -m pip install -r dev-requirements.txt
# ___________________________

# ___________________________
# 📴 desativa o ambiente virtual
deactivate
# ___________________________
```

</details>

<details>
<summary><strong>🧪 Testes</strong></summary><br />

[📖 Documentação](https://docs.pytest.org/en/6.2.x/getting-started.html)

Para executar os testes certifique-se de que você está com o ambiente virtual ativado
<strong>Executar os testes</strong>
```bash
pthon3 -m pytest
```
O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queiraexplicitamente uma saída completa, o comando é:
```bash
python3 -m pytest -s -vv
```
Caso precise executar apenas um arquivo de testes basta executar o comando:
```bash
python3 -m pytest tests/nomedoarquivo.py
```
Caso precise executar apenas uma função de testes basta executar o comando:
```bash
python3 -m pytest -k nome_da_func_de_tests
```
Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`
```bash
python3 -m pytest -x tests/nomedoarquivo.py
```
Caso queria executar um teste especifico de um arquivo basta executar o comando:
```bash
python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
```
</details>

# Estrutura de Dados



# Padrões de Projetos


## Iterator
É o mecanismo usado para "andar", elemento por elemento, por uma coleção de dados. É uma forma abstrata e genérica de tratar o avanço entre os elementos dessa coleção. Esse avanço pode se dar de várias formas, inclusive ao contrário.

## Adapter
Adapter é um padrão de projeto estrutural, que permite que objetos incompatíveis colaborem. O Adapter atua como um wrapper entre dois objetos. Ele captura chamadas para um objeto e as transforma em formato e interface reconhecíveis pelo segundo objeto.

## Strategy

Strategy é um padrão de design comportamental que permite definir uma família de algoritmos, colocar cada um deles em uma classe separada e tornar seus objetos intercambiáveis.
