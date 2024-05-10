# Programmer: Rizon Takabe
# Class: CS 240
# Date: 4/11/23
# Assignment: Linked List
# 
class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

def main():
    array_to_linked_list()
    read_current_list()

def array_to_linked_list():
    head = None
    numbers2txt = read_file("numbers-2.txt")
    for num in numbers2txt:
        newNode = linkedListNode(str(num))
        if head is None:
            head = newNode  # If there is no nodes yet, set the new node as the head
        else:
            currentNode = head
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode

    currentNode = head

def read_current_list():
    while True:
        print(currentNode.value + " -> ", end="")
        if currentNode.nextNode is None:
            print("None")
            break
        currentNode = currentNode.nextNode

def read_file(file_name):
    arr = []
    with open(file_name) as file:
        for line in file:
            arr.append(int(line))
    return arr

main()