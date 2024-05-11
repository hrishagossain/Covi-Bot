import random
import difflib
import webbrowser
from googlesearch import search
import re
import wikipedia
import requests
import nltk

# Import the necessary modules from nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import dataset
import cheeker


# Define a function to get the closest match for the user input from the dictionary keys
def get_closest_match(user_input, response_keys):
    closest_match = difflib.get_close_matches(user_input, response_keys)  # Use the difflib library to get the closest match
    if closest_match:
        return closest_match[0]  # Return the closest match if it exists
    else:
        return None  # Return None if no closest match was found

# Define a function to perform a Google search for the given query
def search_google(query):
    search_url = "https://www.google.com/search?q=" + query
    response = "Here's a Google search result for " + query + ":<br>"
    response += "<a href='" + search_url + "' target='_blank'>" + search_url + "</a><br>"
    return response

# Define a function to perform a Google search for the given query
def search_google(query):
    search_url = "https://www.google.com/search?q=" + query
    response = "Here's a Google search result for " + query + ":<br>"
    response += "<a href='" + search_url + "' target='_blank'>" + search_url + "</a><br>"
    return response

# Define a regular expression pattern to match verbs
verb_pattern = re.compile(r'\b(?!_)(\w+)\b(?<!_)', re.IGNORECASE)

# Define a set to store the questions that have already been saved
saved_questions = set()

# Define a function to generate the chatbot response
def get_response(user_input):
    global saved_questions
    user_input = user_input.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase

    if "fever"in user_input or "i have fever" in user_input or "i have high fever" in user_input or "i experience fever" in user_input or "i am having fever" in user_input or "i am experiencing fever" in user_input or "i have high temperature" in user_input   or "i am having high fever" in user_input or "i think i have fever" in user_input or "my body temperature is high" in user_input or "i am feeling feverish" in user_input or "my body is hot" in user_input or "amar jor hoyeche" in user_input or "amar khub jor jor lagche" in user_input or "mujhe bukhar hai" in user_input or "mereko bukhar hai" in user_input or "amar mone hoche jor hoyeche" in user_input or "amar gaa gorom" in user_input:  # Check if the user wants to check for COVID-19 symptoms
        cheeker.symptom_list('fever')
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "cough"in user_input or "i have cough" in user_input or "i am coughing" in user_input or "i have dry cough" in user_input or "i am experiencing cough" in user_input or "i experience cough" in user_input or "i experience dry cough" in user_input or "amar khub kashi" in user_input or "ami khub kashchi" in user_input or "amar sukno kashi hoyeche" in user_input or "main khash rahi hoon" in user_input or "mujhe khasi ho rahi hain" in user_input or "ami bhishon khashchi" in user_input or "main bohot khash rahi hoon" in user_input:
        cheeker.symptom_list("cough")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "runny nose" in user_input or "cold" in user_input or"i have runny nose" in user_input or "i am have running nose" in user_input or "i am having runny nose" in user_input or "my nose is running" in user_input or "my nose is cold" in user_input or "i am having cold nose" in user_input or "amar nak theke jol porche" in user_input or "mere nak se paani gir raha hain" in user_input:
        cheeker.symptom_list("nose")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "tasteless" in user_input or "no smell" in user_input or"no taste" in user_input or "i lost taste" in user_input or"i lost taste and smell" in user_input or "i am not getting taste of any food" in user_input or "i can not smell any thing" in user_input or "i am tasteless" in user_input or "i am not getting any taste" in user_input or "i am smelless" in user_input or "i am not getting any smell" in user_input:
        cheeker.symptom_list("tatse_smell")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "i have difficulty in breathing" in user_input   or "i am experiencing spasm" in user_input or "i have spasm" in user_input or "i am having spasm" in user_input or "i am having breathing problem" in user_input  or "i am facing difficulty in breathing" in user_input or "i am facing difficulty to breathe" in user_input or "i can not breathe properly" in user_input  or "amar nisash nite kosto hoche" in user_input  or "mujhe sans lene mein problem ho raha hai" in user_input:
        cheeker.symptom_list("breath")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "sore throat" in user_input or "i have sore throat" in user_input  or "i am having sore throat" in user_input  or "my throat is sored" in user_input  or "amar golaye betg  " in user_input:
        cheeker.symptom_list("throat")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "headache" in user_input or "i have headache" in user_input or "my head is paining" in user_input or "my head is aching" in user_input or "i having terrible headache" in user_input or "i am experiencing terrible headache" in user_input or "i am experiencing terrible head pain" in user_input or "amar matha betha korche" in user_input or "amar bhishon matha betha" in user_input or "mera sir dard kar raha hain" in user_input or "mere sir mein dard hain" in user_input:
        cheeker.symptom_list("head")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "diarrhea" in user_input or "upset stomach"in user_input or "i have diarrhea" in user_input or "i have diarrheoa" in user_input or "i think i have diarrhea" in user_input or "i think i have diarrheoa" in user_input or "i think i have diarrhea" in user_input  or "diarrhea hoyeche amar" in user_input  or "diarrhea hoyeche amar" in user_input  or "diarrhea hua hai mujhe" in user_input :
        cheeker.symptom_list("dia")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "nausea" in user_input or "vommiting"in user_input or "vomit"in user_input or "i vomit" in user_input  or "i have nausea" in user_input or "i am vomitting" in user_input  or "i am feeling like to vomit" in user_input  or "amar bomi hoche" in user_input  or "mujhe ulti ho raha hai" in user_input:
        cheeker.symptom_list("vomit")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "fatigue" in user_input or "tired"in user_input or "i am experiencing fatigue" in user_input  or "i am getting tired" in user_input  or "i am getting overtired" in user_input  or "ami khub klanto hoye jachi" in user_input  or "main tired ho rahi hoon" in user_input  or "ami khub tired hoye jachi" in user_input:
        cheeker.symptom_list("fatigue")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "body pain" in user_input or "body ache" in user_input or "pain" in user_input or "i am having muscle pain" in user_input  or "i am having body pain" in user_input or "i am having body and muscle pain" in user_input or "i have body pain" in user_input or "i have muscle pain" in user_input  or "i have body and muscle pain" in user_input or "i have terrible muscle pain" in user_input or "i have terrible body pain" in user_input  or "i am having terrible body and muscle pain" in user_input  or "i am facing body pain" in user_input  or "i am facing muscle pain" in user_input  or "i am facing body and muscle pain" in user_input or "i am experiencing muscle pain" in user_input or "i am experiencing body pain" in user_input or "i am experiencing body and muscle pain" in user_input or "i am experiencing terrible body pain" in user_input or "i am experiencing terrible muscle pain" in user_input or "i am experiencing terrible body and muscle pain" in user_input :
        cheeker.symptom_list("body_muscle")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "chest"in user_input or "chest pain"in user_input or "i am having chest pain" in user_input or "i have chest pain" in user_input or "i am experiencing chest pain" in user_input or "i have terrible chest pain" in user_input or "i am having terrible chest pain" in user_input  or "i am facing chest pain" in user_input or "i am experiencing terrible chest pain" in user_input:
        cheeker.symptom_list("chest")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "eye"in user_input or "i am having pink eye" in user_input  or "i am having conjunctivitis" in user_input or "i am having pink eyes" in user_input or "i have conjunctivitis" in user_input or "i have pink eye" in user_input  or "i have pink eyes" in user_input or "i have terrible conjunctivitis" in user_input or "i have terrible pink eye" in user_input  or "i am having terrible pink eyes" in user_input  or "i am facing conjunctivitis" in user_input  or "i am facing pink eye" in user_input  or "i am facing pink eyes" in user_input :
        cheeker.symptom_list("conjunctivitis")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    elif "rash"in user_input or "i am having rashes" in user_input or "i have rashes" in user_input or "i am experiencing rashes" in user_input or "i have terrible rashes" in user_input or "i am having terrible rashes" in user_input  or "i am facing rashes" in user_input :
        cheeker.symptom_list("rash")
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    
    elif "question" in user_input or "query" in user_input:
        return "That's greate. Tell me what do you want to know aboud covid?"
    
    elif "i am having " in user_input or "i have " in user_input or "i am experiencing " in user_input or "i am facing " in user_input :
        return "Do you have any other symptoms?If yes please mention it one by one in  a sentence."
    
    elif 'no' in user_input:
        rec=cheeker.cheeker()
        return rec
    
    else:
        tokens = word_tokenize(user_input)  # Tokenize the user input into a list of words
        tagged_tokens = pos_tag(tokens)  # Perform part-of-speech tagging on the tokens

        # Remove all verbs from the part-of-speech tagged tokens
        tagged_tokens = [(word, pos) for word, pos in tagged_tokens if not pos.startswith('VB')]
        # Reconstruct the user input string from the remaining tagged tokens
        user_input = ' '.join([word for word, pos in tagged_tokens])
        # Get the closest matching response key from the dictionary
        response_key = get_closest_match(user_input, dataset.responses.keys())
        if response_key:
            # If a matching response key is found, select a random response from the corresponding list
            response = random.choice(dataset.responses[response_key])
        else:
            # If no matching response key is found, search Wikipedia for information
            try:

                
                page = wikipedia.page(user_input)
                summary = wikipedia.summary(user_input)
                url = page.url
                summary_words = summary.split()[:80] # Split the summary into words and take the first 50 words
                summary_truncated = ' '.join(summary_words) + '...' # Join the first 50 words and add ellipsis
                response = summary_truncated + "<br>Here's the Wikipedia page:<br>"
                response += "<a href='" + url + "' target='_blank'>" + url + "</a><br>"
                response += search_google(user_input)
            except wikipedia.exceptions.DisambiguationError as e:
                options = ", ".join(e.options[:5])
                response = "I'm sorry, I couldn't find information on that topic. Here are some possible options: " + options
            except wikipedia.exceptions.PageError:
                # Search Google for information if no Wikipedia page was found
                try:
                    response = search_google(user_input)
                except:
                    response = "I couldn't find anything. Please search for something else."
            # Check if the question has already been saved
            if user_input not in saved_questions:
            # Save the new question and its response to the text file
                with open("new_questions.txt", "a") as file:
                    file.write(user_input + "\n")
                saved_questions.add(user_input)
    return response


