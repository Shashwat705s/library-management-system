## **Project Statement – Library Management System**

## 

Author: Shashwat Singh   
Registration Number: 26BCE10640

## **Problem Statement**

Small libraries, including those in schools and colleges, usually keep their records manually, using paper or loose spreadsheets. As a result, it is slow to locate a book, easy to forget who has borrowed which book, and prone to errors when working out the fines for late returns. Therefore, there is a requirement for a simple programme which keeps members' and books' records in one place, controls the process of issuing and returning books, and automatically calculates the fines.

## **Scope of the Project**

In scope:

We need to keep records of the members (listing their ID and name) and of the books (including their ID, name, author, and availability).  
Books are issued to registered members on a fixed schedule of 15 days.  
When books are returned, the fines are automatically calculated at a rate of ₹10 per day after the due date.  
Preventing actions which are invalid (such as assigning duplicate IDs, issuing a book that is unavailable, or removing a member who still has a book).  
Looking for books and members and showing their current status.  
It is run as a console application with a menu system in Python.

Out of scope (current version):

When the program is closed the data will be lost by being stored permanently (in a database or file).  
The graphical user interface or the web interface.  
Login by user / access based on role (admin as opposed to member).  
Taking books out, altering the records, the reservations, or the multiple copies of a book.  
Payment handling for fines.

## **Target Users**

Librarians or members of the library staff who are responsible for issuing and returning books as well as checking fines.  
Small institutions such as schools, colleges, clubs or community libraries will need a lightweight system.  
Students and those who are just starting to learn Python can use the project as an example of how to work with lists, dictionaries, loops and the datetime module.

## **High-Level Features**

Include new members and books while carrying out duplicate-ID checks.  
Give books to members automatically, with the issue and due dates being set automatically.  
Books should be returned with an automatic daily late fee of ₹10.  
Erase the members (only in the case where no books have been issued to them).  
To look up a book, you can find out about its details, availability, current holder, and fine.  
You can look up a member to view the books they have been issued, their due dates, and any fines they owe.  
Show the full list of books together with their availability status.  
A simple menu interface with clear messages for each action numbered.  
