from pprint import pprint
from xml.dom.minidom import parse


def extract_waypoint(waypoints):
    inner3 = []
    for waypoint in waypoints:
        waypoint_dic = {}

        id = waypoint.getAttribute('id')
        waypoint_dic['id'] = id

        Direction = waypoint.getElementsByTagName("Direction")[0]

        Direction_x = '%.4f' % (float(Direction.getAttribute('x')) * 1000)
        waypoint_dic['Direction_x'] = Direction_x

        Direction_y = '%.4f' % (float(Direction.getAttribute('y')) * 1000)
        waypoint_dic['Direction_y'] = Direction_y

        Direction_z = '%.4f' % (float(Direction.getAttribute('z')) * 1000)
        waypoint_dic['Direction_z'] = Direction_z
        inner3.append(waypoint_dic)
    return inner3



# minidom解析器打开xml文档并将其解析为内存中的一棵树
DOMTree = parse(r'8810A00085G200.xml')
# 获取xml文档对象，就是拿到树的根
collection = DOMTree.documentElement
all = dict()
nodes = collection.getElementsByTagName('node')
nodes_ls = []
# for node in nodes:
#     node_dict = dict()
#
#     name = node.getAttribute('name')
#     node_dict['name'] = name
#
#     displayName = node.getAttribute('displayName')
#     node_dict['displayName'] = displayName
#
#     id = node.getAttribute('id')
#     node_dict['id'] = id
#
#     positions = node.getElementsByTagName("Position")[0]
#
#     x = '%.4f' % (float(positions.getAttribute('x')) * 1000)
#     node_dict['x'] = x
#
#     y = '%.4f' % (float(positions.getAttribute('y')) * 1000)
#     node_dict['y'] = y
#
#     z = '%.4f' % (float(positions.getAttribute('z')) * 1000)
#     node_dict['z'] = z
#
#     nodes_ls.append(node_dict)

bundles = collection.getElementsByTagName('bundle')
bundles_ls = []
for bundle in bundles:
    bundle_dict = dict()

    name = bundle.getAttribute('name')
    bundle_dict['name'] = name

    displayName = bundle.getAttribute('displayName')
    bundle_dict['displayName'] = displayName

    id = bundle.getAttribute('id')
    bundle_dict['id'] = id

    startNode = bundle.getAttribute('startNode')
    bundle_dict['startNode'] = startNode

    endNode = bundle.getAttribute('endNode')
    bundle_dict['endNode'] = endNode

    length = bundle.getAttribute('length')
    bundle_dict['length'] = length

    bundleDiameter = bundle.getAttribute('bundleDiameter')
    bundle_dict['bundleDiameter'] = bundleDiameter

    maxDiameter = bundle.getAttribute('maxDiameter')
    bundle_dict['maxDiameter'] = maxDiameter

    bendRadius = bundle.getAttribute('bendRadius')
    bundle_dict['bendRadius'] = bendRadius
    inner2 = []

    for segment_str in bundle.getElementsByTagName('segments'):
        segment_dic_d = {}
        segment_dic_d['segment'] = {}
        segment = segment_str.getElementsByTagName("segment")[0]

        segment_type = segment.getAttribute('type')
        segment_dic_d['segment']['segment_type'] = segment_type

        segment_length = segment.getAttribute('length')
        segment_dic_d['segment']['segment_length'] = segment_length

        segment_start = segment.getAttribute('start')
        segment_dic_d['segment']['segment_start'] = segment_start

        segment_end = segment.getAttribute('end')
        segment_dic_d['segment']['segment_end'] = segment_end

        waypoints = segment_str.getElementsByTagName("waypoint")

        inner2.append(segment_dic_d['segment'])
        inner3 = extract_waypoint(waypoints)

        segment_dic_d['waypoint'] = inner3
        segment_dic_d['segment'] = inner2
        bundle_dict['segment_all'] = segment_dic_d
    bundles_ls.append(bundle_dict)


all['nodes'] = nodes_ls
all['bundles'] = bundles_ls
pprint(all)



