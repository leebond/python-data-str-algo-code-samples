#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:15:06 2020

@author: macbook
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data: # logic 1: check if Node contains data, if true go to logic 2A, otherwise go to 2B
            if data < self.data: # logic 2A: if incoming data is smaller than Node data, go to logic 3
                if self.left is None: # logic 3A: accessing the left node, if there is no data, do 4A else 4B, otherwise go to 3B
                    self.left = Node(data) # 4A: create a Node class for the left node initialized with data
                else:
                    self.left.insert(data) # 4B: since there is data at left node, call insert logic again
            else:
                if self.right is None: #logic 3B
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data # logic 2B: initialize the Node with data

    def inorderTraversal(self, node, res):
        if self.left:
            self.left.inorderTraversal(self.left, res)
        res.append(self.data)
        if self.right:
            self.right.inorderTraversal(self.right, res)
        return res

    def postorderTraversal(self, node):
        res = []
        if node:
            res = self.postorderTraversal(node.left) # logic: recursively traverse to the left most deepest node until return is hit,
                                                     # without keeping track of the nodes visited
            res = res + self.postorderTraversal(node.right) # if left node hits a return, recursively traverse the right node, if empty go back to 
            res.append(node.data)
        return res

    def preorderTraversal(self, node):
        res = []
        if node:
            res.append(node.data)
            res = res + self.preorderTraversal(node.left) # logic: recursively traverse to the left most deepest node until return is hit,
                                                          # keeping track of the nodes visited
            res = res + self.preorderTraversal(node.right)
        return res

if __name__=='__main__':
    vals = [27,14,35,10,19,31,42]
    root_val = vals.pop(0)
    root = Node(root_val)
    for val in vals:
        root.insert(val)
    print('Given an array: %s' %vals, end = '\n')
    print('Inorder traversal: %s' %root.inorderTraversal(root, []))
    print('Preorder traversal: %s' %root.preorderTraversal(root))
    print('Postorder traversal: %s' %root.postorderTraversal(root))
                