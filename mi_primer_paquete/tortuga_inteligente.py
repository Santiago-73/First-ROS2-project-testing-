import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose  # <--- IMPORTANTE: El mensaje de "los ojos"

class TortugaInteligente(Node):
    def __init__(self):
        super().__init__('nodo_tortuga_inteligente')
        
        # 1. PUBLICADOR (Boca): Para enviar órdenes de movimiento
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # 2. SUSCRIPTOR (Oídos/Ojos): Para saber dónde estamos
        # - Tipo de mensaje: Pose
        # - Topic: /turtle1/pose
        # - Función a llamar: self.pose_callback
        self.subscription = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.pose_callback, 
            10
        )
        self.get_logger().info('¡Tortuga Inteligente activada! 🐢🧠')

    def pose_callback(self, msg):
        # Esta función se ejecuta AUTOMÁTICAMENTE cada vez que la tortuga se mueve
        # 'msg' contiene la x, y, theta, etc.

        cmd = Twist()
        
        # LOGICA DEL CEREBRO:
        # La pared derecha está en x = 11.0 aprox.
        # Vamos a decir: "Si x es mayor que 9.0, ¡FRENA!"
        
        if msg.x > 9.0:
            cmd.linear.x = 0.0
            cmd.angular.z = 1.0  # Gira para evitar el choque
            self.get_logger().warn('¡Cuidado! ¡Pared cerca! Girando... 🚧')
        else:
            cmd.linear.x = 1.0   # Avanza normal
            cmd.angular.z = 0.0
            self.get_logger().info(f'Avanzando tranqui... X={msg.x:.2f}')

        # Enviamos la orden calculada
        self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TortugaInteligente()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()