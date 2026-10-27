class Producto:
    def __init__(self, nombre, precio, cantidad):
        # Validaciones de los atributos al instanciar
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero.")
            
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        
    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        self.precio = float(nuevo_precio)
        
    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero.")
        self.cantidad = int(nueva_cantidad)
        
    def calcular_valor_total(self):
        return self.precio * self.cantidad
        
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
            
    def buscar_producto(self, nombre):
        if not nombre.strip():
            return None
            
        nombre_buscado = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscado:
                return producto
        return None
        
    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)
        
    def listar_productos(self):
        if not self.productos:
            print("- El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu_principal():
    inventario = Inventario()
    
    while True:
        print("\n" + "="*30)
        print("    SISTEMA DE INVENTARIO")
        print("="*30)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Ingrese el nombre del producto: ").strip()
            
            try:
                if not nombre:
                    raise ValueError("El nombre del producto no puede estar vacío.")
                    
                precio_str = input("Ingrese el precio: ").strip()
                cantidad_str = input("Ingrese la cantidad: ").strip()
                
                # Conversión de tipos que puede lanzar ValueError
                precio = float(precio_str)
                cantidad = int(cantidad_str)
                
                # Instanciación (valida negativos automáticamente gracias a la clase)
                nuevo_producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
                print(f"Éxito: Producto '{nombre}' agregado al inventario.")
                
            except ValueError as e:
                # Captura tanto errores de conversión (letras por números) como las validaciones de la clase
                print(f"Error: Entrada inválida. {e}")
                
        elif opcion == '2':
            print("\n--- BUSCAR PRODUCTO ---")
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            
            try:
                if not nombre:
                    raise ValueError("Debe ingresar un nombre para buscar.")
                    
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print("\nProducto encontrado:")
                    print(producto)
                else:
                    # Cumpliendo el requisito: lanzar excepción si no se encuentra
                    raise ValueError(f"No se encontró ningún producto con el nombre '{nombre}'.")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif opcion == '3':
            print("\n--- LISTA DE PRODUCTOS ---")
            inventario.listar_productos()
            
        elif opcion == '4':
            print("\n--- VALOR TOTAL ---")
            total = inventario.calcular_valor_inventario()
            print(f"El valor total del inventario es: ${total:.2f}")
            
        elif opcion == '5':
            print("\nCerrando el sistema... ¡Gracias por utilizar el gestor de inventario!")
            break
            
        else:
            print("Error: Opción no válida. Por favor, elija un número del 1 al 5.")


if __name__ == "__main__":
    menu_principal()
