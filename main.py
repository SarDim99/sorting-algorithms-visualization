# In order for the code to work we need tkinter, numpy and matplotlib
# For tkinter in terminal type: pip install tkinter
# For matplotlib: pip install matplotlib
# For numpy: pip install numpy

# Sarris Dimitris 1387

import tkinter as tk
from numpy import random
from matplotlib import pyplot as plt, animation
from algos import bubblesort, mergesort, quicksort, insertionsort, heapsort, selectionsort # Importing the algoritms from algos.py

# Function performing the visualization proccess
def visualize():
    # Getting the value from options menu for size in gui
    N = int(num.get())
    #A = list(range(1, N + 1))
    #random.shuffle(A)
    A = random.randint(100, size=(N))

    # Getting the value from options menu for algorithm in gui
    algorithm = algo.get()

    sp = speed.get()

    if sp == "Slow":
        speedNum = 200
    elif sp == "Normal":
        speedNum = 150
    else:
        speedNum = 15
    
    # Creates a generator object containing all 
    # the states of the array while performing 
    # sorting algorithm
    if algorithm == "Bubble Sort":
        generator = bubblesort(A)
        o = " O(n\N{SUPERSCRIPT TWO})"
    elif algorithm == "Merge Sort":
        generator = mergesort(A, 0, len(A) - 1)
        o = " O(nlogn)"
    elif algorithm == "Quick Sort":
        generator = quicksort(A, 0, len(A)-1)
        o = " O(n\N{SUPERSCRIPT TWO})"
    elif algorithm == "Heap Sort":
        generator = heapsort(A)
        o = " O(nlogn)"
    elif algorithm == "Selection Sort":
        generator = selectionsort(A)
        o = " O(n\N{SUPERSCRIPT TWO})"
    else:
        generator = insertionsort(A)
        o = " O(n\N{SUPERSCRIPT TWO})"
      
    # Creates a figure and subsequent subplots
    fig, ax = plt.subplots()
    ax.set_title(algorithm + o)
    bar_sub = ax.bar(range(len(A)), A, align="edge")
      
    # Sets the maximum limit for the x-axis
    ax.set_xticks([])
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
      
    # Helper function to update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Number of operations: {iteration[0]}")
        
    # Creating animation object for rendering the iteration
    anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=False,
        interval=speedNum,
        save_count=90000,
    )
      
    # For showing the animation on screen
    plt.show()

# Main function  
if __name__ == "__main__":
    # Creating gui
    root = tk.Tk() # Create a tkinter window
    root.geometry("500x500") # Window dimensions
    root.title("Algorithms Visualization") # Window title
    #root.iconbitmap(r'C:\Users\dsarr\Desktop\algo2\logo.ico') # Window logo
    
    title = tk.Label(root, text="Algorithms Visualization", font=("Arial", 18)) 
    title.grid(columnspan=3, column=2, row=1)

    algoLabel = tk.Label(root, text="Algorithm: ", font=("Arial", 12)) # A simple label
    algoLabel.grid(column=1, row=2)

    algoChoice = ["Bubble Sort",
                  "Merge Sort",
                  "Quick Sort",
                  "Selection Sort",
                  "Insertion Sort",
                  "Heap Sort"]
    algo = tk.StringVar(root)
    algo.set(algoChoice[0])

    algoMenu = tk.OptionMenu(root, algo, *algoChoice) #Algorithm options
    algoMenu.grid(column=2, row=2)

    numLabel = tk.Label(root, text="Array size: ", font=("Arial", 12))
    numLabel.grid(column=1, row=3)

    numChoice = ["10",
                 "20",
                 "50",
                 "100",
                 "200"]

    num = tk.StringVar(root)
    num.set(numChoice[0])

    numMenu = tk.OptionMenu(root, num, *numChoice) #Array size options
    numMenu.grid(column=2, row=3) 

    speedLabel = tk.Label(root, text="Speed: ", font=("Arial", 12)) 
    speedLabel.grid(column=1, row=5)

    speedChoice = ["Fast",
                   "Normal",
                   "Slow"] 

    speed = tk.StringVar(root)
    speed.set(speedChoice[0])

    speedMenu = tk.OptionMenu(root, speed, *speedChoice) #Speed options
    speedMenu.grid(column=2, row=5)

    # Fill label to create an empty 6th row
    label = tk.Label(root)
    label.grid(column=1, row=6)

    button = tk.Button(root, text="Start", command=visualize) # Search button
    button.grid(column=1, row=7)   

    root.mainloop() # Must have for the window to appear
