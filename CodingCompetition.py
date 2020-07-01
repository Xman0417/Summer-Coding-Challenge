def test():
    #This is how the program measures based on the answers.
    score = 0
    #Here an option could be if more tests were added in the future like for some anxiety disorders or bipolar disorder.
    print("During these tough times, your mental health may be worsening and you may develop depression.")
    enter = input("Would you like to take a short test to see if you have developed or are developing depression? Enter 'yes' or 'no' ")
    if enter == "yes":
        print("Okay. Respond either 'yes' or 'no' to these question")
        #these variable names mean q(question) one) it will always follow this trend.
        qone = input("Do you feel sad often? ")
        if qone == "yes":
            score += 1
        qtwo = input("Do you feel hopeless or 'empty' often? ")
        if qtwo == "yes":
            score += 2
        qthree = input("Do you have trouble concentrating and remembering details at times? ")
        if qthree == "yes":
            score += 1
        qfour = input("Do you experience insomnia or trouble sleeping at times? ")
        if qfour == "yes":
            score += 1
        qfive = input("Do you often have feelings of guilt and hopelessness? ")
        if qfive == "yes":
            score += 2
        qsix = input("Do mental illnesses such as depression run in your family? ")
        if qsix == "yes":
            score += 2
        qseven = input("Have you engaged in reckless behavior to 'escape' from your thoughts? ")
        if qseven == "yes":
            score += 3
        qeight = input("Have you experienced a lack of energy over the last few months? ")
        if qeight == "yes":
            score += 2
        qnine = input("Have you experienced a loss of interest in daily activities? ")
        if qnine == "yes":
            score += 3
        qten = input("Do you think you may have depression? ")
        if qten == "yes":
            score += 9
        print("While these tests are not a definite answer, these can give a decent idea whether or not you have depression.")
        if score >= 12:
            print("You may have depression. However, there is a chance that you do not and you should talk to a professional to confirm or deny this.")
        elif score >= 8:
            print("You could have depression. There is a decent chance you do not, however, and you should talk to a professional if you believe you need it.")
        elif score >= 4:
            print("It is unlikely you have depression. However, there is a very low chance that you do, and you could talk to a professional if you feel that you need it.")
        else:
            print("You probably do not have depression. You could always talk to a doctor or a therapist just in case, but you likely do not have to.")


        input("Press enter to exit the test.")
    else:
        input("You either said no, or had a typo. Run this program again if you change your mind. Press enter to continue.")
        


test()
