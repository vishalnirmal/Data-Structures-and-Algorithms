# DOUBLY LINKED LIST

The class DLL in DoublyLinkedList.py implements all the basic operations of a Doubly Linked List. A doubly linked list is a data structure where each node has a value associated to it and two pointers previous and next. The advantage of a doubly linked list is that, given a node in the list, we con navigate in both directions.

Functions of DLL:
* ### traverseList(): 
	> Is used to print the list

* ### insertAtBeginning(data): 
	#### arguments:
		data: value for the node you want to add
	> For adding a new node at the front of the linked list

* ### insertAtEnd(data):
	#### arguments:
		data: value for the node you want to add
	> For adding a new node at the end of the linked list

* ### insert(data, pos):
	#### arguments:
		data: value for the node you want to add
		pos: position at which you want to add the node
	> For adding a new node at any position 'pos' in the linked list

* ### deleteAtBeginning():
	> Delete the first node of the linked list

* ### deleteAtEnd():
	> Delete the last node of the linked list

* ### delete(pos):
	#### arguments: 
		pos: position at which you want to delete a node
	> Delete the node at position 'pos' of the linked list

* ### addNodes(arr):
	#### arguments:
		arr: array, tupple, set or any iterable object whose data you want to add to the linked list
	> For adding all the elements of 'arr' to the list

* ### get(pos):
	#### arguments:
		pos: position of the node whose value you want to fetch
	> For fetching the value of the node at position 'pos' in the linked list

* ### search(data):
	#### arguments:
		data: value whose position you want to know
	> For getting the postion of the 'data' from the linked list

* ### count():
	> For returning no. of nodes in the linked list

* ### reverseList():
	> For reversing the linked list