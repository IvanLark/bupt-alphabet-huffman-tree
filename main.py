from huffman_tree import HuffmanTree
from pprint import pprint

letter_dict_list = [
    {"letter": "a", "weight": 819},
    {"letter": "b", "weight": 147},
    {"letter": "c", "weight": 383},
    {"letter": "d", "weight": 391},
    {"letter": "e", "weight": 1225},
    {"letter": "f", "weight": 226},
    {"letter": "g", "weight": 171},
    {"letter": "h", "weight": 457},
    {"letter": "i", "weight": 710},
    {"letter": "j", "weight": 41},
    {"letter": "k", "weight": 14},
    {"letter": "l", "weight": 377},
    {"letter": "m", "weight": 334},
    {"letter": "n", "weight": 706},
    {"letter": "o", "weight": 726},
    {"letter": "p", "weight": 289},
    {"letter": "q", "weight": 9},
    {"letter": "r", "weight": 685},
    {"letter": "s", "weight": 636},
    {"letter": "t", "weight": 941},
    {"letter": "u", "weight": 258},
    {"letter": "v", "weight": 109},
    {"letter": "w", "weight": 159},
    {"letter": "x", "weight": 21},
    {"letter": "y", "weight": 158},
    {"letter": "z", "weight": 8}
]

# 构建哈夫曼树
print('根据字母权重构建哈夫曼树')
huffman_tree = HuffmanTree(letter_dict_list)
print('哈夫曼树编码长度表:')
encode_dict = huffman_tree.get_encode_dict()
pprint({key: len(encode_dict[key]) for key in encode_dict})
print('哈夫曼树编码表:')
pprint(encode_dict)
print('哈夫曼编码字符串"pneumonoultramicroscopicsilicovolcanoconiosis"结果: ')
print(huffman_tree.encode_text('pneumonoultramicroscopicsilicovolcanoconiosis'))
print('可视化哈夫曼树')
huffman_tree.draw_tree()
