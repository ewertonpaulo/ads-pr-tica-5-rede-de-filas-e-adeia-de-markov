from grafo import grafo
           
def visits(grafo, entry, key):
    for vertex in grafo[key]:
        if vertex != 'exit' and vertex != key:    
            try:
                entry[vertex] = grafo[key][vertex]*entry[key] 
                visits(grafo, entry, vertex)
            except KeyError:
                entry[vertex] = grafo[key][vertex]*entry[key] 
                visits(grafo, entry, vertex)
        if vertex == key:
            entry[vertex] = entry[vertex]/(1-grafo[vertex][vertex])

entry = {'entry': 1.0}

def show(entry):
    visits(grafo, entry, 'entry')
    for key in entry:
        print(key+' %s' %entry[key])

show(entry)
