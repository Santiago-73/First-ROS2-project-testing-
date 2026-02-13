import sys
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn  # <--- IMPORTANTE: El tipo de servicio

class ClienteTortuga(Node):

    def __init__(self):
        super().__init__('nodo_cliente_tortuga')
        
        # 1. CREAR EL CLIENTE
        # Definimos: Tipo de mensaje (Spawn) y nombre del servicio (/spawn)
        self.cliente = self.create_client(Spawn, '/spawn')
        
        # 2. ESPERAR AL SERVICIO (La Pizzería)
        # Bucle que comprueba cada segundo si el servicio está activo
        while not self.cliente.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('El servicio /spawn no está disponible, esperando... 🕒')
        
        # 3. PREPARAR LA PETICIÓN (El pedido)
        self.req = Spawn.Request()

    def enviar_peticion(self):
        # Rellenamos los datos del formulario
        self.req.x = 5.5
        self.req.y = 5.5
        self.req.theta = 1.57 # 90 grados
        self.req.name = 'Leonardo' # 🐢🐢

        # 4. ENVIAR Y RECIBIR EL "TICKET" (Future)
        # call_async significa: "Envía esto y no te bloquees, dame un resguardo"
        self.future = self.cliente.call_async(self.req)
        
        # Devolvemos el ticket para que el 'main' sepa qué vigilar
        return self.future

def main(args=None):
    rclpy.init(args=args)
    
    # Creamos el nodo
    nodo_cliente = ClienteTortuga()
    
    # Lanzamos la petición
    futuro = nodo_cliente.enviar_peticion()
    
    # 5. ESPERAR HASTA QUE SE COMPLETE (El momento clave)
    # Aquí el programa se queda pausado hasta que el servicio responde
    rclpy.spin_until_future_complete(nodo_cliente, futuro)
    
    # 6. LEER EL RESULTADO
    try:
        respuesta = futuro.result()
        nodo_cliente.get_logger().info(f'¡Éxito! Nueva tortuga creada: {respuesta.name} 🐢')
    except Exception as e:
        nodo_cliente.get_logger().error(f'La llamada falló: {e}')

    nodo_cliente.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()