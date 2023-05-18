"""

CHARACTER PALETTE
You can copy the necessary characters for drawing cards from here.

Horizontal lines:  │

Vertical lines:  ─

Corners of a card:  ┐  ┌  ┘  └

Intersections of two cards:

    if card1_height == card2_height:  ┬  ┴

    if card1_height < card2_height:  ┤

    if card1_height > card2_height:  ├

"""

print("This program will draw two cards next to each other.")
print("─" * 20)

print("Texts must not be empty.")
card1_text = input("Text of first card: ")
card2_text = input("Text of second card: ")
print("─" * 20)

##############################
# INSERT YOUR CODE HERE
# Assign proper values to card1_min_width and card2_min_width here.
# They are length of the corresponding text + 2.
# For example, if card1_text contains 5 characters, then card1_min_width must be 7.
card1_min_width = len(card1_text) + 2
card2_min_width = len(card2_text) + 2
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

print("Width of first card must be at least " + str(card1_min_width) + ".")
card1_width = int(input("Width of first card: "))
print("Width of second card must be at least " + str(card2_min_width) + ".")
card2_width = int(input("Width of second card: "))
print("─" * 20)

print("Heights must be odd and at least 3.")
card1_height = int(input("Height of first card: "))
card2_height = int(input("Height of second card: "))
print("─" * 20)


##############################
# INSERT YOUR CODE HERE
# Assign the proper value to is_invalid.
# Check if there is at least one problem in the inputs.
# I added two conditions, add more to the line below.
is_invalid = len(card1_text) == 0 or len(card2_text) == 0 or card1_width < card1_min_width  or card2_width < card2_min_width or card1_height < 3 or card2_height < 3 or card1_height%2 == 0 or card2_height%2 == 0
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

if is_invalid:
    print("ERROR: Invalid inputs.")

else:

    if card1_height == card2_height:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 1
        # You can add as many new lines as you need.

        #lines that repeats for each condition.
        card1_horizontal = card1_width - 2 - len(card1_text)
        card1_left = card1_horizontal // 2
        card1_right = card1_horizontal - card1_left
        card2_horizontal = card2_width - 2 - len(card2_text)
        card2_left = card2_horizontal // 2
        card2_right = card2_horizontal - card2_left

        center_line = "│" + card1_left * " " + card1_text + card1_right * " " + "│" + card2_left * " " + card2_text + card2_right * " " + "│" + "\n"

        number_of_empty_lines = abs(card1_height - card2_height)
        noel_up = number_of_empty_lines//2
        noel_down = number_of_empty_lines - noel_up
        ########################################

        top_line = "┌" + (card1_width - 2)* "─" + "┬" + (card2_width - 2) * "─" + "┐" + "\n"
        upper_lines = ("│" +(card1_width - 2)* " " + "│" + (card2_width - 2) * " " + "│" + "\n")*((card1_height - 3)//2)
        center_line1 = center_line
        lower_lines = upper_lines
        bottom_line = "└" + (card1_width - 2)* "─" + "┴" + (card2_width - 2) * "─" + "┘"

        print(top_line + upper_lines + center_line + lower_lines + bottom_line)
        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################


    elif card1_height > card2_height:
        
        ##############################
        # INSERT YOUR CODE HERE
        # Case 2
        # You can add as many new lines as you need.

        #lines that repeats for each condition.
        card1_horizontal = card1_width - 2 - len(card1_text)
        card1_left = card1_horizontal // 2
        card1_right = card1_horizontal - card1_left
        card2_horizontal = card2_width - 2 - len(card2_text)
        card2_left = card2_horizontal // 2
        card2_right = card2_horizontal - card2_left

        center_line = "│" + card1_left * " " + card1_text + card1_right * " " + "│" + card2_left * " " + card2_text + card2_right * " " + "│" + "\n"

        number_of_empty_lines = abs(card1_height - card2_height)
        noel_up = number_of_empty_lines//2
        noel_down = number_of_empty_lines - noel_up
        ########################################

        top_line_c1 = "┌" + (card1_width - 2)* "─" + "┐" + "\n"
        upper_lines_c1 = ("│" +(card1_width - 2)* " " + "│" + "\n") * noel_up
        upper_lines_c1_w_top_line_c2 = "│" +(card1_width - 2)* " " + "├" + (card2_width - 2) * "─" + "┐" + "\n"
        upper_lines_c1_and_c2 = ("│" +(card1_width - 2)* " " + "│" + (card2_width - 2) * " " + "│" + "\n") * ((card2_height - 3)//2)
        center_line2 = center_line
        lower_lines_c1_and_c2 = upper_lines_c1_and_c2
        lower_lines_c1_w_bottom_line_c2 = "│" +(card1_width - 2)* " " + "├" + (card2_width - 2) * "─" + "┘" + "\n"
        lower_lines_c1 = ("│" +(card1_width - 2)* " " + "│" + "\n") * noel_down
        bottom_line_c1 = "└" + (card1_width - 2)* "─" + "┘" + "\n"

        print(top_line_c1 + upper_lines_c1 + upper_lines_c1_w_top_line_c2 + upper_lines_c1_and_c2 + center_line2 + lower_lines_c1_and_c2 + 
        lower_lines_c1_w_bottom_line_c2 + lower_lines_c1 + bottom_line_c1)
       # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################


    else:
        
       ##############################
        # INSERT YOUR CODE HERE
        # Case 3
        # You can add as many new lines as you need.

        #lines that repeats for each condition.
        card1_horizontal = card1_width - 2 - len(card1_text)
        card1_left = card1_horizontal // 2
        card1_right = card1_horizontal - card1_left
        card2_horizontal = card2_width - 2 - len(card2_text)
        card2_left = card2_horizontal // 2
        card2_right = card2_horizontal - card2_left

        center_line = "│" + card1_left * " " + card1_text + card1_right * " " + "│" + card2_left * " " + card2_text + card2_right * " " + "│" + "\n"

        number_of_empty_lines = abs(card1_height - card2_height)
        noel_up = number_of_empty_lines//2
        noel_down = number_of_empty_lines - noel_up
        ########################################

        top_line_c2 = (card1_width - 1) * " " + "┌" + (card2_width - 2)* "─" + "┐" + "\n"
        upper_lines_c2 = ((card1_width - 1) * " " + ("│" +(card2_width - 2)* " " + "│" + "\n")) * noel_up
        upper_lines_c2_w_top_line_c1 ="┌" + (card1_width - 2)* "─" + "┤" + (card2_width - 2)* " " + "│" + "\n"
        upper_lines_c2_and_c1 = ("│" +(card1_width - 2)* " " + "│" + (card2_width - 2) * " " + "│" + "\n") * ((card1_height - 3)//2)
        center_line3 = center_line
        lower_lines_c2_and_c1 = upper_lines_c2_and_c1
        lower_lines_c2_w_bottom_line_c1 = "└" + (card1_width - 2)* "─" + "┤" + (card2_width - 2)* " " + "│" + "\n"
        lower_lines_c2 = ((card1_width - 1) * " " + ("│" +(card2_width - 2)* " " + "│" + "\n")) * noel_down
        bottom_line_c2 = (card1_width - 1) * " " + "└" + (card2_width - 2)* "─" + "┘"

        print(top_line_c2 + upper_lines_c2 + upper_lines_c2_w_top_line_c1 + upper_lines_c2_and_c1 + center_line3 + lower_lines_c2_and_c1 + 
        lower_lines_c2_w_bottom_line_c1 + lower_lines_c2 + bottom_line_c2)
       # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################
