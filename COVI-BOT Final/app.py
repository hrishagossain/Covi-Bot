from flask import Flask, render_template, request  # Import the necessary Flask modules
import ast  # Import the ast module for literal evaluation
import os.path  # Import the os.path module for file operations
import chatbot  # Import the chatbot module for chatbot functionality

app = Flask(__name__)  # Create a Flask application instance
app.static_folder = 'static'  # Set the static folder for serving static files such as CSS, JavaScript, and images

reg_file = "datasheet.txt"  # File name for storing user data

@app.route("/")  # Define a route for the main page ("/")
def main():
    return render_template("Main.html")  # Render the "Main.html" template for the main page

@app.route('/login_form', methods=['POST'])  # Define a route for the login form ("/login_form")
def log():
    return render_template('log_in.html')  # Render the "log_in.html" template for the login form

@app.route('/register_form', methods=['POST'])  # Define a route for the register form ("/register_form")
def sign():
    return render_template('sign_up.html')  # Render the "sign_up.html" template for the register form

@app.route("/for_register", methods=['POST', 'GET'])  # Define a route for form submission ("/for_register")
def register():
    name1 = request.form['username']  # Get the value of the "username" field from the form
    psd = request.form['password']  # Get the value of the "password" field from the form
    confirm = request.form['confirm']  # Get the value of the "confirm" field from the form

    if psd == confirm:  # Check if the password matches the confirmation
        try:
            if os.path.isfile(reg_file):  # Check if the registration file exists
                with open(reg_file, 'r') as file:  # Open the registration file in read mode
                    user_data = ast.literal_eval(file.read())  # Read and evaluate the file contents as a dictionary
            else:
                user_data = {}  # If the registration file doesn't exist, create an empty dictionary

            if name1 in user_data.keys():  # Check if the username already exists in the user data dictionary
                error_message = "Username already exists. Please choose a different username."
                return render_template('sign_up.html', error_message=error_message)  # Render the "sign_up.html" template with an error message

            user_data[name1] = psd  # Add the new username and password to the user data dictionary

            with open(reg_file, 'w') as file:  # Open the registration file in write mode
                file.write(str(user_data))  # Write the updated user data dictionary to the file

            return render_template('log_in.html')  # Render the "log_in.html" template after successful registration
        except Exception as e:
            print("Error:", e)  # Print the error message to the console
            return render_template('sign_up.html')  # Render the "sign_up.html" template in case of an error during registration
    else:
        error_message = "Password and confirmation do not match. Please try again."
        return render_template('sign_up.html', error_message=error_message)  # Render the "sign_up.html" template with an error message

@app.route("/for_login", methods=['POST', 'GET'])  # Define a route for login form submission ("/for_login")
def login():
    name1 = request.form['username']  # Get the value of the "username" field from the form
    psd = request.form['password']  # Get the value of the "password" field from the form

    if os.path.isfile(reg_file):  # Check if the registration file exists
        with open(reg_file, 'r') as file:  # Open the registration file in read mode
            user_data = ast.literal_eval(file.read())  # Read and evaluate the file contents as a dictionary

        if name1 in user_data.keys() and psd == user_data[name1]:  # Check if the username and password match the user data
            return render_template('chatbot.html')  # Render the "chatbot.html" template after successful login
        else:
            error_message = "Invalid username or password. Please try again."
            return render_template('log_in.html', error_message=error_message)  # Render the "log_in.html" template with an error message
    else:
        error_message = "Invalid username or password. Please try again."
        return render_template('log_in.html', error_message=error_message)  # Render the "log_in.html" template with an error message

@app.route("/get")  # Define a route for obtaining chatbot responses ("/get")
def get_bot_response():
    userText = request.args.get('msg')  # Get the value of the "msg" parameter from the URL query string
    return str(chatbot.get_response(userText))  # Get a response from the chatbot based on the user input and return it as a string

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode
