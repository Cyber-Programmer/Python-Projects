ECAT Exam Quiz Application
This Python script is a console-based quiz application designed to simulate the ECAT (Engineering College Admission Test) exam. The application presents a series of multiple-choice questions to the user, records their answers, and calculates their score based on correct and incorrect responses.

Key Features
Discipline Selection:

The user can choose their discipline: Pre-Engineering, Pre-Medical, or ICS (Intermediate in Computer Science). Based on the selection, the relevant set of questions is loaded.
Question Presentation:

The script iterates through a predefined set of questions, displaying each question with its multiple-choice answers. Each question also includes options to skip ((E) Skip) or submit ((F) Submit).
Answer Handling:

User inputs are compared with the correct answer for each question. Correct answers add points, while incorrect answers deduct points. Skipped questions are tracked for later review.
Score Calculation:

Correct answers add 4 points.
Incorrect answers deduct 1 point.
Skipped questions are revisited at the end if the user opts to attempt them again.
Skipped Questions:

Skipped questions are stored in a list and presented to the user at the end of the quiz if they choose to attempt them again.
Result Display:

At the end of the quiz, the user's performance is summarized, showing the number of correct, wrong, and skipped questions.
The user's percentage score is calculated and displayed.
Based on the percentage score, the user is informed whether they are eligible or ineligible.
Usage
Start the Quiz:

Run the script and choose your discipline by entering pe for Pre-Engineering, pm for Pre-Medical, or ics for ICS.
Answer Questions:

Enter the corresponding letter (A, B, C, D) for your chosen answer.
To skip a question, enter E.
To submit and end the quiz, enter F.
Review Skipped Questions:

After completing all questions, if there are skipped questions, you will be prompted to attempt them again.
View Results:

The script will display your total correct answers, wrong answers, skipped questions, and your eligibility based on your score.
