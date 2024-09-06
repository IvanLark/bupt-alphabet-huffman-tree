import sys
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, letter: str, weight: int, left_child, right_child):
        self.letter = letter
        self.weight = weight
        self.left_child = left_child
        self.right_child = right_child


class HuffmanTree:
    # 构建哈夫曼树
    # 输入格式为: [{"letter": "a", "weight": 2}]
    def __init__(self, letter_dict_list: list):
        # 获取所有叶子节点
        node_list = []
        for letter_dict in letter_dict_list:
            node_list.append(Node(
                letter=letter_dict['letter'],
                weight=letter_dict['weight'],
                left_child=None,
                right_child=None
            ))
        # 构建路径节点
        while len(node_list) > 1:
            # 寻找weight最小的两个节点
            first_min_weight = sys.maxsize
            first_min_index = 0
            second_min_weight = sys.maxsize
            second_min_index = 0
            node_index = 0
            while node_index < len(node_list):
                node = node_list[node_index]
                if node.weight < first_min_weight:
                    # 要先让第二小被第一小顶替再让新的第一小顶替原来的第一小
                    second_min_weight = first_min_weight
                    second_min_index = first_min_index
                    first_min_weight = node.weight
                    first_min_index = node_index
                    node_index += 1
                    continue
                if node.weight < second_min_weight:
                    second_min_weight = node.weight
                    second_min_index = node_index
                    node_index += 1
                    continue
                node_index += 1

            # 构建weight最小的两个节点的父节点
            parent_node = Node(
                letter='',
                weight=first_min_weight+second_min_weight,
                left_child=node_list[first_min_index],
                right_child=node_list[second_min_index]
            )

            # 删除weight最小的两个节点
            node_list = [node_list[i] for i in range(len(node_list)) if i not in (first_min_index, second_min_index)]

            # 将父节点添加进node_list中
            node_list.append(parent_node)

        # 当循环结束，node_list应只剩下一个节点，即根节点
        self.root = node_list[0] if len(node_list) > 0 else None

    # 获取哈夫曼编码表
    def get_encode_dict(self):
        # 获取哈夫曼编码表-深度优先遍历递归体
        def encode_dict_dfs(node: Node, cur_code: str) -> dict:
            if node.letter != '':
                return {node.letter: cur_code}
            # 定义左路径为 0 右路径为 1
            left_child_dict = encode_dict_dfs(node.left_child, cur_code + '0')
            right_child_dict = encode_dict_dfs(node.right_child, cur_code + '1')
            return left_child_dict | right_child_dict

        return encode_dict_dfs(self.root, '')

    # 使用哈夫曼树对文本进行编码
    def encode_text(self, text: str):
        encode_dict = self.get_encode_dict()
        encoded_text = ''
        for letter in list(text):
            if letter not in encode_dict:
                return None
            encoded_text += encode_dict[letter]
        return encoded_text

    # 使用哈夫曼树对密文进行解码
    def decode_text(self, text: str):
        encode_dict = self.get_encode_dict()
        # encode_dict的key和value反转
        decode_dict = {value: key for key, value in encode_dict.items()}
        decoded_text = ''
        while len(text) > 0:
            is_match = False
            for key in decode_dict:
                if text.startswith(key):
                    is_match = True
                    decoded_text += decode_dict[key]
                    if len(text) > len(key):
                        text = text[len(key):]
                    else:
                        text = ''
            if not is_match:
                return None
        return decoded_text

    # 可视化哈夫曼树
    def draw_tree(self):
        # 哈夫曼树可视化-添加边的递归体
        # 获取哈夫曼编码表-深度优先遍历递归体
        def edge_list_dfs(parent_label: str, node: Node, edge_weight: int) -> list:
            if node.letter != '':
                return [(parent_label, f'[{node.letter.upper()}]\n{node.weight}', {'weight': edge_weight})]
            node_label = str(node.weight)
            cur_list = [(parent_label, node_label, {'weight': edge_weight})] if parent_label else []
            left_child_list = edge_list_dfs(node_label, node.left_child, 0)
            right_child_list = edge_list_dfs(node_label, node.right_child, 1)
            return cur_list + left_child_list + right_child_list

        edge_list = edge_list_dfs(None, self.root, None)
        # 创建一个空的有向图
        G = nx.DiGraph()
        # 添加节点和边来构建树形结构
        G.add_edges_from(edge_list)
        # 使用networkx的树形布局算法
        pos = nx.bfs_layout(G, start=str(self.root.weight))  # 使用spring_layout布局
        # 绘制图形
        nx.draw(G, pos, with_labels=True, node_size=1100, node_color="skyblue", font_size=12, font_weight="normal",
                arrows=True)
        # 绘制边的权重
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        # 显示图形
        plt.show()
