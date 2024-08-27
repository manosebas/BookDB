# Multi-Layered Database Application

## Description
This project involves the implementation of a multi-layered application that connects to a MySQL database, designed to manage book records. The application features a graphical user interface (GUI) developed using QtDesigner and Python, enabling users to perform CRUD (Create, Read, Update, Delete) operations on the database. The project demonstrates the integration of multiple windows for different operations, such as selecting, inserting, updating, and deleting records. The application is highly expandable, with the potential to manage more complex data structures and interactions.

**Short Description:** Database Management App

## Database Design and Data

**Database UML Diagram**  
This diagram illustrates the structure of the database, including the relationships between tables.
![Database UML](./images/1.png)

**Author Table with Data**  
This table contains the details of the authors.
![Author Table](./images/2.png)

**Books Table with Data**  
This table stores information about the books.
![Books Table](./images/3.png)

**Books_has_Authors Table with Data**  
This table links books with their respective authors.
![Books_has_Authors Table](./images/4.png)

**Phone Table with Data**  
This table stores the phone numbers related to the authors or publishers.
![Phone Table](./images/5.png)

## Application Interface

**Main Window**  
The main window of the application features four buttons for different operations: Search Books, Insert Books, Update Books, Delete Books.
![Main Window](./images/6.png)

**Select/Search Books by Title**  
This window allows users to search for books by their title.
![Search Books by Title](./images/7.png)

**Select/Search Books by Author**  
This window allows users to search for books by their author.
![Search Books by Author](./images/8.png)

**Insert Book Window**  
This window requires the user to input the book's ID, name, price, and the number of pages.
![Insert Book Window](./images/9.png)

**Book Insertion Confirmation**  
This screen shows that the book has been successfully inserted.
![Book Inserted](./images/10.png)

**Update Book Window**  
This window allows the user to update the book's details by providing the ID, name, price, and page count. If the ID matches an existing book, the information is overwritten.
![Update Book Window](./images/11.png)

**Book Update Confirmation**  
This screen shows that the book's details have been successfully updated.
![Book Updated](./images/12.png)

**Delete Book Window**  
This window requires the user to input the book's ID to delete it from the database.
![Delete Book Window](./images/13.png)

**Book Deletion Confirmation**  
This screen shows that the book has been successfully deleted.
![Book Deleted](./images/14.png)

## Note
The graphical interface was not the primary focus of this project, so a simple one was used. However, the project can be significantly improved and expanded, both in terms of the interface and functionality.
