#### Isabella Malixi and Thomas Hillenmeyer - Computer Networking - Spring 2021

# NYU Classroom Chat App - Flask, SocketIO

This is an online chat application made to support onine schooling which uses Python, Flask and Socket IO.

### Table of Contents

    1.0 Introduction
        1.1 Purpose
        1.3 Installation
        1.4 Run
    2.0 Developement
        2.1 Login
        2.2 Homepage
        2.3 Classroom Group Chat
        2.4 Private Messaging
    3.0 Future Improvements
    4.0 Conclusion
    5.0 References

## 1.0 Introduction

We wanted to create an online chat application that would help support the classroom environment. For now, our application is targeted to Professors and Students in the NYU global network, but would ideally be used as a framework for other schools around the world. It allows professors to have a group chat with all of the students enrolled in the class, and enables student-student or student-professor private messaging who don't necessarily want to add eachother as a "friend" on social media platforms.

### 1.1 Purpose

This project was created as a final project for our Computer Networking Class. The reason we created this application is that there are many schools and universities around the world that don’t have sophisticated systems for communication between students and professors that are participating in a class (ex. Using facebook group chats, emails, and zoom only).
Today, the main means for communication between a student and a professors is email, and students communicate with eachother using social media. Back and Forth interaction through email is often slow and this leads to crowded inboxes. Sometimes, professors are okay with creating class group chats on chat platforms like Whatsapp, Facebook Messenger, or Wechat. The problem is, usually social media is part of people's private life, and professors/students would prefer keeping their school life seperate from their private life.

### 1.2 Installation

1.  Clone the repository.
2.  Install all the required libraries by running the following command

`pip install -r requirements.txt`

### 1.3 Run

Execute the application by

    `python app.py`

## 2.0 Development

### 2.1 Login

Enter username and password
Password hidden/show password

### 2.2 Homepage

Side bar with classes
A way to enter private messaging
Filter search
Logout (go back to login)

### 2.3 Classroom Group Chat

### 2.4 Private Messaging

## 3.0 Future Improvements

Database
Automatic history
Encryption
Quiz/Poll functionality
Sending Files
Mentioning
Searching for keywords
See which users are online
Class Announcements (read only) (professor write only)
Class Questions (read and write)
Pressing Enter sends message

## 4.0 Conclusion

## 5.0 References

Socket Programming:
https://www.geeksforgeeks.org/socket-programming-python/

Creating a multi-client chat using threading:
https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/
https://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php
https://www.jitsejan.com/python-and-javascript-in-flask.html

Flask:
https://www.brianlinkletter.com/2020/12/flask-web-app-tutorial-for-network-engineers/
https://www.youtube.com/watch?v=mqhxxeeTbu0
https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
https://www.youtube.com/watch?v=uJC8A_7VZOA (having room IDs)
https://github.com/danielv775/Whisperly/blob/master/application.py
https://www.youtube.com/watch?v=2-S-PMWJVxM (pt 2 has login)
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxi-user-notifications

Ajax:

HTML:

HTML and Python:

Diffie-Hellman encryption technique:
https://medium.com/@sadatnazrul/diffie-hellman-key-exchange-explained-python-8d67c378701c

CSS:
https://getbootstrap.com/docs/4.3/components/navbar/
https://www.youtube.com/watch?v=iUk-zgfRFU4
https://www.w3schools.com/howto/howto_js_topnav.asp
https://www.w3schools.com/howto/howto_css_fixed_sidebar.asp
https://www.youtube.com/watch?v=YesSVqjcDts
https://www.w3schools.com/w3css/w3css_sidebar.asp

Buttons and notification:
https://mdbootstrap.com/docs/standard/components/buttons/

Filtering:
https://www.w3schools.com/howto/howto_js_filter_lists.asp

Dynamic changing:
https://www.quackit.com/javascript/tutorial/innerhtml_in_javascript.cfm#:~:text=The%20innerHTML%20property%20can%20be,content%20without%20refreshing%20the%20page.&text=The%20innerHTML%20property%20can%20be%20used%20along%20with%20getElementById(),element%20and%20change%20its%20contents.

Databases with MySQL/ MongoDB etc. :
https://www.youtube.com/watch?v=vDxrmKOJMJ8
https://flask-mysqldb.readthedocs.io/en/latest/

Private messaging with flask:
https://cloudstack.ninja/lordhomie/sending-private-messages-using-flask-socketio/
