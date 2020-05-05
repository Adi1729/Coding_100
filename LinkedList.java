public class LinkedList {

    static Node head;

    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            next = null;
        }

    }


        public static void main(String[] args) {
            head = null;
            head = new Node(10);

            Node temp = head;

            for (int i = 0; i < 5; i++) {

                temp.next = new Node(i*10);
                temp = temp.next;

            }

//            addelem(2,3);
//            System.out.println("Linked List after inserting elem 3 at index 2" );
//            printlist();

            reverse_elem();
            System.out.println("Reversed Linked List " );
            printlist();

            printmiddlenode();
            print_nth_from_end(2);




        }

    static void addelem(int index,int elem){
        Node current = head;
        Node prev= current;
        int position= 0;
        while((position<index) && (current.next!=null)){
            position = position +1;
            prev = current;
            current = current.next;

        }

        if (position==index){
            Node new_node = new Node(elem);
            prev.next = new_node;
            new_node.next = current;
        }

    }

    static void printlist(){

        Node current = head;

        while (current != null) {

            System.out.println(current.data);
            current = current.next;


        }
    }

    static void reverse_elem(){
        Node current = head;
        Node prev = null;
        Node next_node = current;

        while(current.next!=null){
            next_node = current.next;
            current.next = prev;
            prev = current;
            current =  next_node;
        }
        head = prev;


    }

    static void printmiddlenode(){

        Node current = head.next;
        Node prev = head;

        while(current!=null && current.next!=null){
            prev = prev.next;
            current = current.next.next;

        }

        System.out.println("Middle Node: " + prev.data);
    }


    static void print_nth_from_end(int n){
        Node current = head;
        Node n_forward = head;

        for(int i = 0 ; i < n-1 ; i++){
            n_forward = n_forward.next;
        }


        while(n_forward.next!=null){
            current = current.next;
            n_forward = n_forward.next;
        }

        System.out.println( n + "th element from end is " + current.data);
    }


}