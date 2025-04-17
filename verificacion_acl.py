acl = int(input("Ingrese el número de ACL IPv4: "))

if 1 <= acl <= 99 or 1300 <= acl <= 1999:
    print("\nTipo de ACL: Estándar")
    print("\nEjemplo - Standard IP access list DUOC-LIST-LOCAL")
    print("    10 permit 192.168.1.10")
    print("    20 permit 192.168.200.0")
    print("    !")
elif 100 <= acl <= 199 or 2000 <= acl <= 2699:
    print("\nTipo de ACL: Extendida")
    print("\nEjemplo - Extended IP access list INTERNET")
    print("    30 permit ip any host 8.8.8.8")
    print("    40 permit ip 192.168.1.0 0.0.0.255 any log")
else:
    print("\nEl número ingresado NO corresponde a una ACL válida.")
