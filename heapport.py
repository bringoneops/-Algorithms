# Install modules prior to execution
import matplotlib.pyplot as plt
import networkx as nx
from docx import Document
from docx.shared import Inches
import numpy as np
import os

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left or right child is larger than root
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def draw_heap(arr, title, filename):
    # Create a directed graph
    G = nx.DiGraph()
    positions = {}
    labels = {}
    n = len(arr)

    # Assuming a complete binary tree, calculate positions in a way that the parent is above children
    for i in range(n):
        level = int(np.log2(i+1))
        num_nodes_on_level = 2**level
        x_position = 4 * (i - num_nodes_on_level + 1) + 2 * (num_nodes_on_level - 1)
        y_position = 2 * (np.log2(n) - level)
        positions[i] = (x_position, y_position)
        labels[i] = str(arr[i])
        if i != 0:  # If not the root node
            G.add_edge((i - 1) // 2, i)

    # Draw the graph representing the heap
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, pos=positions, labels=labels, with_labels=True, node_size=3000, node_color="skyblue", alpha=0.5)

    # Add title and remove axes
    plt.title(title)
    plt.axis('off')

    # Save the figure
    plt.savefig(filename)
    plt.close()

def create_document(plots):
    doc = Document()
    for i, plot in enumerate(plots):
        if i % 4 == 0 and i != 0:  # Start a new page after every 4 images
            doc.add_page_break()
        doc.add_picture(plot, width=Inches(6.0))
        os.remove(plot)  # Remove the file after adding to the document
    doc.save("Heap_Visualization.docx")

# Test data
data_sets = [
    [5, 1, 3, 4, 10],
    [10, 7, 8, 9, 1, 5],
    [100, 55, 45, 35, 25, 15, 10, 5]

]

# Generate and save the plots
plots = []
for i, data_set in enumerate(data_sets, start=1):
    filename_start = f"heap_{i}_start.png"
    draw_heap(data_set, f"Dataset {i} Start", filename_start)
    plots.append(filename_start)

    sorted_data = heap_sort(data_set[:])  # Create a sorted copy of the data
    filename_finish = f"heap_{i}_finish.png"
    draw_heap(sorted_data, f"Dataset {i} Finish", filename_finish)
    plots.append(filename_finish)

create_document(plots)
print("Document with heap visualizations created.")
