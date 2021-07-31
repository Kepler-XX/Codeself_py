from pprint import pprint
from xml.dom.minidom import parse

# minidom解析器打开xml文档并将其解析为内存中的一棵树
DOMTree = parse(r'8810A00085G200.xml')
# 获取xml文档对象，就是拿到树的根
collection = DOMTree.documentElement
all = dict()
nodes = collection.getElementsByTagName('node')
nodes_ls = []
for node in nodes:
    node_dict = dict()
    if node.hasAttribute('name'):
        name = node.getAttribute('name')
        node_dict['name'] = name
        # print('name is ', node.getAttribute('name'))
    if node.hasAttribute('displayName'):
        displayName = node.getAttribute('displayName')
        node_dict['displayName'] = displayName
        # print('displayName is ', node.getAttribute('displayName'))
    if node.hasAttribute('id'):
        id = node.getAttribute('id')
        node_dict['id'] = id
        # print('id is ', node.getAttribute('id'))
    positions = node.getElementsByTagName("Position")[0]
    # print(positions)
    if positions.hasAttribute('x'):
        x = '%.4f' % (float(positions.getAttribute('x')) * 1000)
        node_dict['x'] = x
        # print('x is ', '%.4f' % (float(positions.getAttribute('x')) * 1000))
    if positions.hasAttribute('y'):
        y = '%.4f' % (float(positions.getAttribute('y')) * 1000)
        node_dict['y'] = y
        # print('y is ', '%.4f' % (float(positions.getAttribute('y')) * 1000))
    if positions.hasAttribute('z'):
        z = '%.4f' % (float(positions.getAttribute('z')) * 1000)
        node_dict['z'] = z
        # print('z is ', '%.4f' % (float(positions.getAttribute('z')) * 1000))
    # print('****************************************')
    nodes_ls.append(node_dict)

bundles = collection.getElementsByTagName('bundle')
bundles_ls = []
for bundle in bundles:
    segment_ls = []
    bundle_dict = dict()
    bundle_dict['segment_dict'] = {}
    if bundle.hasAttribute('name'):
        name = bundle.getAttribute('name')
        bundle_dict['name'] = name
        # print('name is ', bundle.getAttribute('name'))
    if bundle.hasAttribute('displayName'):
        displayName = bundle.getAttribute('displayName')
        bundle_dict['displayName'] = displayName
        # print('displayName is ', bundle.getAttribute('displayName'))
    if bundle.hasAttribute('id'):
        id = bundle.getAttribute('id')
        bundle_dict['id'] = id
        # print('id is ', bundle.getAttribute('id'))
    if bundle.hasAttribute('startNode'):
        startNode = bundle.getAttribute('startNode')
        bundle_dict['startNode'] = startNode
        # print('startNode is ', bundle.getAttribute('startNode'))
    if bundle.hasAttribute('endNode'):
        endNode = bundle.getAttribute('endNode')
        bundle_dict['endNode'] = endNode
        # print('endNode is ', bundle.getAttribute('endNode'))
    if bundle.hasAttribute('length'):
        length = bundle.getAttribute('length')
        bundle_dict['length'] = length
        # print('length is ', bundle.getAttribute('length'))
    if bundle.hasAttribute('bundleDiameter'):
        bundleDiameter = bundle.getAttribute('bundleDiameter')
        bundle_dict['bundleDiameter'] = bundleDiameter
        # print('bundleDiameter is ', bundle.getAttribute('bundleDiameter'))
    if bundle.hasAttribute('maxDiameter'):
        maxDiameter = bundle.getAttribute('maxDiameter')
        bundle_dict['maxDiameter'] = maxDiameter
        # print('maxDiameter is ', bundle.getAttribute('maxDiameter'))
    if bundle.hasAttribute('bendRadius'):
        bendRadius = bundle.getAttribute('bendRadius')
        bundle_dict['bendRadius'] = bendRadius
        # print('bendRadius is ', bundle.getAttribute('bendRadius'))
    bundles_ls.append(bundle_dict)
    for segment_str in bundle.getElementsByTagName('segments'):
        waypoint_ls = []
        bundle_dict['segment_dict']['waypoint_dict'] = {}
        segment = segment_str.getElementsByTagName("segment")[0]
        if segment.hasAttribute('type'):
            type = segment.getAttribute('type')
            bundle_dict['segment_dict']['type'] = type
            # print('type is ', segment.getAttribute('type'))
        if segment.hasAttribute('length'):
            length = segment.getAttribute('length')
            bundle_dict['segment_dict']['length'] = length
            # print('length is ', segment.getAttribute('length'))
        if segment.hasAttribute('start'):
            start = segment.getAttribute('start')
            bundle_dict['segment_dict']['start'] = start
            # print('start is ', segment.getAttribute('start'))
        if segment.hasAttribute('end'):
            end = segment.getAttribute('end')
            bundle_dict['segment_dict']['end'] = end
            # print('end is ', segment.getAttribute('end'))
        waypoints = segment_str.getElementsByTagName("waypoint")
        for waypoint in waypoints:
            # if waypoint.hasAttribute('id'):
            id = waypoint.getAttribute('id')
            bundle_dict['segment_dict']['waypoint_dict']['id'] = id
                # print('id is ', waypoint.getAttribute('id'))
            Direction = waypoint.getElementsByTagName("Direction")[0]
            # if Direction.hasAttribute('x'):
            x = '%.4f' % (float(Direction.getAttribute('x')) * 1000)
            bundle_dict['segment_dict']['waypoint_dict']['x'] = x
                # print('x is ', '%.4f' % (float(Direction.getAttribute('x')) * 1000))
            # if Direction.hasAttribute('y'):
            y = '%.4f' % (float(Direction.getAttribute('y')) * 1000)
            bundle_dict['segment_dict']['waypoint_dict']['y'] = y
                # print('y is ', '%.4f' % (float(Direction.getAttribute('y')) * 1000))
            # if Direction.hasAttribute('z'):
            z = '%.4f' % (float(Direction.getAttribute('z')) * 1000)
            bundle_dict['segment_dict']['waypoint_dict']['z'] = z
                # print('z is ', '%.4f' % (float(Direction.getAttribute('z')) * 1000))
            waypoint_ls.append(bundle_dict['segment_dict']['waypoint_dict'])
        segment_ls.append(bundle_dict['segment_dict'])
    bundles_ls.append(bundle_dict)
    # print('----------------------------------------------')

all['nodes'] = nodes_ls
all['bundles'] = bundles_ls
pprint(all)
