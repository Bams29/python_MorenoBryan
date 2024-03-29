import json

class DataHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'ventas': {'clientes': [], 'comerciales': [], 'pedidos': []}}

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)

    def create_cliente(self, cliente):
        self.data['ventas']['clientes'].append(cliente)
        self.save_data()

    def read_clientes(self):
        return self.data['ventas']['clientes']

    def update_cliente(self, cliente_id, new_data):
        for cliente in self.data['ventas']['clientes']:
            if cliente['id'] == cliente_id:
                cliente.update(new_data)
                self.save_data()
                return True
        return False

    def delete_cliente(self, cliente_id):
        self.data['ventas']['clientes'] = [cliente for cliente in self.data['ventas']['clientes'] if cliente['id'] != cliente_id]
        self.save_data()

    # Repetir las mismas operaciones CRUD para comerciales y pedidos


# Ejemplo de uso:
if __name__ == "__main__":
    handler = DataHandler('data.json')

    # Crear un nuevo cliente
    idd = int(input("porfa ingrese un id: "))
    nomb = input("ingrese un nombre: ")
    apell = input("ingrese un apellido: ")
    ciud = input("ingresa una city: ")
    catt= int(input("ingrese una categoria: "))
    nuevo_cliente = {"id": idd, "nombre": nomb, "apellido1": apell, "ciudad": ciud, "categoría": catt}
    handler.create_cliente(nuevo_cliente)

    # Leer todos los clientes
    clientes = handler.read_clientes()
    print("Clientes:")
    for cliente in clientes:
        print(cliente)

    # Actualizar un cliente existente
    cliente_id = 4
    newcyry = input("ingrese la ciudad a donde se cambio: ")
    datos_actualizados = {"ciudad": newcyry}
    if handler.update_cliente(cliente_id, datos_actualizados):
        print(f"Cliente con ID {cliente_id} actualizado correctamente.")
    else:
        print(f"No se encontró ningún cliente con ID {cliente_id}.")

    # Eliminar un cliente
    n = int(input())
    cliente_id_a_eliminar = n
    handler.delete_cliente(cliente_id_a_eliminar )
    print(f"Cliente con ID {cliente_id_a_eliminar} eliminado correctamente.")
