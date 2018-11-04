grafo = {
    'entry':{'home': 1.0},
    'home': {'add': 0.2, 'search': 0.7, 'exit': 0.1}, 
    'search':{'search': 0.6, 'add': 0.3, 'exit': 0.1},
    'add': {'pay': 0.4, 'exit': 0.6},
    'pay': {'exit': 1.0}
}

demand = {
    'cpu':{'home':0.010,'search':0.015,'add':0.010,'pay':0.020},
    'disc':{'home':0.015,'search':0.025,'add':0.015,'pay':0.010}
}