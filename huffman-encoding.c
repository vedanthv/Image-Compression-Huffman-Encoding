// C Program for Huffman Encoding

#include<stdio.h>
#include<stdlib.h>

#define MAX_TREE_H 100

// Huffman Tree Node Structure
struct MinHeapNode{
    int data;
    unsigned freq;
    struct MinHeapNode *left, *right;
};