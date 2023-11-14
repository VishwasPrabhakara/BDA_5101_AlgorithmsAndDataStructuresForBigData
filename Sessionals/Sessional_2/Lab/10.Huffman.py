import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    char_freq = defaultdict(int)

    for char in data:
        char_freq[char] += 1

    min_heap = []
    for char, freq in char_freq.items():
        min_heap.append(Node(char, freq))

    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        merged_node = Node(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(min_heap, merged_node)

    return min_heap[0]

def build_huffman_codes(root):
    def traverse(node, current_code):
        if node is None:
            return

        if node.char:
            huffman_codes[node.char] = current_code
            return

        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    huffman_codes = {}
    traverse(root, "")
    return huffman_codes

def huffman_encoding(data):
    if not data:
        return "", None

    root = build_huffman_tree(data)
    huffman_codes = build_huffman_codes(root)

    encoded_data = ''.join([huffman_codes[char] for char in data])
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return ""

    current = root
    decoded_data = ""

    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char:
            decoded_data += current.char
            current = root

    return decoded_data

if __name__ == '__main__':
    data = "this is an example for huffman encoding"
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"Original data: {data}")
    print(f"Encoded data: {encoded_data}")
    print(f"Decoded data: {decoded_data}")
