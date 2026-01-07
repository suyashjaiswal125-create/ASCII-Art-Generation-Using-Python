def generate_ascii_art():
    height = 32
    width = 52

    for row in range(height):
        for column in range(width):
            char = ' '

            if row == 0:
                if column == 20:
                    char = ":"
                elif column == 21:
                    char = "-"
                elif 21 <= column <= 29:
                    char = "#"
                elif column == 30:
                    char = "+"
                elif column == 31:
                    char = "-"

            elif row == 1:
                if column == 16:
                    char = "."
                elif column == 17:
                    char = "*"
                elif 18 <= column <= 33:
                    char = "%"
                elif column == 34:
                    char = "+"

            elif row == 2:
                if column == 15:
                    char = "*"
                elif 16 <= column <= 35:
                    char = "%"
                elif column == 36:
                    char = "+"

            elif row == 3:
                if column == 14:
                    char = "+"
                elif 15 <= column <= 22:
                    char = "%"
                elif 23 <= column <= 29:
                    char = "#"
                elif 30 <= column <= 32:
                    char = "+"
                elif column == 33:
                    char = "*"
                elif 34 <= column <= 36:
                    char = "%"
                elif column == 37:
                    char = "="
                
            elif row == 4:
                if column == 13:
                    char ="-"
                elif 14 <= column <= 17:
                    char ="%"
                elif column == 18:
                    char ="#"
                elif column == 19:
                    char ="#"
                elif 20 <= column <= 24:
                    char ="#"
                elif column == 25:
                    char ="+"
                elif 26 <= column <= 27:
                    char ="-"
                elif 28 <= column <= 30:
                    char =":"
                elif 31 <= column <= 32:
                    char ="-"
                elif column == 33:
                    char ="="
                elif column == 34:
                    char ="*"
                elif column == 35:
                    char ="#"
                elif column == 36:
                    char ="%"
                elif column == 37:
                    char ="+"
                    
            elif row == 5:
                if column == 13:
                    char ="="
                elif 14 <= column <= 15:
                    char ="%"
                elif column == 16:
                    char ="#"
                elif 17 <= column <= 18:
                    char ="*"
                elif column == 19:
                    char ="+"
                elif  column == 20:
                    char ="="
                elif column == 21:
                    char ="-"
                elif 22 <= column <= 30:
                    char =":"
                elif 31 <= column <= 33:
                    char ="-"
                elif column == 34:
                    char ="+"
                elif 35 <= column <= 36:
                    char ="%"
                elif column == 37:
                    char ="*"
                    
            elif row == 6:
                if column == 13:
                    char =":"
                elif 14 <= column <= 15:
                    char ="%"
                elif column == 16:
                    char ="#"
                elif 17 <= column <= 18:
                    char ="+"
                elif column == 19:
                    char ="="
                elif 20 <= column <= 21:
                    char ="-"
                elif 22 <= column <= 23:
                    char =":"
                elif 24 <= column <= 30:
                    char ="."
                elif column == 31:
                    char =":"
                elif 32 <= column <= 33:
                    char ="-"
                elif column == 34:
                    char ="="
                elif column == 35:
                    char ="*"
                elif column == 36:
                    char ="%"
                elif column == 37:
                    char ="="
            
            elif row == 7:
                if column == 14:
                    char ='*'
                elif column == 15:
                    char ="%"
                elif column == 16:
                    char ="*"
                elif 17 <= column <= 19:
                    char ="+"
                elif 20 <= column <= 22:
                    char ="="
                elif column == 23:
                    char ="-"
                elif 24 <= column <= 26:
                    char =":"
                elif column == 27:
                    char ="-"
                elif column == 28:
                    char ="="
                elif column == 29:
                    char ="+"
                elif column == 30:
                    char ="*"
                elif column == 31:
                    char ="+"
                elif 32 <= column <= 33:
                    char ="="
                elif 34 <= column <= 35:
                    char ="-"
                elif column == 36:
                    char ="#"
                elif column == 37:
                    char =":"
                
            elif row == 8:
                if column == 14:
                    char ="-"
                elif column == 15:
                    char ="%"
                elif 16 <= column <= 18:
                    char ="+"
                elif column == 19:
                    char ="*"
                elif 20 <= column <= 21:
                    char ="#"
                elif 22 <= column <= 24:
                    char ="*"
                elif column == 25:
                    char ="="
                elif column == 26:
                    char =":"
                elif column == 27:
                    char ="="
                elif column == 28:
                    char ="*"
                elif column == 29:
                    char ="+"
                elif 30 <= column <= 31:
                    char ="*"
                elif column == 32:
                    char ="="
                elif column == 33:
                    char ="*"
                elif column == 34:
                    char ="="
                elif column == 35:
                    char ="-"
                elif column == 36:
                    char ="+"
                elif 37 <= column <= 38:
                    char ="-"
                    
            elif row == 9:
                if 13 <= column <= 14:
                    char ="="
                elif 15 <= column <= 17:
                    char ="+"
                elif 18 <= column <= 19:
                    char ="*"
                elif 20 <= column <= 21:
                    char ="+"
                elif 22 <= column <= 23:
                    char ="="
                elif column == 24:
                    char ="+"
                elif column == 25:
                    char ="-"
                elif column == 26:
                    char ="."
                elif column == 27:
                    char =":"
                elif 28 <= column <= 31:
                    char ="="
                elif 32 <= column <= 33:
                    char ="-"
                elif 34 <= column <= 35:
                    char =":"
                elif column == 36:
                    char ="-"
                elif column == 37:
                    char =":"
                elif column == 38:
                    char ="-"
                    
            elif row == 10:
                if 13 <= column <= 14:
                    char ="-"
                elif column == 15:
                    char ="="
                elif column == 16:
                    char ="+"
                elif column == 17:
                    char ="="
                elif 18 <= column <= 21:
                    char ="-"
                elif column == 22:
                    char =":"
                elif column == 23:
                    char ="-"
                elif column == 24:
                    char ="="
                elif column == 25:
                    char =":"
                elif column == 27:
                    char ="."
                elif column == 28:
                    char ="-"
                elif column == 29:
                    char =":"
                elif 30 <= column <= 32:
                    char ="."
                elif 33 <= column <= 34:
                    char =":"
                elif 35 <= column <= 38:
                    char ="-"
                    
            elif row == 11:
                if column == 13:
                    char =":"
                elif 14 <= column <= 15:
                    char ="-"
                elif 16 <= column <= 17:
                    char ="+"
                elif column == 18:
                    char ="="
                elif column == 19:
                    char ="-"
                elif 20 <= column <= 22:
                    char =":"
                elif 23 <= column <= 24:
                    char ="="
                elif column == 25:
                    char ="-"
                elif column == 26:
                    char ="."
                elif column == 27:
                    char =":"
                elif 28 <= column <= 30:
                    char ="-"
                elif 31 <= column <= 33:
                    char =":"
                elif 34 <= column <= 35:
                    char ="-"
                elif column == 36:
                    char ="="
                elif 37 <= column <= 38:
                    char =":"  
                    
            elif row == 12:
                if column == 14:
                    char =":"
                elif column == 15:
                    char ="-"
                elif 16 <= column <= 17:
                    char ="+"
                elif 18 <= column <= 19:
                    char ="="
                elif 20 <= column <= 21:
                    char ="-"
                elif 22 <= column <= 23:
                    char ="="
                elif 24 <= column <= 25:
                    char ="+"
                elif column == 26:
                    char ="*"
                elif column == 27:
                    char ="+"
                elif column == 28:
                    char ="="
                elif column == 29:
                    char ="-"
                elif column == 30:
                    char =":"
                elif 31 <= column <= 35:
                    char ="-"
                elif column == 36:
                    char="="
                elif column == 37:
                    char="-"
                elif column == 38:
                    char="."
                    
            elif row == 13:
                if column == 15:
                    char ="."
                elif column == 16:
                    char ="-"
                elif column == 17:
                    char ="="
                elif column == 18:
                    char ="+"
                elif 19 <= column <= 21:
                    char ="="
                elif column == 22:
                    char ="+" 
                elif 23 <= column <= 26:
                    char ="="
                elif 27 <= column <= 29:
                    char ="-"
                elif 30 <= column <= 33:
                    char ="="
                elif 34 <= column <= 36:
                    char ="-"
                elif column == 37:
                    char ="="
                    
            elif row == 14:
                if 17 <= column <= 18:
                    char ="+"
                elif 19 <= column <= 21:
                    char ="="
                elif 22 <= column <= 24:
                    char ="+"
                elif 25 <= column <= 26:
                    char ="="
                elif 27 <= column <= 30:
                    char ="-"
                elif column == 31:
                    char ="="
                elif 32 <= column <= 33:
                    char ="-"
                elif 34 <= column <= 35:
                    char ="="
                elif column == 36:
                    char="-"
                    
            elif row == 15:
                if column == 17:
                    char =":"
                elif 18 <= column <= 23:
                    char ="+"
                elif column == 24:
                    char ="="
                elif 25 <= column <= 26:
                    char ="+"
                elif 27 <= column <= 28:
                    char ="="
                elif 29 <= column <= 30:
                    char ="-"
                elif 31 <= column <= 32:
                    char ="="
                elif 33 <= column <= 34:
                    char ="+"
                elif column == 35:
                    char ="="
                    
            elif row == 16:
                if column == 18:
                    char ="-"
                elif 19 <= column <= 22:
                    char ="*"
                elif column == 23:
                    char ="+"
                elif 24 <= column <= 26:
                    char ="="
                elif 27 <= column <= 29:
                    char ="-"
                elif column == 30:
                    char ="="
                elif 31 <= column <= 34:
                    char ="+"
                elif column == 35:
                    char="."
                    
            elif row == 17:
                if column == 18:
                    char ="."
                elif column == 19:
                    char="-"
                elif column == 20:
                    char="+"
                elif 21 <= column <= 24:
                    char ="*"
                elif column == 25:
                    char="+"
                elif 26 <= column <= 31:
                    char ="*"
                elif column == 32:
                    char="+"
                elif 33 <= column <= 34:
                    char ="*"
                elif column == 36:
                    char="="
                    
            elif row == 18:
                if column == 16:
                    char ="."
                elif column == 17:
                    char ="#"
                elif column == 18:
                    char ="="
                elif 19 <= column <= 21:
                    char ="." 
                elif column == 22:
                    char ="="
                elif 23 <= column <= 28:
                    char ="*"
                elif 29 <= column <= 30:
                    char="+"
                elif column == 31:
                    char="-"
                elif 32 <= column <= 34:
                    char ="."
                elif column == 36:
                    char="+"
                elif column == 37:
                    char="#"
                elif column == 38:
                    char=":"
                    
            elif row == 19:
                if column == 14:
                    char ="."
                elif column == 15:
                    char ="#"
                elif column == 16:
                    char ="%"
                elif column == 17:
                    char ="#"
                elif column == 18:
                    char =":"
                elif column == 19:
                    char ="."
                elif column == 24:
                    char =":"
                elif 25 <= column <= 28:
                    char ="+"
                elif column == 29:
                    char="-"
                elif column == 36:
                    char="+" 
                elif 37 <= column <= 41:
                    char ="#" 
                elif column == 42:
                    char="+"
                elif column == 43:
                    char="."
                    
            elif row == 20:
                if column == 10:
                    char ="."
                elif column == 11:
                    char ="="
                elif 12 <= column <= 13:
                    char ="#"
                elif 14 <= column <= 16:
                    char ="%"
                elif column == 17:
                    char ="*"
                elif column == 18:
                    char ="."
                elif column == 25:
                    char ="."
                elif 26 <= column <= 27:
                    char =":"
                elif column == 28:
                    char="-"
                elif column == 29:
                    char="+"
                elif column == 30:
                    char="-"
                elif 37 <= column <= 46:
                    char ="#"
                elif column == 47:
                    char ="*"
                elif column == 48:
                    char ="-"
                    
            elif row == 21:
                if column == 3:
                    char ="."
                elif 4 <= column <= 13:
                    char ="#"
                elif 14 <= column <= 16:
                    char ="%"
                elif column == 17:
                    char ="*"
                elif column == 18:
                    char ="."
                elif column == 23:
                    char ="="
                elif column == 24:
                    char ="*"
                elif column == 25:
                    char ="+"
                elif column == 26:
                    char ="="
                elif column == 27:
                    char ="#"
                elif column == 28:
                    char ="="
                elif column == 29:
                    char ="+"
                elif column == 30:
                    char ="*"
                elif column == 31:
                    char ="="
                elif column == 36:
                    char ="+"
                elif 37 <= column <= 51:
                    char ="#"
                    
            elif row == 22:
                if 2 <= column <= 13:
                    char ="#"
                elif 14 <= column <= 15:
                    char ="%"
                elif column == 16:
                    char="#"
                elif column == 17:
                    char ="*"
                elif column == 18:
                    char ="."
                elif column == 24:
                    char ="="
                elif column == 25:
                    char ="#"
                elif column == 26:
                    char ="="
                elif column == 27:
                    char ="-"
                elif column == 28:
                    char ="+"
                elif column == 29:
                    char ="="
                elif column == 36:
                    char ="*"
                elif 37 <= column <= 51:
                    char ="#"
                    
            elif row == 23:
                if 2 <= column <= 13:
                    char ="#"
                elif 14 <= column <= 16:
                    char ="%"
                elif column == 17:
                    char ="*"
                elif column == 25:
                    char ="="
                elif 26 <= column <= 27:
                    char ="+"
                elif column == 28:
                    char ="."
                elif column == 35:
                    char ="."
                elif column == 36:
                    char ="*"
                elif 37 <= column <= 51:
                    char ="#"
                    
            elif row == 24:
                if 2 <= column <= 14:
                    char ="#"
                elif 15 <= column <= 16:
                    char ="%"
                elif column == 17:
                    char ="#"
                elif column == 25:
                    char ="*"
                elif 26 <= column <= 27:
                    char ="="
                elif column == 28:
                    char ="-"
                elif 36 <= column <= 51:
                    char ="#"
                    
            elif row == 25:
                if 2 <= column <= 14:
                    char ="#"
                elif 15 <= column <= 17:
                    char ="%"
                elif column == 18:
                    char ="="
                elif column == 24:
                    char ="-"
                elif column == 25:
                    char ="*"
                elif column == 26:
                    char ="="
                elif column == 27:
                    char ="-"
                elif column == 28:
                    char ="="
                elif 36 <= column <= 51:
                    char ="#"
                    
            
            print(char, end='')
        print()

generate_ascii_art()
