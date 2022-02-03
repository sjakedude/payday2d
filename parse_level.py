import os
import pygame


class LevelParser:
    def __init__(self, width, height):
        self.row_factor = width / 100
        self.column_factor = height / 100

    def remove_new_line_characters(self, line):
        line = line.replace(r"\n", "")
        return line

    def load_level(self, screen):
        rects = []
        with open("levels/bank.dat") as file:
            lines = file.readlines()
        row = 0
        column = 0
        for line in lines:
            line = self.remove_new_line_characters(line)
            for item in line:
                if item == "1":
                    rect = pygame.Rect(column * self.column_factor, row * self.row_factor, self.column_factor, self.row_factor)
                    rects.append(rect)
                row += 1
            row = 0
            column += 1
        return rects

