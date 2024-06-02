mark = 0
skipped_questions = 0
correct_questions = 0
wrong_questions = 0
Questions = (   (("Q1. Which of the following is not a state of matter?", "(A) Solid", "(B) Liquid", "(C) Gas","(D) Plasma", "(E) Skip", "(F) Submit", "(D) Plasma"), ("Q2. What is the study of living organisms called?", "(A) Chemistry", "(B) Biology", "(C) Physics", "(D) Geology", "(E) Skip", "(F) Submit", "(B) Biology"), ("(E) Skip", "(F) Submit", "(C) Red"), ("Q4. What is the process by which plants use sunlight to convert carbon dioxide and water into oxygen and glucose called?","(A) Respiration", "(B) Fermentation", "(C) Photosynthesis", "(D) Digestion", "(E) Skip",  "(F) Submit", "(C) Photosynthesis"), ("Q5. Which of the following is not a type of energy?", "(A) Thermal", "(B) Kinetic", "(C) Potential","(D) Sound", "(E) Skip", "(F) Submit", "(D) Sound"), ("Q6. Which of the following is a common polysaccharide found in plants?", "(A) Glucose","(B) Fructose", "(C) Starch", "(D) Sucrose", "(E) Skip", "(F) Submit", "(C) Starch"), ("Q7. What is the study of matter and its properties called?", "(A) Chemistry", "(B) Physics","(C) Biology", "(D) Geology", "(E) Skip", "(F) Submit", "(A) Chemistry"), ("Q8. Which of the following is not a part of an atom?", "(A) Proton", "(B) Neutron", "(C) Electron", "(D) Nucleus", "(E) Skip", "(F) Submit", "(D) Nucleus"), ("Q9. Which of the following is a homophone for 'their'?", "(A) There", "(B) They're", "(C) Them","(D) Themselves", "(E) Skip", "(F) Submit", "(A) There"), ("Q10. What is the force that pulls objects towards the center of the Earth called?", "(A) Gravity","(B) Magnetism", "(C) Friction", "(D) Tension", "(E) Skip", "(F) Submit", "(A) Gravity")),
             (("Q1. What is the value of pi (π)?", "(A) 3.14", "(B) 2.72", "(C) 1.41", "(D) 1.73", "(E) Skip","(F) Submit", "(A) 3.14"), ("Q2. Which of the following is a vector quantity?", "(A) Distance", "(B) Speed", "(C) Time","(D) Velocity", "(E) Skip", "(F) Submit", "(D) Velocity"), ("Q3. Which element has the atomic number 6?", "(A) Carbon", "(B) Nitrogen", "(C) Oxygen","(D) Hydrogen", "(E) Skip", "(F) Submit", "(A) Carbon"), ("Q4. Which of the following is a non-metal?", "(A) Sodium", "(B) Chlorine", "(C) Iron","(D) Calcium", "(E) Skip", "(F) Submit", "(B) Chlorine"), ("Q5. What is the past participle of the verb 'swim'?", "(A) Swam", "(B) Swum", "(C) Swimmed","(D) Swimming", "(E) Skip", "(F) Submit", "(B) Swum"), ("Q6. What is the square root of 16?", "(A) 2", "(B) 4", "(C) 6", "(D) 8", "(E) Skip", "(F) Submit","(B) 4"), ("Q7. What is the formula for water?", "(A) NaCl", "(B) H2SO4", "(C) H2O", "(D) CO2", "(E) Skip","(F) Submit", "(C) H2O"), ("Q8. Which of the following is an example of potential energy?", "(A) A moving car","(B) A burning candle", "(C) A stretched rubber band", "(D) A falling rock", "(E) Skip","(F) Submit", "(C) A stretched rubber band"), ("Q9. Which of the following is not a part of an atom?", "(A) Proton", "(B) Neutron","(C) Electron", "(D) Ion", "(E) Skip", "(F) Submit", "(D) Ion"), ( "Q10. What is the correct way to write the following sentence: i never knew it was you","(A) I never knew it was you.", "(B) I never knew it was you?", "(C) I never knew it was you!","(D) I never knew it was you...", "(E) Skip", "(F) Submit", "(A) I never knew it was you.")),
             (("Q1. What does RAM stand for in a computer?", "(A) Read-Only Memory", "(B) Random Access Memory","(C) Central Processing Unit", "(D) Graphics Processing Unit", "(E) Skip", "(F) Submit","(B) Random Access Memory"), ("Q2. Which programming language is often used for developing mobile apps?", "(A) Python", "(B) Java","(C) C#", "(D) Ruby", "(E) Skip", "(F) Submit", "(B) Java"), ("Q3. What is the process of converting source code into machine code called?", "(A) Compiling","(B) Debugging", "(C) Interpreting", "(D) Coding", "(E) Skip", "(F) Submit", "(A) Compiling"), (     "Q4. Which of the following is not an input device?", "(A) Mouse", "(B) Keyboard", "(C) Monitor","(D) Scanner", "(E) Skip", "(F) Submit", "(C) Monitor"), ("Q5. Which of the following is a programming language?", "(A) HTML", "(B) CSS", "(C) JavaScript","(D) SQL", "(E) Skip", "(F) Submit", "(C) JavaScript"), ("Q6. What is the formula for calculating the area of a circle?", "(A) pi x r^2", "(B) 2 x pi x r","(C) 2 x r", "(D) r^2", "(E) Skip", "(F) Submit", "(A) pi x r^2"), ("Q7. Which of the following is not a type of energy?", "(A) Thermal", "(B) Kinetic", "(C) Potential","(D) Static", "(E) Skip", "(F) Submit", "(D) Static"), ("Q8. Which of the following is not a metal?", "(A) Iron", "(B) Copper", "(C) Lead", "(D) Oxygen","(E) Skip", "(F) Submit", "(D) Oxygen"), ("Q9. Which of the following is an example of a chemical change?", "(A) Melting ice","(B) Boiling water", "(C) Burning wood", "(D) Dissolving sugar in water", "(E) Skip", "(F) Submit","(C) Burning wood"), ("Q10. Which of the following is a synonym of 'eloquent'?", "(A) Inarticulate", "(B) Fluent","(C) Mute", "(D) Silent", "(E) Skip", "(F) Submit", "(B) Fluent")))
skip = []
attempted_questions = 0




def sk():
    global skip, skipped_questions, correct_questions, wrong_questions, attempted_questions, mark
    for i in skip:
        print(q[i][0])
        for j in range(1, 7):
            print(q[i][j])
        inp = input("Choose Option: ")
        if inp == q[i][7][1]:
            mark += 4
            correct_questions += 1
            attempted_questions += 1
            skipped_questions -= 1
            if skipped_questions == 0:
                break
        elif inp == "F":
            if len(skip) != 0:
                has = input("Do You Want to Attempt Skipped Questions? (Y/N)")
                if has == "Y":
                    sk()
                else:
                    break
            else:
                break
        elif inp == "E":
            continue
        else:
            wrong_questions += 1
            mark -= 1
            attempted_questions += 1
            skipped_questions -= 1
            if skipped_questions == 0:
                break
def result():
    global skipped_questions, correct_questions, wrong_questions
    print(f"Correct Answers: {correct_questions}")
    print(f"Wrong Answers: {wrong_questions}")
    print(f"Skipped Questions: {skipped_questions}")


print("\t --------ECAT EXAM--------")
user_input = input("Choose Your Discipline(Pre-Eng[pe],Pre-Med[pm],ICS[ics]: ")
if user_input == "pe":
    q = Questions[1]
elif user_input == "pm":
    q = Questions[0]
elif user_input == "ics":
    q = Questions[2]
for i in range(len(q)):
    print(q[i][0])
    for j in range(1, 7):
        print(q[i][j])
    inp = input("Choose Option: ")

    if inp == q[i][7][1]:
        mark += 4
        correct_questions += 1
        attempted_questions += 1
        if len(skip) != 0 and q[i] == q[len(q)-1]:
            ask = input("Do You Want to Attempt Skipped Questions? (Y/N)")
            if ask == "Y":
                sk()
                break
            else:
                break
        else:
            pass
    elif inp == "F":
        if len(skip) != 0:
            ask = input("Do You Want to Attempt Skipped Questions? (Y/N)")
            if ask == "Y":
                sk()
                break
            else:
                break
        else:
            break
    elif inp == "E":
        skipped_questions += 1
        skip.append(i)
        if len(skip) != 0 and q[i] == q[len(q)-1]:
            ask = input("Do You Want to Attempt Skipped Questions? (Y/N)")
            if ask == "Y":
                sk()
                break
            else:
                break
        else:
            pass
    else:
        wrong_questions += 1
        mark -= 1
        attempted_questions += 1
        if len(skip) != 0 and q[i] == q[len(q)-1]:
            ask = input("Do You Want to Attempt Skipped Questions? (Y/N)")
            if ask == "Y":
                sk()
                break
            else:
                break
        else:
            pass

per = (mark/40) * 100
print()
result()
if per >= 50:
    print("Eligible")
else:
    print("Ineligible. Please Try Again")
