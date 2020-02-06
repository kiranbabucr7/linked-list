"""
PROGRAM TO DO THE LINKED LIST OPRATIONS
@author:Kiran Babu
Created_Date:6 feb 2020

"""

"""
Class node is used to create a node with specipic value
(By Default the value is None)
and its pointer pointing to NULL or None. 
"""
class node:
	def __init__(self,data=None):#Constructor to create a node
		self.data=data
		self.next=None
"""
Class linked_list is used to create a linked list.
whenever an instace of linked_list is instantiated 
a node called head node is created
(By Default the value of head is None and its pointer is pointing to).
class linked list provides all the functionalities such as
1)Display 2)show_lenth 3)insertion at head 4)insertion at tail 
5)insert on an index 6)Deletion at head 7)deletion at tail 
8)deleteion on an index .
"""
class linked_list:
	def __init__(self):
		self.head=node()
	"""
	Displays All The Nodes in the linked list.
	"""
	def display(self):
		if self.length()==0:#checks whether the list is empty or not.
			print "No Elements in the linked list\n"
			return#returning to main exicution.
		l=[]#creating a Null list to store values of the nodes.
		cur=self.head#assigning the current node as head.
		while cur.next!=None:#itreating from head to the last node.
			cur=cur.next#changing current node to the next node.
			l.append(cur.data)#appending the value of the current node to the list.
		print l#printing the list of vales of the nodes in exact order.
	"""
	Displays The length of the linked list
	"""
	def length(self):
		length=0#initilizing length to 0.
		cur=self.head#assigning the current node as head.
		while cur.next!=None:#itreating from head to the last node.
			cur=cur.next#changing current node to the next node.
			length+=1#incrimenting the value of length.
		return length#returning length.
	"""
	push is used to add or push a node on the head of the linked list.
	data is the parameter which is stored in the node.
	"""
	def push(self,data):
		new_node=node(data)#creating a node with the value data and its pointer pointing to None.
		new_node.next=self.head.next#changing pointer from null to the 1st element of the linked list.
		self.head.next=new_node#changing pointer of head to the newly added element of the linked list.
	"""
	append is used to add a node at the end or tai of the linked list.
	data is the parameter which is stored in the node.
	"""
	def append(self,data):
		new_node=node(data)#creating a node with the value data and its pointer pointing to None.
		cur=self.head#assigning the current node as head.
		while cur.next!=None:#itreating from head to the last node.
			cur=cur.next#changing current node to the next node.
		cur.next=new_node#adding new node to last node of the linked list.
	""" 
	given a position and data append_any_position will add a node with given data at the given position.
	"""
	def append_any_position(self,position,data):
		if position>self.length() or position<0:#checking wheather the given given position is valid or not.
			return False#if not valid returning false to main function
		new_node=node(data)#creating a node with the value data and its pointer pointing to None.
		cur=self.head#assigning the current node as head.
		for i in range(position+1):#itrating to the get the required node with given position
			last_node=cur#setting previous node as current node
			cur=cur.next#changing current node to the next node.
		last_node.next=new_node#setting the pointer of the previous node at the given position pointing to the new node to added.
		new_node.next=cur#setting the pointer of the new node pointing to the current node(which is actually the next node to the last node and new node is added in between them).
		return True#returing true to the main function
	"""
	Delete_snode will delete the node at head
	"""
	def delete_snode(self):
		if self.length()==0:#checking wheather the linked list is empty or not
			print "No Elements in the linked list\n"
			return#returning to main method
		temp_node=node()#creating a temp node so that the value of the deleted node can be returned(intsted of writing those 3 line u can write self.head=self.head.next))
		temp_node=self.head.next#assigning node to be deleted to the temp node
		self.head.next=temp_node.next#making head pointer to point the next node(node which is ponited by the deleted node).
		return temp_node.data#returning the deleted data to the main method
	"""
	Delete_Lnode will delete the last node
	"""
	def delete_lnode(self):
		if self.length()==0:#checking wheather the linked list id empty or not
			print "No Elements in the linked list\n"
			return#returning to main method
		else:
			cur=self.head#assigning the current node as head
			for i in range(self.length()-1):#itreating from head to the last node.
				cur=cur.next#changing current node to the next node.
			temp_node=cur.next#temp variable to send data to main method
			cur.next=None#deleting the last node from the liked list by setting the pointer of the second last node to None
			return temp_node.data#returning deleted data to the main method
	"""
	Delete_pnode will delete the node at a given position or index
	"""
	def delete_pnode(self,position):
		if self.length()==0 or position>=self.length()or position<0:#checking wheather the given given position is valid or the liked list is empty.
			return [False]#returning flase if index not valid or the linked list is empty
		else:
			cur=self.head#assigning the current node as head
			for i in range(position+1):#itrating to position of the node to be deleted
				last_node=cur#setting previous node as current node
				cur=cur.next#setting previous node as current node
			last_node.next=cur.next#setting the pointer of last node to node after the node at given position.(sounds confusing lol ikr still tthats corret)
			return [True,cur.data]#returning the list contaning the trude state and the data of the deleted node.
print("Program to do linked list operations\n")
my_linked_list=linked_list()#creating an instance of the linked_list class				
while True:#the program will run unless the users choice is to exit the program inputing the value 0
	"""
	here in the main method we take the input user_input and do the corresponding linked list operations 
	if elif else cnstruct is used to  handle the user_input
	1:to Display 2:to show lenth 3:for insertion at head 4:for insertion at tail
	5:for insert anywhere 6:for Deletion at head 7:for deletion at tail 8:to delete anywhere 0:to exit
	"""
	user_input=input("Enter 1 to Display\nEnter 2 to show lenth\nEnter 3 for insertion at head\nEnter 4 for insertion at tail\nEnter 5 for insert anywhere\nEnter 6 for Deletion at head\nEnter 7 for deletion at tail\nEnter 8 to delete anywhere\nEnter 0 to exit\n")#Taking user input for the operation to be done
	if user_input==1: 
		my_linked_list.display()#if user input is 1 we call display function and displayes the linked list
	elif user_input==2:
		print"Length of the linked list is ",my_linked_list.length()#if user input is  we call length function and displayes the length of the linked list
	elif user_input==3:
		data=input("Enter the data to be inserted: ")#inputing data of the node to be passed
		my_linked_list.push(data)#if user input is 3 we call push function and pass the data data of the node to be added
		print"node with data ",data," added\n"
	elif user_input==4:
		data=input("Enter the data to be inserted: ")#inputing data of the node to be passed
		my_linked_list.append(data)#if user input is 4 we call append function and pass the data data of the node to be added
		print"node with data ",data," added \n"
	elif user_input==5:
		data=input("Enter the data to be inserted: ")#inputing data of the node to be passed
		position=input("Enter the position to be inserted: ")#inputing positon of the node to be passed
		z=my_linked_list.append_any_position(position,data)#if user input is 5 we call append_any_position function ,pass the position and data of the node to be added
		if z:#append_any_position function returns a list of one bool value(T if deleted F if not deleted) and data value(deleted value)
			print"node with data ",data," added at position ",position,"\n"
		else:
			print"Index error cannot be added\n"
	elif user_input==6:
		z=my_linked_list.delete_snode()#if user input is 6 we call delete_snode function which will delete the first node and returns the value of the deleted node
		print"Head Node with vale ",z,"is deleted\n"
	elif user_input==7:
		z=my_linked_list.delete_lnode()#if user input is 7 we call delete_snode function which will delete the last node and returnd the value of the deleted node
		print"Tail Node with vale ",z,"is deleted\n"
	elif user_input==8:
		position=input("Enter the position to be deleted: ")#inputing positon of the node to be deleted
		z=my_linked_list.delete_pnode(position)#if user input is 8 we call delete_pnode function ,pass the position of the node to be deleted and returns the list contaning the values status and deleted element
		if z[0]:
			print"Node with vale ",z[1],"at position ",position,"is deleted\n"
		else:
			print "out of index"
	elif user_input==0:
		exit()# to exit from program
	else:
		print("Invalid choice\n")
		

















			
		
		
