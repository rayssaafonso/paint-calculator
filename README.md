# Calculadora de Tinta
Uma aplicação simples para calcular quantos litros/latas de tinta serão necessários para pintar as paredes de uma sala tendo em vista as regras de negócio propostas pelo desafio. 
Essa aplicação usou Python 3 com Flask e HTML para o seu desenvolvimento.

**Disponível online em:** http://paint-calculator.herokuapp.com/


## Instalação
Para rodar esse app será necessário ter Python 3 e Pip instalados.

### Clonar o projeto
```bash
$ git clone https://gitlab.com/rayssaafonso/paint-calculator.git
```

### Instalando os requisitos
Dentro do diretório do projeto inserir os seguintes comandos:
```bash
$ pip install -r requirements.txt
```

### Setando as variáveis
```bash
$ export FLASK_APP=app.py
$ export FLASk_ENV=development
```

### Iniciar o servidor
```bash
$ python -m flask run
```

**A aplicação ficará disponível em:** http://127.0.0.1:5000/