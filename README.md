# library-management-system
#                     **PROJECT TITLE**   

 **LIBRARY MANAGEMENT SYSTEM**  
Author: Shashwat Singh  
Registration Number:  26BCE10640

**OVERVIEW**

It is a Library Management System that is based on a menu and runs on a console, written using Python. The system handles members and books, deals with the issuing and return of books, and automatically computes fines for late returns. The entire project is contained in one file and makes use only of the Python standard library.

## **Features \-**

1\. Add Member \- records a new member and rejects any member IDs that are duplicates. 

 2\. Add Book \- This action adds a new book and rejects any duplicate book IDs. 

 3\. Issue Book \- Sends a book to a member and fixes the issue date and the due date.

 4\.  Remove a member \- The member can only be removed if they do not currently have a book issued. 

 5\. When a book is returned \- The book is returned, any fine is calculated and the book is then marked as available.  

6\. Search Book — displays the book's details, its status, and the name of the person who has it, together with the current fine if the book has been borrowed.

7\. Search Member — displays the member's details together with all the books they currently have, including the due dates and any fines.

8\. Show all books- Gives a list of every book together with its availability. 

 9\. Exit \- This ends the program. 

## **Technologies / Tools Used**

| Item | Details |
| ----- | ----- |
| Language |           Python  |
| Libraries | `datetime` (`date`, `timedelta`)  from the Python standard library |
| Data storage | In memory lists and dictionaries |
| Interface | Command-line |
| Editor / IDE | VS Code |

## **HOW TO RUN-**

1. Clone the repository    
      
    git clone https://github.com/\<your-username\>/library-management-system.git  
      cd library-management-system  
     
2. Run the program :  
      python library\_management.py  
3. Enter a number from 1 to 9 to choose an option. 

   ##     Instructions for Testing

The program starts with this sample data:  
 Members:   
 M101 \- Rahul Sharma   
 M102 \- Aman Verma   
 M103 \- Priya Singh   
 M104 \- Arjun Mehta 

Books: \- B101 \- Python Programming (issued to M101)   
 B102 \- Data Structures (issued to M102, overdue)   
 B103 \- Computer Networks (available)   
 B104 \- Artificial Intelligence (available)  
 B105 \- Introduction to Algorithms (available)

 Suggested test cases:   
1\. Add member Steps: Option 1 \-\> M105, Neha Gupta   
Expected result: "Member added successfully\!"  
 2\. Duplicate member Steps: Option 1 \-\> M101   
Expected result: "Member ID already exists\!"   
3\. Add book Steps: Option 2 \-\> B106, any name and author  
 Expected result: "Book added successfully\!"  
 4\. Duplicate book Steps: Option 2 \-\> B101   
Expected result: "Book ID already exists\!"  
 5\. Issue book Steps: Option 3 \-\> M103, B103   
Expected result: Issued; issue date and due date (15 days) shown  
 6\. Issue already-issued book Steps: Option 3 \-\> M104, B101  
 Expected result: "Book is already issued"   
7\. Issue with invalid member/book Steps: Option 3 \-\> M999 or B999 Expected result: "Member not found" / "Book not found"  
 8\. Return on time Steps: Option 5 \-\> M101, B101  
 Expected result: "Book returned on time\!", fine Rs. 0   
9\. Return late Steps: Option 5 \-\> M102, B102   
Expected result: Late by 2 days, fine Rs. 20   
10\. Search book Steps: Option 6 \-\> B102  
 Expected result: Details, status ISSUED, holder and current fine   
11\. Search member Steps: Option 7 \-\> M102   
Expected result: Member details with issued book, overdue status and fine   
12\. Remove member with issued book Steps: Option 4 \-\> M101 (before returning)   
Expected result: "Cannot remove the member..."   
13\. Remove member Steps: Option 4 \-\> M104   
Expected result: "Member removed successfully\!"   
14\. Display books Steps: Option 8  
 Expected result: All books with availability status   
15\. Exit Steps: Option 9  
 Expected result: Program closes with a thank-you message 

##  
