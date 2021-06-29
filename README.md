# calculadora-salario-liquido
Uma calculadora pra descobrir um salário liquido brasileiro

## Execução
```
docker build -t calculadora-salario-liquido .
docker run -v $PWD:/code calculadora-salario-liquido main.py <salario>
```
