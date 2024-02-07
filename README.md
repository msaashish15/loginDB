"1 - loginDB "


Description

This Python program serves as a simple user authentication system. It allows users to log in, register, and quit the application. User credentials (username and password) are stored in a dictionary called loginDB. The program prompts users to enter their username and password, verifies the credentials, and provides appropriate feedback.

Features

Login: Users can log in using their existing username and password.
Registration: New users can register by providing a username and password.
Password Check: The pwd_check function currently returns 1, indicating a successful password check. This can be enhanced based on specific password requirements or validation rules.

Usage

Run the program.
Choose one of the following options:
1: Login: Enter an existing username and password.
2: Register: Provide a new username and password for registration.
3: Quit: Exit the program.
Example

"OUTPUT"
Customer Login Screen
Press 1 for login, 2 for register, 3 to quit

1
Enter your username: user1
Enter your password: pswd1
Login successful

Press 1 for login, 2 for register, 3 to quit

2
Enter your username: newuser
You are a new user
Enter your password: newpassword
Registration successful

Press 1 for login, 2 for register, 3 to quit

3

Notes

The program's password-checking mechanism is currently a placeholder (pwd_check function returns 1). It can be modified to implement more robust password validation.
Ensure that the loginDB dictionary is appropriately managed to persist user data between program runs in a real-world scenario.
This program serves as a basic example and may require further enhancements for production use, such as securing user data and implementing more sophisticated authentication mechanisms.
Feel free to adapt and extend the program based on your specific requirements.
