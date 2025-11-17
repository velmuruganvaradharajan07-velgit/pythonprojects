'''class a:
    def __init__(self,nodes,values):
        self.nodes=nodes
        self.values=values



    def set_values(self, nodes, values):
        """        Write values to multiple nodes in one ua call        """

    nodeids = [node.nodeid for node in nodes]
    dvs = [ua_utils.value_to_datavalue(val) for val in values]
    results = self.uaclient.set_attributes(nodeids, dvs, ua.AttributeIds.Value)
    for result in results: result.check()
     nodeids = [node.nodeid for node in nodes]
    dvs = [ua_utils.value_to_datavalue(val) for val in values]
    results = self.uaclient.set_attributes(nodeids, dvs, ua.AttributeIds.Value)

    for result in results:
        result.check()

b=a
b.set_values(10,10)'''
from opcua.common import utils
from opcua.common import ua_utils
def set_values(self, nodes, values):
    """
    Write values to multiple nodes in one UA call.

    Parameters:
    - nodes: list of node objects
    - values: list of values to write to the corresponding nodes
    """
    nodeids = [node.nodeid for node in nodes]
    dvs = [ua_utils.value_to_datavalue(val) for val in values]
    results = self.uaclient.set_attributes(nodeids, dvs, ua.AttributeIds.Value)

    for result in results:
        result.check()

set_values(10,10,10)