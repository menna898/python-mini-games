def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    # فحص الصفوف الثلاثة
    if board[0] == board[1] == board[2] != " ": return board[0]
    if board[3] == board[4] == board[5] != " ": return board[3]
    if board[6] == board[7] == board[8] != " ": return board[6]
    
    # فحص الأعمدة الثلاثة
    if board[0] == board[3] == board[6] != " ": return board[0]
    if board[1] == board[4] == board[7] != " ": return board[1]
    if board[2] == board[5] == board[8] != " ": return board[2]
    
    # فحص المقصات (القطر الرئيسي والفرعي)
    if board[0] == board[4] == board[8] != " ": return board[0]
    if board[2] == board[4] == board[6] != " ": return board[2]
    
    return None

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ": return board[combo[0]]
    return None

def play_game():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    
    print("--- لعبة X - O ---")
    
    while True:
        print_board(board)
        
        try:
            choice = int(input(f"دور ({current_player}) - اختار رقم المربع: "))
            index = choice - 1
            
            # التأكد إن الرقم صح والمكان مش محجوز
            if choice < 1 or choice > 9 or board[index] == "X" or board[index] == "O":
                print("حركة غلط! اختار مربع فاضي")
                continue
                
        except ValueError:
            print(" اكتب رقم بس!")
            continue
            
        # تسجيل الحركة للاعب الحالي
        board[index] = current_player
        
        # فحص الفوز
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"مبروك! اللاعب ({winner}) هو الفائز! 🎉")
            break 
            
        # فحص التعادل
        if all(slot == "X" or slot == "O" for slot in board):
            print_board(board)
            print(" اللعبة انتهت بالتعادل!")
            break
            
        # تبديل الدور أوتوماتيك بين X و O
        current_player = "O" if current_player == "X" else "X"

# تشغيل اللعبة
play_game()
