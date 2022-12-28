import rclpy
from rclpy.node import Node
from person_msgs.msg import Query

def cd(request, response):
    if request.name == "大良将輝":
        response.age = 20
    else:
        response = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cd)
rclpy.spin(node)

