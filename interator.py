
from grafo import grafo
import texttable as tt

tab = tt.Texttable()
           
def visits(grafo, entry, key):
    temp = entry
    for vertex in grafo[key]:
        if vertex != 'exit' and vertex != key:    
            try:
                temp[vertex] = grafo[key][vertex]*temp[key] 
                visits(grafo, entry, vertex)
            except KeyError:
                temp[vertex] = grafo[key][vertex]*temp[key] 
                visits(grafo, entry, vertex)
        if vertex == key:
            temp[vertex] = temp[vertex]/(1-grafo[vertex][vertex])
    return temp

entry = {'entry': 1.0}

def table(headings,keys):
    tab = tt.Texttable()
    tab.header(headings)
    tab.add_row(keys)
    s = tab.draw()
    print (s)

def show(entry):
    temp = visits(grafo, entry, 'entry')
    headings = []
    keys = []
    for key in temp:
        headings.append(key)
        keys.append(temp[key])

    table(headings, keys)

show(entry)
