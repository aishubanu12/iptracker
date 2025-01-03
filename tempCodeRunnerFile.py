ields(inputEntry, outputMsg, map_widget))
clearButton.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Configure Grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start the Tkinter loop
root.mainloop()
