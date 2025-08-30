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

for question_num in range(len(Questions_List)) : # 0 1 2 3 4
    print("************************")
    print(Questions_List[question_num]["text"])
    for i in options[question_num] :
        print(i)
