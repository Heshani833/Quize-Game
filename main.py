print("Welcome to the Quiz Game!")

Questions_List = [

    {"text" : "Which data structure uses FIFO (First In, First Out) principle?", "answer": "B"},
    {"text" : "Which of the following is the best data structure to implement recursion?", "answer": "C"},
    {"text" : "What is the time complexity of searching in a balanced binary search tree (BST)?", "answer": "B"},
    {"text" : "Which data structure is used in Breadth First Search (BFS) algorithm?", "answer": "B"},
    {"text" : "Which of the following is a non-linear data structure?", "answer": "D"}

]

options = [
    ["A) Stack","B) Queue","C) Tree","D) Graph"],
    ["A) Array","B) Queue","C) Stack","D) Linked List"],
    ["A) O(1)","B) O(log n)","C) O(n)","D) O(n log n)"],
    ["A) Stack","B) Queue","C) Linked List","D) Heap"],
    ["A) Array","B) Stack","C) Queue","D) Graph"]

]

score = 0

def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(Questions_List)) : # 0 1 2 3 4
    print("************************")
    print(Questions_List[question_num]["text"])
    for i in options[question_num] :
        print(i)

    guess = input("Enter (A/B/C/D) : ").upper()  
    is_correct = check_answer(guess, Questions_List[question_num]["answer"])
    if is_correct:
        print("You got it right!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {Questions_List[question_num]['answer']}")

print("************************")
print(f"You have given {score} correct answers.")
print(f"Your score is {score / len(Questions_List) * 100}%")
print("Thank you for playing the Quiz Game!")