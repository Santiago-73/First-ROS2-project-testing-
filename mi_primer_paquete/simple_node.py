import rclpy
from rclpy.node import Node

class MiNodoSaludador(Node):
    def __init__(self):
        # 1. Llamamos al constructor del padre (Node) y le damos nombre al nodo
        super().__init__('nodo_saludador')
        
        # 2. Imprimimos un mensaje inicial
        self.get_logger().info('¡Hola mundo! El nodo ha arrancado correctamente.')
        
        # 3. Creamos un temporizador (Timer)
        # Cada 1.0 segundos, ROS ejecutará la función self.timer_callback
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Esta función es la que se repite
        self.get_logger().info('Sigo vivo... (mensaje desde el timer)')

def main(args=None):
    # Inicializa la comunicación con ROS
    rclpy.init(args=args)
    
    # Crea el objeto (instancia la clase)
    nodo = MiNodoSaludador()
    
    # Mantiene el programa despierto escuchando eventos (timers, topics, etc.)
    rclpy.spin(nodo)
    
    # Cierra limpiamente
    rclpy.shutdown()

if __name__ == '__main__':
    main()