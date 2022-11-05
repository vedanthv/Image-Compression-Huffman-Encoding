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

// MinHeap -> Collection of Huffman Tree nodes
struct MinHeap{
    unsigned size; // Current size of minHeap
    unsigned capacity; //Capacity of MinHeap
    struct MinHeapNode **array; // Array of pointers
};

// Utility funtion to allocate a heap to a single character
struct MinHeapNode* newNode(int data, unsigned freq)
{
    struct MinHeapNode* temp =
          (struct MinHeapNode*) malloc(sizeof(struct MinHeapNode));
    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

// Utility Function to Create MinHeap of a Capacity 
struct MinHeap* createMinHeap(unsigned capacity)
{
    struct MinHeap* minHeap =
         (struct MinHeap*) malloc(sizeof(struct MinHeap));
    minHeap->size = 0;  // current size is 0
    minHeap->capacity = capacity;
    minHeap->array =
     (struct MinHeapNode**)malloc(minHeap->capacity * sizeof(struct MinHeapNode*));
    return minHeap;
}




