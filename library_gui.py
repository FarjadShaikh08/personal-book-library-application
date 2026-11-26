import tkinter as tk
from tkinter import messagebox, ttk
from table_helper import make_table


# The allowed reading-status values once for use in multiple widgets.
READING_STATUSES = ("Want to read", "Reading", "Finished")
# The allowed personal-rating values, including the unrated option.
PERSONAL_RATINGS = ("Unrated", "1", "2", "3", "4", "5")


class LibraryWindow:
    """Main window for viewing and managing the personal collection."""

    # Describe all collection columns in the order they appear in the table.
    COLUMNS = (
        ("title", "Title", 225),
        ("author", "Author", 180),
        ("status", "Reading status", 125),
        ("online_rating", "Online rating", 100),
        ("rating", "My rating", 85),
    )

    def __init__(self, root, library):
        # Keep references to the top-level window and collection service.
        self.root = root
        self.library = library
        # Map book IDs to visible book records for later reference.
        self.visible_books = {}
        # Start the table in title order, with ascended sorting.
        self.sort_field = "title"
        self.sort_descending = False

        # Configure the main window title and size constraints.
        root.title("Personal Book Library")
        root.geometry("860x500")
        root.minsize(640, 350)

        # Create the padded main layout and make the table area expandable.
        body = ttk.Frame(root, padding=15)
        body.pack(fill="both", expand=True)
        body.columnconfigure(0, weight=1)
        body.rowconfigure(2, weight=1)

        # Display the collection heading at the top of the window.
        ttk.Label(
            body,
            text="Personal Book Library",
            font=("Lexend", 18, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 12))

        # Create the search and filter controls in a dedicated row.
        filters = ttk.Frame(body)
        filters.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        filters.columnconfigure(0, weight=1)

        # Add a text search field for title and author.
        ttk.Label(filters, text="Title or author").grid(
            row=0, column=0, sticky="w"
        )
        self.search_entry = ttk.Entry(filters)
        # Expand the search box across the remaining width of its column.
        self.search_entry.grid(row=1, column=0, padx=(0, 8), sticky="ew")
        # Search when the user presses Enter in the search.
        self.search_entry.bind("<Return>", self.refresh)

        # Add a read-only dropdown to filter by reading status.
        ttk.Label(filters, text="Reading status").grid(
            row=0, column=1, sticky="w"
        )
        self.status_filter = ttk.Combobox(
            filters,
            values=("All statuses",) + READING_STATUSES,
            state="readonly",
            width=14,
        )
        # Select the option that does not restrict reading status as default.
        self.status_filter.current(0)
        self.status_filter.grid(row=1, column=1, padx=(0, 8))
        # Refresh automatically after a status selection changes.
        self.status_filter.bind("<<ComboboxSelected>>", self.refresh)
        # Add a read-only dropdown to filter by personal rating.
        ttk.Label(filters, text="My rating").grid(
            row=0, column=2, sticky="w"
        )
        self.rating_filter = ttk.Combobox(
            filters,
            values=("All ratings",) + PERSONAL_RATINGS,
            state="readonly",
            width=11,
        )
        # Select the option that does not restrict personal rating as default.
        self.rating_filter.current(0)
        self.rating_filter.grid(row=1, column=2, padx=(0, 8))
        # Refresh automatically after a selection changes.
        self.rating_filter.bind("<<ComboboxSelected>>", self.refresh)

        # Provide a search button in addition to Enter-key search.
        ttk.Button(filters, text="Search", command=self.refresh).grid(
            row=1, column=3
        )

        # Each row uses the book's ID, even after sorting or filtering.
        table_frame, self.tree = make_table(body, self.COLUMNS, height=12)
        table_frame.grid(row=2, column=0, sticky="nsew")

        # Turn each heading into a button that changes the sort field.
        for field, heading, width in self.COLUMNS:
            self.tree.heading(
                field,
                command=lambda selected_field=field: self.sort_by(selected_field),
            )

        # Keep edit and delete functionality synchronized with row selection.
        self.tree.bind("<<TreeviewSelect>>", self.update_buttons)

        # Create the action row below the table.
        actions = ttk.Frame(body)
        actions.grid(row=3, column=0, sticky="ew", pady=(12, 6))

        # Create a button to open the add dialog.
        ttk.Button(actions, text="Add", command=self.open_add_window).pack(
            side="left"
        )

        # Edit should require one selected row.
        self.edit_button = ttk.Button(
            actions, text="Edit", command=self.open_edit_window, state="disabled"
        )
        self.edit_button.pack(side="left", padx=6)

        # Delete should require one selected row.
        self.delete_button = ttk.Button(
            actions, text="Delete", command=self.delete_book, state="disabled"
        )
        self.delete_button.pack(side="left")

        # Place refresh on the right as a convenience.
        ttk.Button(actions, text="Refresh", command=self.refresh).pack(
            side="right"
        )

        # Reserve a label for showing the number of matching visible books.
        self.count_label = ttk.Label(body)
        self.count_label.grid(row=4, column=0, sticky="w")

        # add the initial table with the collection data.
        self.refresh()

    def refresh(self, event=None):
        """Reload the collection and display its books."""
        # TODO: Implement collection refresh, including search and filters.
        pass

    def sort_by(self, field):
        """Toggle the sort direction for the active field or start sorting another field."""
        # TODO: Implement column sorting.
        pass

    def update_buttons(self, event=None):
        """Enable row-dependent actions only while a table row is selected."""
        # Selection is converted into an enabled or disabled widget state.
        state = "normal" if self.tree.selection() else "disabled"
        # Keep edit and delete in sync with the current selection.
        self.edit_button.configure(state=state)
        self.delete_button.configure(state=state)

    def open_add_window(self):
        """Open the dialog for adding a catalog result to the collection."""
        # TODO: Implement the add-book dialog.
        pass

    def open_edit_window(self):
        """Open the dialog for editing the currently selected collection row."""
        # TODO: Implement the edit-book dialog.
        pass

    def delete_book(self):
        """Delete the selected book through the collection service."""
        # TODO: Implement book deletion.
        pass


