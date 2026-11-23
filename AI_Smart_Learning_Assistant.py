
import tkinter as tk
from tkinter import messagebox, simpledialog

# PROFESSIONAL BLUE AND WHITE THEME
BG_COLOR = "#F4F7FB"
HEADER_COLOR = "#17365D"
BUTTON_COLOR = "#2563A6"
CARD_COLOR = "#FFFFFF"
TEXT_COLOR = "#263445"
LIGHT_TEXT = "#718096"


# MAIN WINDOW
window = tk.Tk()
window.title("AI Smart Learning Assistant")
window.geometry("760x620")
window.config(bg=BG_COLOR)

# STUDENT NAME
student_name = ""


# LESSONS
lessons = {
    "physics": """Newton's Laws of Motion explain how objects move and how forces affect their motion.

Newton's First Law:
An object remains at rest or in uniform motion unless an external force acts on it.

Newton's Second Law:
Force = Mass x Acceleration (F = ma).

Newton's Third Law:
Every action has an equal and opposite reaction.

Example: Pushing a trolley or kicking a ball.""",

    "english": """Parts of Speech are the basic categories of words used in English grammar.

There are eight main parts of speech:

1. Noun: Names a person, place, animal, or thing.
2. Pronoun: Replaces a noun.
3. Verb: Shows an action.
4. Adjective: Describes a noun.
5. Adverb: Describes a verb.
6. Preposition: Shows position.
7. Conjunction: Joins words or sentences.
8. Interjection: Expresses emotions.

Examples: Ali, He, Run, Beautiful, Quickly, In, And, Wow.""",

    "mathematics": """A quadratic equation is a polynomial equation of degree two.

Standard Form:
ax^2 + bx + c = 0

Here, a, b, and c are constants and a is not equal to zero.

Methods:
1. Factorization
2. Completing the Square
3. Quadratic Formula

Quadratic Formula:
x = (-b +/- sqrt(b^2 - 4ac)) / 2a

Example:
x^2 - 5x + 6 = 0

Solutions:
x = 2 and x = 3.""",

    "computer": """Python is a high-level, easy-to-learn programming language.

Python is used for software development, artificial intelligence, data science, and automation.

Important Python Concepts:

1. print() displays output.
2. input() takes information from the user.
3. Variables store data.
4. Loops repeat instructions.
5. If and else help programs make decisions.
6. Lists store multiple values.
7. Functions perform specific tasks.

Python is widely used by beginners and professional programmers."""
}


# QUIZ QUESTIONS
quiz_questions = {
    "1": {
        "name": "Physics",
        "questions": [
            (
                "SI unit of force?",
                "A. Joule  B. Newton  C. Watt",
                "B",
                "Force is measured in Newton. Joule is the unit of work and energy, while Watt is the unit of power."
            ),

            (
                "Which law is also called the law of inertia?",
                "A. First Law  B. Second Law  C. Third Law",
                "A",
                "Newton's First Law is called the law of inertia because an object resists changes in its state of motion."
            ),

            (
                "SI unit of mass?",
                "A. Newton  B. Joule  C. Kilogram",
                "C",
                "Kilogram is the SI unit of mass. Newton measures force and Joule measures energy."
            )
        ]
    },

    "2": {
        "name": "English",
        "questions": [
            (
                "Which part of speech names a person, place, or thing?",
                "A. Noun  B. Verb  C. Adjective",
                "A",
                "A Noun is the name of a person, place, animal, or thing. Examples include Ali, School, and Book."
            ),

            (
                "Which part of speech describes an action?",
                "A. Pronoun  B. Verb  C. Noun",
                "B",
                "A Verb describes an action or state. Examples include Run, Eat, Write, and Sleep."
            ),

            (
                "Which word is an adjective?",
                "A. Quickly  B. Run  C. Beautiful",
                "C",
                "Beautiful is an adjective because it describes a noun. Quickly is an adverb and Run is a verb."
            )
        ]
    },

    "3": {
        "name": "Mathematics",
        "questions": [
            (
                "What is 5 x 5?",
                "A. 20  B. 25  C. 30",
                "B",
                "5 multiplied by 5 equals 25."
            ),

            (
                "Square root of 81?",
                "A. 9  B. 8  C. 7",
                "A",
                "9 is the square root of 81 because 9 multiplied by 9 equals 81."
            ),

            (
                "What is 2 + 8?",
                "A. 12  B. 11  C. 10",
                "C",
                "Adding 2 and 8 gives 10."
            )
        ]
    },

    "4": {
        "name": "Computer Science",
        "questions": [
            (
                "Which language is used in this project?",
                "A. Python  B. HTML  C. CSS",
                "A",
                "Python is the programming language used to develop this project."
            ),

            (
                "Which symbol is used for comments in Python?",
                "A. //  B. #  C. **",
                "B",
                "The hash symbol (#) is used to write comments in Python."
            ),

            (
                "Which function displays output?",
                "A. input()  B. printtext()  C. print()",
                "C",
                "The print() function displays output on the screen."
            )
        ]
    }
}


# STUDY PLANS
study_plans = {
    "physics": """Physics Study Plan:

1. Revise Physics Concepts - 30 Minutes
2. Learn Important Formulas - 30 Minutes
3. Solve Numerical Problems - 1 Hour""",

    "english": """English Study Plan:

1. Learn English Grammar - 30 Minutes
2. Practice Vocabulary - 30 Minutes
3. Practice Writing and Reading - 1 Hour""",

    "mathematics": """Mathematics Study Plan:

1. Revise Mathematical Formulas - 30 Minutes
2. Understand Mathematical Concepts - 30 Minutes
3. Solve Practice Questions - 1 Hour""",

    "maths": """Mathematics Study Plan:

1. Revise Mathematical Formulas - 30 Minutes
2. Understand Mathematical Concepts - 30 Minutes
3. Solve Practice Questions - 1 Hour""",

    "computer": """Computer Science Study Plan:

1. Learn Programming Concepts - 30 Minutes
2. Practice Python Coding - 30 Minutes
3. Solve Programming Questions - 1 Hour""",

    "computer science": """Computer Science Study Plan:

1. Learn Programming Concepts - 30 Minutes
2. Practice Python Coding - 30 Minutes
3. Solve Programming Questions - 1 Hour"""
}


# CLEAR WINDOW
def clear_window():

    for widget in window.winfo_children():
        widget.destroy()


# SHOW MAIN MENU
def show_main_menu():

    clear_window()

    heading = tk.Label(
        window,
        text="AI SMART LEARNING ASSISTANT",
        font=("Arial", 21, "bold"),
        bg=BG_COLOR,
        fg=HEADER_COLOR
    )
    heading.pack(pady=20)

    welcome = tk.Label(
        window,
        text="Welcome " + student_name + "!",
        font=("Arial", 16, "bold"),
        bg=BG_COLOR,
        fg=BUTTON_COLOR
    )
    welcome.pack(pady=10)

    # LEARN BUTTON
    learn_button = tk.Button(
        window,
        text="1. Learn a Topic",
        font=("Arial", 13, "bold"),
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=HEADER_COLOR,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=28,
        command=learn_topic
    )
    learn_button.pack(pady=12, ipady=5)

    # QUIZ BUTTON
    quiz_button = tk.Button(
        window,
        text="2. Take a Smart Quiz",
        font=("Arial", 13, "bold"),
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=HEADER_COLOR,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=28,
        command=smart_quiz
    )
    quiz_button.pack(pady=12, ipady=5)

    # STUDY PLAN BUTTON
    plan_button = tk.Button(
        window,
        text="3. Create Study Plan",
        font=("Arial", 13, "bold"),
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=HEADER_COLOR,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=28,
        command=study_plan
    )
    plan_button.pack(pady=12, ipady=5)

    # EXIT BUTTON
    exit_button = tk.Button(
        window,
        text="4. Exit",
        font=("Arial", 13, "bold"),
        bg=HEADER_COLOR,
        fg="white",
        activebackground=HEADER_COLOR,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=28,
        command=exit_program
    )
    exit_button.pack(pady=12, ipady=5)

    footer = tk.Label(
        window,
        text="Keep Learning, Keep Growing!",
        font=("Arial", 11, "italic"),
        bg=BG_COLOR,
        fg=LIGHT_TEXT
    )
    footer.pack(pady=25)


# LEARN A TOPIC
def learn_topic():

    topic = simpledialog.askstring(
        "Learn a Topic",
        "Available Topics:\n\n"
        "1. Physics - Newton's Laws\n"
        "2. English - Parts of Speech\n"
        "3. Mathematics - Quadratic Equation\n"
        "4. Computer - Python\n\n"
        "Enter topic name:"
    )

    if topic is None:
        return

    topic = topic.lower().strip()

    if topic in lessons:

        messagebox.showinfo(
            "Simple Explanation",
            lessons[topic]
        )

    else:

        messagebox.showerror(
            "Invalid Topic",
            "Topic not available. Please try again."
        )


# SMART QUIZ
def smart_quiz():

    subject = simpledialog.askstring(
        "Smart Quiz",
        "Select Your Subject:\n\n"
        "1. Physics\n"
        "2. English\n"
        "3. Mathematics\n"
        "4. Computer Science\n\n"
        "Enter subject number:"
    )

    if subject is None:
        return

    subject = subject.strip()

    if subject not in quiz_questions:

        messagebox.showerror(
            "Invalid Subject",
            "Please select a subject between 1 and 4."
        )
        return

    subject_name = quiz_questions[subject]["name"]
    questions = quiz_questions[subject]["questions"]

    score = 0

    # ASK QUESTIONS
    for question, options, correct, explanation in questions:

        answer = simpledialog.askstring(
            subject_name + " Quiz",
            question + "\n\n" + options +
            "\n\nEnter Your Answer (A/B/C):"
        )

        if answer is None:
            return

        answer = answer.upper().strip()

        if answer == correct:

            score = score + 1

            messagebox.showinfo(
                "Correct Answer",
                "Correct Answer!\n\nExcellent Work!"
            )

        else:

            messagebox.showinfo(
                "Wrong Answer",
                "Wrong Answer!\n\n"
                "Correct Answer: " + correct +
                "\n\nSMART MISTAKE EXPLANATION\n\n" +
                "Why is this correct?\n" + explanation +
                "\n\nSmart Tip: Remember this concept for your next quiz!"
            )

    # PERFORMANCE REPORT
    percentage = (score / len(questions)) * 100

    wrong_answers = len(questions) - score

    if percentage == 100:

        performance = "Excellent!"
        suggestion = "Try advanced questions."

    elif percentage >= 60:

        performance = "Good!"
        suggestion = "Practice more MCQs."

    else:

        performance = "Needs Improvement!"
        suggestion = "Revise this subject."

    # SMART RECOMMENDATION
    if percentage < 60:

        recommendation = (
            "Your weak subject is: " + subject_name +
            "\nRecommended Study Time: 2 Hours Daily" +
            "\nTip: Revise concepts and solve practice questions."
        )

    else:

        recommendation = (
            "You are doing well in " + subject_name +
            "\nRecommended Study Time: 1 Hour Daily" +
            "\nTip: Continue regular revision."
        )

    report = (
        "YOUR PERFORMANCE REPORT\n\n"
        "Student: " + student_name +
        "\nSubject: " + subject_name +
        "\nMarks: " + str(score) + " / " + str(len(questions)) +
        "\nWrong Answers: " + str(wrong_answers) +
        "\nPercentage: " + str(round(percentage, 2)) + "%" +
        "\n\nPerformance: " + performance +
        "\nAI Suggestion: " + suggestion +
        "\n\nSMART RECOMMENDATION\n\n" + recommendation
    )

    messagebox.showinfo(
        "Performance Report",
        report
    )


# PERSONALIZED STUDY PLAN
def study_plan():

    weak = simpledialog.askstring(
        "Personalized Study Plan",
        "Available Subjects:\n\n"
        "1. Physics\n"
        "2. English\n"
        "3. Mathematics\n"
        "4. Computer Science\n\n"
        "Enter your weak subject:"
    )

    if weak is None:
        return

    weak = weak.lower().strip()

    if weak in study_plans:

        messagebox.showinfo(
            "Your Study Plan",
            study_plans[weak] +
            "\n\nAI Tip: Focus on your selected subject!"
        )

    else:

        messagebox.showerror(
            "Invalid Subject",
            "Subject not available! Please enter a valid subject name."
        )


# EXIT PROGRAM
def exit_program():

    answer = messagebox.askyesno(
        "Exit Program",
        "Are you sure you want to exit?"
    )

    if answer:

        messagebox.showinfo(
            "Thank You",
            "Thank you for using AI Smart Learning Assistant!\n\n"
            "Keep Learning, Keep Growing!\n\n"
            "Program Closed Successfully!"
        )

        window.destroy()


# WELCOME SCREEN
heading = tk.Label(
    window,
    text="AI SMART LEARNING ASSISTANT",
    font=("Arial", 22, "bold"),
    bg=BG_COLOR,
    fg=HEADER_COLOR
)
heading.pack(pady=45)

student_label = tk.Label(
    window,
    text="BY NEHA MALIK  |  PH-25",
    font=("Arial", 14, "bold"),
    bg=BG_COLOR,
    fg=BUTTON_COLOR
)
student_label.pack(pady=10)

name_label = tk.Label(
    window,
    text="Enter Student Name:",
    font=("Arial", 13),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
name_label.pack(pady=15)

name_entry = tk.Entry(
    window,
    font=("Arial", 13),
    width=25
)
name_entry.pack(pady=10, ipady=6)


# START BUTTON
def start_program():

    global student_name

    student_name = name_entry.get().strip()

    if student_name == "":

        messagebox.showwarning(
            "Name Required",
            "Please enter your name first."
        )

    else:

        show_main_menu()


start_button = tk.Button(
    window,
    text="Start Learning",
    font=("Arial", 13, "bold"),
    bg=BUTTON_COLOR,
    fg="white",
    activebackground=HEADER_COLOR,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=22,
    command=start_program
)
start_button.pack(pady=30, ipady=5)


# RUN GUI
window.mainloop()
