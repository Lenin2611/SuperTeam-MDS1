from backend.cliente import listarClientes, consultarCliente

clientes = listarClientes()
cliente = consultarCliente("1101")

print(clientes)
print(cliente)
