def getScores():
    
    flag = True

    while flag:
        
        score_list = []    
        
        score_list.append(input("Enter your midterm score: "))
        score_list.append(input("Enter your final score: "))
        score_list +=     input("Enter your quiz scores (enter 4 scores by leaving space): ").split(" ")
        score_list +=     input("Enter your homework scores (enter 4 scores by leaving space): ").split(" ")
        
        if len(score_list) == 10:
            flag = False
            print("Scores are saved!")
        else:
            print("\nSomething doesn't add up... Please enter again, properly.\n")

    score_list = list(map(int, score_list))  # Turns each element to integer in the list.

    return score_list

# This function gets the scores from user, checks it if its valid or not and returns it as a list.


def calculateScores(calculate_list):
    qs = (calculate_list[2] + calculate_list[3] + calculate_list[4] + calculate_list[5])/4
    hs = (calculate_list[6] + calculate_list[7] + calculate_list[8] + calculate_list[9])/4
    
    total_score = calculate_list[0] * 0.25 + qs * 0.20 + hs * 0.20 + calculate_list[1] * 0.35

    return total_score

# This function calculates the total score. For this program it is designed to work with the list we get from getScores() function.


def getAbsenceRate():
    absence_count = int(input("Enter the number of absences: "))
    absence_rate = absence_count/14
    return absence_rate

# This function calculates the absence rate by an input.


def showLetter(abs_rate, total_score):
    
    if abs_rate > 0.25:
        return "NA"
    
    if 90 <= total_score <= 100:
        return "AA"
    elif 85 <= total_score < 90:
        return "BA"
    elif 80 <= total_score < 85:
        return "BB"
    elif 75 <= total_score < 80:
        return "CB"
    elif 70 <= total_score < 75:
        return "CC"
    elif 65 <= total_score < 70:
        return "DC"
    elif 60 <= total_score < 65:
        return "DD"
    elif 50 <= total_score < 60:
        return "FD"
    elif 0 <= total_score < 50:
        return "FF"

# This function returns the grade by letter according to overall score.


def main():
    scoreList = getScores()
    print()
    absenceRate = getAbsenceRate()
    totalScore = calculateScores(scoreList)
    print()
    result = showLetter(absenceRate, totalScore)
    print("Your grade is:", result)
    return None

# This is the main program where everything take place.


main()