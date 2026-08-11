from core.mikrotik import MikroTik

mk = MikroTik()

pppoe = mk.pppoe()

mk.close()

for item in pppoe:
    print("-" * 60)
    for chave, valor in item.items():
        print(f"{chave}: {valor}")