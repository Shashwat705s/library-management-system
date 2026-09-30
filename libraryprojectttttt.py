from datetime import date, timedelta

print("Shashwat Singh")
print("Registration number: 26BCE10640")

fineperday = 10
issuedays = 15

# Random database for working

members = [
    {"id": "M101", "name": "Rahul Sharma"},
    {"id": "M102", "name": "Aman Verma"},
    {"id": "M103", "name": "Priya Singh"},
    {"id": "M104", "name": "Arjun Mehta"}
]

books = [
    {"id": "B101", "name": "Python Programming", "author": "John Snow", "available": False},
    {"id": "B102", "name": "Data Structures", "author": "D Lakshmi", "available": False},
    {"id": "B103", "name": "Computer Networks", "author": "Anubhav Singh", "available": True},
    {"id": "B104", "name": "Artificial Intelligence", "author": "Ravi Kishan", "available": True},
    {"id": "B105", "name": "Introduction to Algorithms", "author": "Arnav Agarwal", "available": True}
]

issuedate1 = date.today() - timedelta(days=12)
duedate1 = issuedate1 + timedelta(days=issuedays)

issuedate2 = date.today() - timedelta(days=17)
duedate2 = issuedate2 + timedelta(days=issuedays)

issuedbooks = [
    {"memberid": "M101", "bookid": "B101", "issuedate": issuedate1, "duedate": duedate1},
    {"memberid": "M102", "bookid": "B102", "issuedate": issuedate2, "duedate": duedate2}
]

choice = ""

while choice != "9":

    print("\n============================================")
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("============================================")
    print("1. Add Member")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Remove Member")
    print("5. Return Issued Book")
    print("6. Search Book")
    print("7. Search Member")
    print("8. Display All Books")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # Adding a new member

    if choice == "1":

        memberid = input("Enter Member ID: ")
        membername = input("Enter the name of member:")

        memberexists = any(member["id"] == memberid for member in members)

        if memberexists:

            print("\nMember ID already exists!")

        else:

            members.append({"id": memberid, "name": membername})

            print("\nMember added successfully!")

    # adding a bookkkkkkkkkkk

    elif choice == "2":

        bookid = input("Enter Book ID: ")
        bookname = input("Enter the name of book : ")
        author = input("Enter the name of the author : ")

        bookexists = any(book["id"] == bookid for book in books)

        if bookexists:

            print("\nBook ID already exists!")

        else:

            books.append({
                "id": bookid,
                "name": bookname,
                "author": author,
                "available": True
            })

            print("\nBook added successfully!")

    # Issuing a book from library

    elif choice == "3":

        memberid = input("Enter Member ID: ")
        bookid = input("Enter Book ID: ")

        memberexists = any(member["id"] == memberid for member in members)

        book = None

        for bookdata in books:

            if bookdata["id"] == bookid:

                book = bookdata
                break

        if not memberexists:

            print("\nMember not found")

        elif book is None:

            print("\nBook not found")

        elif not book["available"]:

            print("\nBook is already issued")

        else:

            issuedate = date.today()

            duedate = (issuedate + timedelta(days=issuedays))

            book["available"] = False

            issuedbooks.append({
                "memberid": memberid,
                "bookid": bookid,
                "issuedate": issuedate,
                "duedate": duedate
            })

            print("\nBook issued successfully!")
            print("Issue Date:", issuedate)
            print("Due Date:", duedate)
            print("Issue Period:", issuedays, "days")

    # Removing the member from the system

    elif choice == "4":

        memberid = input("Enter the Member ID to be remove: ")

        member = None

        for memberdata in members:

            if memberdata["id"] == memberid:

                member = memberdata
                break

        if member is None:

            print("\nMember not found")

        elif any(
            issued["memberid"] == memberid
            for issued in issuedbooks
        ):

            print("\nCannot remove the member because this member currently has an issued book")

        else:

            members.remove(member)

            print("\nMember removed successfully!")

    # Returning the issued boook and fine calculation

    elif choice == "5":

        memberid = input("Enter Member ID: ")
        bookid = input("Enter Book ID: ")

        record = None

        for issued in issuedbooks:

            if issued["memberid"] == memberid and issued["bookid"] == bookid:

                record = issued
                break

        if record is None:

            print("\nNo matching issued book found!")

        else:

            returndate = date.today()

            latedays = (returndate - record["duedate"]).days

            if latedays > 0:

                fine = latedays * fineperday

                print("\nBook returned late!")
                print("Late by:", latedays, "days")
                print("Fine: ₹", fine)

            else:

                fine = 0

                print("\nBook returned on time!")
                print("Fine: ₹0")

            issuedbooks.remove(record)

            for book in books:

                if book["id"] == bookid:

                    book["available"] = True
                    break

            print("Book returned successfully!")

    # Searching the book

    elif choice == "6":

        searchid = input("Enter Book ID to search: ")

        book = None

        for bookdata in books:

            if bookdata["id"] == searchid:

                book = bookdata
                break

        if book is None:

            print("\nBook is NOT present in the library.")

        else:

            print("LOADING BOOK DETAIL.....")

            print("\n============================================")
            print("              BOOK DETAILS")
            print("============================================")

            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])

            if book["available"]:

                print("Status: AVAILABLE")
                print("The book is currently in the library.")

            else:

                print("Status: ISSUED")

                record = None

                for issued in issuedbooks:

                    if issued["bookid"] == searchid:

                        record = issued
                        break

                if record:

                    member = None

                    for memberdata in members:

                        if memberdata["id"] == record["memberid"]:

                            member = memberdata
                            break

                    if member:

                        print("Issued To:", member["name"])

                    print("Member ID:", record["memberid"])
                    print("Issue Date:", record["issuedate"])
                    print("Due Date:", record["duedate"])

                    today = date.today()

                    latedays = (today - record["duedate"]).days

                    if latedays > 0:

                        fine = (latedays * fineperday)

                        print("Current Fine: ₹", fine)

                    else:

                        print("Current Fine: ₹0")

    # Search member in the system and their details

    elif choice == "7":

        searchid = input("Enter Member ID to search: ")

        member = None

        for memberdata in members:

            if memberdata["id"] == searchid:

                member = memberdata
                break

        if member is None:

            print("\nMember is not registered in the library.")

        else:

            print("member details loading...")

            print("\n============================================")
            print("             MEMBER DETAILS")
            print("============================================")

            print("Member ID:", member["id"])
            print("Member Name:", member["name"])

            memberbooks = [
                issued for issued in issuedbooks
                if issued["memberid"] == searchid
            ]

            if len(memberbooks) == 0:

                print("Status: No book currently issued.")

            else:

                print("Status: Book(s) currently issued.")
                print("Number of books issued:", len(memberbooks))

                for record in memberbooks:

                    print("\n--------------------------------------------")

                    for book in books:

                        if book["id"] == record["bookid"]:
                            break

                    print("Book ID:", book["id"])
                    print("Book Name:", book["name"])
                    print("Issue Date:", record["issuedate"])
                    print("Due Date:", record["duedate"])

                    today = date.today()
                    latedays = (today - record["duedate"]).days

                    if latedays > 0:

                        fine = latedays * fineperday

                        print("Status: OVERDUE")
                        print("Late by:", latedays, "days")
                        print("Fine Due Today: ₹", fine)

                    else:

                        print("Status: Book is within due date")
                        print("Fine Due Today: ₹0")

    # Display all the books in the system

    elif choice == "8":

        if len(books) == 0:

            print("\nNo books in the library.")

        else:

            print("\n============================================")
            print("                ALL BOOKS")
            print("============================================")

            for book in books:

                print("\nBook ID:", book["id"])
                print("Book Name:", book["name"])
                print("Author:", book["author"])

                if book["available"]:

                    print("Status: AVAILABLE")

                else:

                    print("Status: ISSUED")

    elif choice == "9":

        print("\nThank you for using the Library Management System")
        print("Program closed.")