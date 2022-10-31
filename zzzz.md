inicio de projeto

Assert é uma estrutura do Python para depurar o código, ou seja, essa estrutura vai te permitir verificar algumas condições para facilitar a correção de erros dentro do seu código.

abrir arquivo data/inventory.csv em exel para gerar um atabela para poder pegar valores para o teste

Dica: A reimplementação do **repr** não faz o objeto retornar exatamente uma string, fazer um cast para string, pode te ajudar.

    Python __str__()

Este método retorna a representação de string do objeto. Este método é chamado quando print()ou str()função é invocada em um objeto. Este método deve retornar o objeto String. Se não implementarmos a função **str**() para uma classe, então a implementação do objeto embutido é usada que realmente chama a função **repr**().

    Python __repr__()

A função Python **repr**() retorna a representação do objeto em formato de string. Este método é chamado quando repr()a função é invocada no objeto. Se possível, a string retornada deve ser uma expressão Python válida que possa ser usada para reconstruir o objeto novamente.

Você deve sempre usar as funções str() e repr(), que chamarão as funções **str** e **repr** subjacentes. Não é uma boa ideia usar essas funções diretamente.

cast para string - Em Python, um inteiro pode ser convertido em uma string usando a função str() integrada. A função str() recebe qualquer tipo de dados python e o converte em uma string. Mas o uso do str() não é a única maneira de fazer isso. Este tipo de conversão também pode ser feito usando a palavra-chave “%s” , a função .format ou a função f-string .

https://discuss.python.org/t/what-is-this-command/9045

3 - Gerar a versão simplificada do relatório
inventory_report/reports/simple_report.py

    datetime - https://docs.python.org/3/library/datetime.html
    apend - https://www.w3schools.com/python/ref_list_append.asp
    most_common - https://docs.python.org/3/library/collections.html

4 - Gerar a versão completa do relatório
inventory_report/reports/complete_report.py

    O super() serve para - em uma relação de herança entre uma classe Base e outra Derivada - permitir que a classe Derivada se refira explicitamente à classe Base.

self - https://ealexbarros.medium.com/como-utilizar-o-self-em-python-c03c43ec29a2
