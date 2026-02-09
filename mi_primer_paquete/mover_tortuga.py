import rclpy
from rclpy.node import Node

# IMPORTANTE: Importamos el tipo de mensaje para moverse (Twist)
# Es como importar una hoja de papel pautado específica para escribir música
from geometry_msgs.msg import Twist

class MoverTortuga(Node):
    def __init__(self):
        super().__init__('nodo_mover_tortuga')
        
        # 1. EL PUBLICADOR (El Mando a Distancia)
        # - Tipo de mensaje: Twist (Velocidad)
        # - Topic: '/turtle1/cmd_vel' (El canal que escucha la tortuga)
        # - Cola: 10 (Si enviamos muy rápido, guarda hasta 10 mensajes)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # 2. EL TEMPORIZADOR (El dedo pulsando el botón)
        # Cada 0.5 segundos, enviará una orden de movimiento
        self.timer = self.create_timer(0.5, self.timer_callback)
        
        self.get_logger().info('¡Nodo arrancado! Preparando para mover la tortuga...')

    def timer_callback(self):
        # 3. CREAMOS EL MENSAJE (Rellenamos el sobre)
        msg = Twist()
        
        # Configurar la velocidad
        msg.linear.x = 2.0   # Moverse hacia adelante a 2 m/s
        msg.angular.z = 1.0  # Girar sobre sí misma a 1 rad/s (giro izquierda)
        
        # 4. PUBLICAMOS (Enviamos el sobre)
        self.publisher_.publish(msg)
        
        self.get_logger().info('Enviando orden: Avanza y Gira 🔄')

def main(args=None):
    rclpy.init(args=args)
    node = MoverTortuga()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()