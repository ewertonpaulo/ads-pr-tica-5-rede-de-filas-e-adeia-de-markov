
from grafo import grafo, demand
import texttable as tt

tab = tt.Texttable()
           
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

def table(dic):
    headings = []
    keys = []
    for key in dic:
        headings.append(key)
        keys.append(dic[key])
    tab = tt.Texttable()
    tab.header(headings)
    tab.add_row(keys)
    s = tab.draw()
    print (s)

def first(entry):
    entry = visits(grafo,entry,'entry')
    table(entry)

def second(entry,taxa):
    dic = {}
    for vertex in entry:
        entry[vertex] = entry[vertex]*taxa
        dic[vertex] = entry[vertex]

    table(dic)
    return entry

def third(demand,req):
    u = {}
    total = 0
    for i in demand:
        total += demand[i]*req[i]
        u[i] = demand[i]*req[i]
    u['total']=total
    table(u)
    return u

def fourth(req, demand, util):
    dic  = {}
    for i in req:
        try:
            dic[i] = demand[i]/(1-util['total'])
        except:
            pass
    table(dic)
    return dic

def fifth(res_cpu, res_disc):
    resp_time = {}
    for i in res_cpu:
        resp_time[i] = res_cpu[i]+res_disc[i]
    table(resp_time)
    return resp_time

entry = {'entry': 1.0}

first(entry)
req = second(entry,5)
util_cpu = third(demand['cpu'], req)
util_disc = third(demand['disc'], req)
res_cpu = fourth(req, demand['cpu'], util_cpu)
res_disc = fourth(req, demand['disc'], util_disc)
fifth(res_cpu, res_disc)


