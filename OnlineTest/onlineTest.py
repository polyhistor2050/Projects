def check_answer(question, answer):
    global marks
    notAnswered = True
    attempt = 0
    while notAnswered and attempt < 1:
        if question.lower() == answer.lower():
            print("Correct answer!")
            marks = marks + 10
            notAnswered = False
        else:
            if attempt < 2:
                wrong = input("Wrong answer!")
                attempt = attempt + 1
    if attempt == 2:
        print("The correct answer is " + answer)


marks = 0

print("Welcome to our online exams system.\n\
This is Networking exam \n\
Duration:2hr")

question1 = input("USB-C ports and cables are compatible with Apple Lightning ports and cables, \
True or false? ")
check_answer(question1, "false")

question2 = input("What type of file system is usually used for the Linux boot partition? ")
check_answer(question2, "ext")

question3 = input("Which Linux command allows a user to run a specific command or program \
with superuser/root privileges? ")
check_answer(question3, "sudo")

question4 = input("Which file contains the list of user accounts created on Linux? ")
check_answer(question4, "/etc/passwd")

question5 = input("What command would you normally need to run in order to access the contents of a USB memory \
stick inserted into Linux? ")
check_answer(question5, "mount")

question6 = input("What is the equivalent of Explorer in macOS? ")
check_answer(question6, "The Finder")

question7 = input("What is the name of Apple's multiple desktop management feature? ")
check_answer(question7, "Mission Control")

question8 = input("Which tool is used to verify file system integrity in Linux? ")
check_answer(question8, "fsck")

question9 = input("What Windows utility would you use to back up data files in Windows 10? ")
check_answer(question9, "File History")

question10 = input("What is the name of Apple's backup software for macOS? ")
check_answer(question10, "Time Machine")

print("Your result is " + str(marks) + " out of 100 marks")
