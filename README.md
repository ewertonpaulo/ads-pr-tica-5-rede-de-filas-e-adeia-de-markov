# ads-prática-5-rede-de-filas-e-adeia-de-markov
Nesta atividade é apresentado um problema de rede de filas, envolvendo a análise de desempenho de um site de comércio eletrônico.

## Questão 1:
As fórmulas utilizadas foram as seguintes:

Ventry = 1

Vhome = Ventry x Peh

Vsearch = Vhome x Phs / 1 - Pss

Vadd = Vhome x Pha + Vsearch x Psa

Vpay = Vadd x Pap

Código para gerar os resultados:
```py
def visits(grafo, entry, key):
    for vertex in grafo[key]:
        if vertex != 'exit' and vertex != key:    
            try:
                entry[vertex] += grafo[key][vertex]*entry[key] 
                visits(grafo,entry,vertex)
            except KeyError:
                entry[vertex] = grafo[key][vertex]*entry[key] 
                visits(grafo,entry,vertex)
        if vertex == key:
            entry[vertex] = entry[vertex]/(1-grafo[vertex][vertex])
    return entry
```
![Image of Yaktocat](https://github.com/ewertonpaulo/ads-pr-tica-5-rede-de-filas-e-adeia-de-markov/blob/master/img/1.png)

## Questão 2:
A forma utilizada para os resultados da segunda questão foi:

Taxa de chegada = Tempo Total * Tempo médio de Visita

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-pr-tica-5-rede-de-filas-e-adeia-de-markov/blob/master/img/2.png)

Código para gerar os resultados:
```py
def second(entry,taxa):
    dic = {}
    for vertex in entry:
        entry[vertex] = entry[vertex]*taxa
        dic[vertex] = entry[vertex]

    table(dic)
    return entry
```
O valor da taxa foi 5 como dado na questão.

## Questão 3:
A forma utilizada para os resultados da terceira questão foi:

Ultilização = Taxa de chegada * Demanda de serviço

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-pr-tica-5-rede-de-filas-e-adeia-de-markov/blob/master/img/3.png)

Código para gerar os resultados:
```py
def third(demand,req):
    u = {}
    total = 0
    for i in demand:
        total += demand[i]*req[i]
        u[i] = demand[i]*req[i]
    u['total']=total
    table(u)
    return u
```

## Questão 4:
Para calcular o tempo de residencia na questão 4, os valores das demandas que foram resultados da questão 3 foram multiplicados pela taxa de utilização total dos dois
componentes, cpu e disco.

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-pr-tica-5-rede-de-filas-e-adeia-de-markov/blob/master/img/4.png)

Código para gerar os resultados:
```py
def fourth(req, demand, util):
    dic  = {}
    for i in req:
        try:
            dic[i] = demand[i]/(1-util['total'])
        except:
            pass
    table(dic)
    return dic
```

## Questão 5:
Para calcular o tempo de resposta, foi utilizado o tempo de residencia dos dois componentes que foram somados.

![Image of Yaktocat](https://github.com/ewertonpaulo/ads-pr-tica-5-rede-de-filas-e-adeia-de-markov/blob/master/img/5.png)

Código para gerar os resultados:
```py
def fifth(res_cpu, res_disc):
    resp_time = {}
    for i in res_cpu:
        resp_time[i] = res_cpu[i]+res_disc[i]
    table(resp_time)
    return resp_time
```
