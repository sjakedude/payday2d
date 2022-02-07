import os
import pygame


class LevelParser:
    def __init__(self, width, height):
        self.row_factor = width / 100
        self.column_factor = height / 100
        self.map = self.load_map()

    def remove_new_line_characters(self, line):
        line = line.replace(r"\n", "").replace("0", " ")
        return line

    def load_map(self):
        level_map = []
        with open("levels/bank.dat") as file:
            lines = file.readlines()
        for line in lines:
            line = self.remove_new_line_characters(line)
            level_map.append(line)
        return level_map
