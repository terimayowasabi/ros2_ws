import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16,"countup", 10)
        self.create.timer(0.5, self.cd)
        self.n = 0
    def cd(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1


def main():
    rcply.init()
    node = Talker()
    rclpy.spin(node)
            
