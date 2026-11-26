from tkinter import ttk


def make_table(parent, columns, height):
    """Create a themed Treeview with vertical and horizontal scrollbars.

    Each column description is a three-item tuple containing its data name,
    display heading, and preferred width.
    """
    # Use a frame as a resizeable container for the table and scrollbars.
    frame = ttk.Frame(parent)
    # Let the table grow to fill the frame's row and column.
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    # Extract the only internal column names for the Treeview constructor.
    column_names = [name for name, heading, width in columns]
    # Create a read-only heading-oriented table that allows one selected row.
    tree = ttk.Treeview(
        frame,
        columns=column_names,
        show="headings",
        selectmode="browse",
        height=height,
    )

    # Configure each heading label and column presentation.
    for name, heading, width in columns:
        tree.heading(name, text=heading)
        tree.column(name, width=width, minwidth=75, anchor="w")

    # Create independent scrollbars for both table directions.
    vertical = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    horizontal = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    # Connect scrollbar movement to their matching table axes.
    tree.configure(
        yscrollcommand=vertical.set,
        xscrollcommand=horizontal.set,
    )

    # Place the table and scrollbars in a grid layout.
    tree.grid(row=0, column=0, sticky="nsew")
    vertical.grid(row=0, column=1, sticky="ns")
    horizontal.grid(row=1, column=0, sticky="ew")

    # Return the container and table so callers can place and control them.
    return frame, tree
