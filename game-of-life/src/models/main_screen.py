class MainScreen:
    def __init__(self, width, height, horizontal_cells, vertical_cells, back_ground_color):
        self.width = width
        self.height = height
        self.horizontal_cells = horizontal_cells
        self.vertical_cells = vertical_cells
        self.back_ground_color = back_ground_color
        self.cell_width = 0
        self.cell_height = 0

    def getWidth(self) -> int:
        return self.width

    def setWidth(self, val) -> None:
        self.height = val

    def getHeight(self) -> int:
        return self.width

    def setHeight(self, val) -> None:
        self.width = val

    def getHorizontalCells(self) -> int:
        return self.horizontal_cells

    def setHorizontalCells(self, val) -> None:
        self.horizontal_cells = val

    def getVerticalCells(self) -> int:
        return self.vertical_cells

    def setVerticalCells(self, val) -> None:
        self.vertical_cells = val

    def getBackGroundColor(self) -> tuple:
        return self.back_ground_color

    def setBackGroundColor(self, val) -> None:
        self.back_ground_color = val

    def getWidthCell(self) -> float:
        return self.cell_width

    def setWidthCell(self, val) -> None:
        self.cell_width = val

    def getHeightCell(self) -> float:
        return self.cell_height

    def setHeightCell(self, val) -> None:
        self.cell_height = val

    def __repr__(self):
        return 'MainScreen [' \
               'Width: %rpx, ' \
               'Height: %rpx, ' \
               'Horizontal Cells: %r, ' \
               'Vertical Cells: %r, ' \
               'BackGroundColor(R,G,B): %r]' % \
               (
                   self.width,
                   self.height,
                   self.horizontal_cells,
                   self.vertical_cells,
                   self.back_ground_color
               )
