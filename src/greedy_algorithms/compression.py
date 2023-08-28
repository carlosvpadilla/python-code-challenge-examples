#
# Copyright (c) 2023, Carlos Vergara
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
import sys
from typing import Optional


class HuffmanNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.weight = 0


class HuffmanLeaf(HuffmanNode):
    def __init__(self, letter, weight = 0):
        super().__init__()
        self.letter = letter
        self.weight = weight


class HuffmanTree:
    root: Optional[HuffmanNode]

    def __init__(self):
        self.root = None
    
    def _recursive_build(self, node: HuffmanNode, codeword: int) -> dict[str, int]:
        if isinstance(node, HuffmanLeaf):
            return {
                node.letter: codeword
            }
        
        left_codeword = self._recursive_build(node.left, codeword << 1)
        right_codeword = self._recursive_build(node.right, (codeword << 1) + 0b1)

        right_codeword.update(left_codeword)
        return right_codeword
        
    
    def build_codewords(self) -> dict[str, int]:
        return self._recursive_build(self.root, 0b0)


def constant_length_compress(input: str) -> int:
    codewords = {
        "A": 0b0,
        "B": 0b1,
        "C": 0b10,
        "D": 0b11
    }
    compressed_input = 0b1
    length = 0
    for char in input:
        compressed_input = compressed_input << 2
        compressed_input |= codewords[char]
        length += 2
    return compressed_input


def variable_length_compress(input: str, codewords: dict[str, int]) -> int:
    compressed_input = 0b1
    length = 0
    for char in input:
        codeword = codewords[char]
        compressed_input = compressed_input << codeword.bit_length()
        compressed_input |= codeword
        length += codeword.bit_length()
    return compressed_input


def combine_nodes(left: HuffmanNode, right: HuffmanNode) -> HuffmanNode:
    parent = HuffmanNode()
    parent.weight = left.weight + right.weight
    parent.left = left
    parent.right = right
    return parent


def huffman_compress(input: str) -> int:
    frequency_table = dict()
    for i in input:
        frequency_table[i] = 1 + frequency_table.get(i, 0)
    leaves = [
        HuffmanLeaf(k, v) for k, v in frequency_table.items()
    ]
    leaves.sort(key=lambda l: l.weight)

    tree = HuffmanTree()

    if len(leaves) == 0:
        raise RuntimeError("Tree should not be empty")

    if len(leaves) == 1:
        tree.root = leaves[0]
    else:
        # Combine first two items
        root = combine_nodes(leaves[0], leaves[1])
        for item in leaves[2:]:
            root = combine_nodes(item, root)
        
        tree.root = root
    
    codewords = tree.build_codewords()
    return variable_length_compress(input, codewords)


if __name__ == "__main__":
    string_to_compress = "AABACDACA"
    print("Suppose we have this string:")
    print(string_to_compress)
    print("In memory, this has a weight of "
          f"{sys.getsizeof(string_to_compress)} bytes")
    print("If we perform a constant length compression, we get this:")
    constant_length_compressed = constant_length_compress(string_to_compress)
    print(bin(constant_length_compressed))
    print("In memory, this has a weight of "
          f"{constant_length_compressed.bit_length()} bytes")
    print("But using a variable length compression might be more optimal:")
    variable_length_codewords = {
        "A": 0b0,
        "B": 0b110,
        "C": 0b10,
        "D": 0b111
    }
    variable_length_compressed = variable_length_compress(
        string_to_compress, variable_length_codewords)
    print(bin(variable_length_compressed))
    print("In memory, this has a weight of "
          f"{variable_length_compressed.bit_length()} bytes")
    print("We can also try and use a Huffman coding tree:")
    huffman_compressed = huffman_compress(string_to_compress)
    print(bin(huffman_compressed))
    print("In memory, this has a weight of "
          f"{huffman_compressed.bit_length()} bytes")
    