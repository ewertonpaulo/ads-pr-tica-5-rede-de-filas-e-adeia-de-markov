
from grafo import grafo
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

def table(headings,keys):
    tab = tt.Texttable()
    tab.header(headings)
    tab.add_row(keys)
    s = tab.draw()
    print (s)

def show(entry):
    entry = visits(grafo,entry,'entry')
    headings = []
    keys = []
    for key in entry:
        headings.append(key)
        keys.append(entry[key])

    table(headings, keys)

def arrive(entry,taxa):
    headings = []
    keys = []
    for vertex in entry:
        entry[vertex] = entry[vertex]*taxa
        headings.append(vertex)
        keys.append(entry[vertex])
    table(headings, keys)
    return entry

entry = {'entry': 1.0}
show(entry)
arrive(entry,5)
