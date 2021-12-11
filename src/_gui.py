#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Code for the GUI."""
import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: Create new variable type that automaties  pathlibe (Like I have done before)
        self.filePath = tk.StringVar(value="C:\\FolditTest", name="filePath")

        self.pathDisplay = ttk.Entry(textvariable=self.filePath, name="pathDisplay")
        self.choosePath = ttk.Button(text="Select", name="choosePath")
        self.cleanSciptlog = ttk.Checkbutton(text="Clean scriptlog files?", name="cleanScriptLog")
        self.cleanOldPuzzles = ttk.Checkbutton(text="Clean Expired Puzzles (requires internet)", name="cleanOldPuzzles")
        self.startButton = ttk.Button(text="Start", command=self.start, name="startButton")
        self.closeButton = ttk.Button(text="Close", name="closeButton")


        self.pathDisplay.grid(row=0, column=0)
        self.choosePath.grid(row=0, column=1)
        self.cleanSciptlog.grid(row=1, column=0, columnspan=2, sticky=tk.W)
        self.cleanOldPuzzles.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        self.startButton.grid(row=3, column=0)
        self.closeButton.grid(row=3, column=1)

    def start(self):
        ...




    def deleteScriptLog(self):
        filePath = Path(self.filePath.get())

        scriptLogFiles = filePath.glob("scriptlog.*.xml")

        [file.unlink() for file in scriptLogFiles]


if __name__ == "__main__":

    gui = GUI()
    gui.mainloop()