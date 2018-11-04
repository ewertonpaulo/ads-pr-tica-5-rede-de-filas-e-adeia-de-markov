import iterator as it
from grafo import grafo, demand
import sys

entry = {'entry': 1.0}

print('First')
it.first(entry)
sys.stdout.flush()
print('Second')
req = it.second(entry,5)
sys.stdout.flush()
print('Third')
util_cpu = it.third(demand['cpu'], req)
util_disc = it.third(demand['disc'], req)
sys.stdout.flush()
print('Fourth')
res_cpu = it.fourth(req, demand['cpu'], util_cpu)
res_disc = it.fourth(req, demand['disc'], util_disc)
sys.stdout.flush()
print('Fifth')
it.fifth(res_cpu, res_disc)
