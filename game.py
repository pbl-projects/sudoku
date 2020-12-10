import sudoku

model = sudoku.Model()
model.load_quiz()
view = sudoku.View()
while not model.solved():
    view.display_board(model.current)
    row, col, value = view.play()
    msg = model.play(row, col, value)
    view.error = msg