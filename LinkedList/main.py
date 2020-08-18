class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("Linked List Is empty")
            return
        itr =self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    

    def insert_at_begening(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is Node:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def remove_at(self,index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index ==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if ( count == index-1 ):
                itr.next=itr.next.next
                break
            else:
                itr=itr.next
            count+=1
    


    
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_begening(data)

        

    
    def get_length(self):
        counter=0
        itr=self.head
        while itr:
            counter+=1
            itr=itr.next
        return counter
 
    def insert_at(self,index,data):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begening(data)
            return

        count=0
        itr=self.head

        while itr:
            if ( count == index-1 ):
                node=Node(data,itr.next)
                itr.next=node
                break
            else:
                itr=itr.next
            count+=1

if __name__ == "__main__":
    ll=LinkedList()
    ll.insert_at_begening(4)
    ll.insert_at_begening(40)
    ll.insert_at_end(22)
    ll.insert_values([1,2,3,4,5])
    ll.print()
    ll.remove_at(0)
    ll.print()
    ll.insert_at(2,1)
    ll.print()