
# Define the name of the chatbot and some possible greeting messages
bot_name = "Covi-Bot"
greeting = ["Hello! I'm " + bot_name + ".", "Hi there! I'm " + bot_name + ".", "Hey, it's " + bot_name + "!"]

# Define a dictionary of responses to user input

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "hlw": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hi!", "Heya!", "Holaa!"],
    "tell me about you":["Hello! I am Covi-Bot .You can ask me anything about Covid-19 .You can also tell me if you have any symptoms"],
    "who are you":["Hello! I am Covi-Bot.You can ask me anything about Covid-19.You can also tell me if you have any symptoms"],
    "how are you?": ["I'm doing well, thanks!", "I'm good, thanks for asking!", "I'm great!","I am awesome"],
    "i am nice":["Thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "i am awesome":["thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "i am great":["thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "i am beautiful":["thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "i am faboulous":["thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "i am amazing":["thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "i am good":["thats great,what you want know about Covid?","Sounds nice! What you want to know about Covid"],
    "what's your name?": ["My name is " + bot_name + "."+"How can I help you?"],
    "I am": ["Thats great ! What you want to know about Covid?"],
    "I am here to check symptoms": ["Sure! Do you have any symptoms?"],
    "I want to check symptoms": ["Sure! Do you have any symptoms?"],
    "my name is": ["Thats great ! What you want to know about Covid?"],
    "thank you": ["Most welcome.Do you want to know anything else?","My pleasure.Do you want to know anything else?","Not a problem.Do you want to know anything else?"],
    "thanks": ["Most welcome.Do you want to know anything else?","My pleasure.Do you want to know anything else?","Not a problem.Do you want to know anything else?"],
    "thnks": ["Most welcome.Do you want to know anything else?","My pleasure.Do you want to know anything else?","Not a problem.Do you want to know anything else?"],
    "thnx": ["Most welcome.Do you want to know anything else?","My pleasure.Do you want to know anything else?","Not a problem.Do you want to know anything else?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "have a nice day": ["You too"],
    "see ya": ["Yes","Yup"],
    "see you": ["Yes","Yup"],
    "wow": ["Yes","Yup"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."],
    "ok":["pkaaaay!"],
    "okay":["okaay!"],
    "I was wondering if you can teach me more about Covid19": ['''Covid-19 is a viral illness caused by the SARS-CoV-2 virus. The virus was first identified in Wuhan, China in December 2019, and it has since spread to become a global pandemic.
    Symptoms of Covid-19 can vary, but they typically include fever, cough, and shortness of breath. Some people may also experience fatigue, muscle aches, headache, loss of taste or smell, sore throat, or congestion. In severe cases, Covid-19 can lead to pneumonia, acute respiratory distress syndrome (ARDS), and death.
    Covid-19 is primarily spread through respiratory droplets that are released when an infected person talks, coughs, or sneezes. The virus can also be spread by touching a surface contaminated with the virus and then touching your mouth, nose, or eyes.
    Preventing the spread of Covid-19 involves several measures, including wearing masks in public, practicing physical distancing, washing hands frequently with soap and water, and avoiding large gatherings. Vaccines have also been developed and are widely available to help prevent severe illness and hospitalization from Covid-19.
    If you have further questions or concerns about Covid-19, please do not hesitate to ask.'''],

    "what is coronavirus ": ["Coronavirus is a family of viruses that can cause illness in animals and humans. The coronavirus that has been causing the current pandemic is known as SARS-CoV-2, which causes the illness COVID-19. COVID-19 first emerged in Wuhan, China in late 2019 and has since spread globally, leading to widespread illness, death, and economic disruption"],
    "about corona ": ["Coronavirus is a family of viruses that can cause illness in animals and humans. The coronavirus that has been causing the current pandemic is known as SARS-CoV-2, which causes the illness COVID-19. COVID-19 first emerged in Wuhan, China in late 2019 and has since spread globally, leading to widespread illness, death, and economic disruption"],
    
    "What is Covid": ["COVID-19, also known as the coronavirus disease 2019, is an infectious disease caused by a newly discovered coronavirus called SARS-CoV-2. The disease first emerged in Wuhan, China, in late 2019 and quickly spread around the world, causing a global pandemic. COVID-19 primarily spreads through respiratory droplets when an infected person talks, coughs, or sneezes, but it can also spread by touching a surface contaminated with the virus and then touching mouth, nose, or eyes. The disease can range from mild to severe symptoms and can be fatal, particularly in older adults or those with underlying health conditions. Common symptoms include fever, cough, fatigue, and difficulty breathing. Vaccines and public health measures, such as wearing masks, social distancing, and frequent hand washing, are being used to control the spread of the disease"],
    "about Covid": ["COVID-19, also known as the coronavirus disease 2019, is an infectious disease caused by a newly discovered coronavirus called SARS-CoV-2. The disease first emerged in Wuhan, China, in late 2019 and quickly spread around the world, causing a global pandemic. COVID-19 primarily spreads through respiratory droplets when an infected person talks, coughs, or sneezes, but it can also spread by touching a surface contaminated with the virus and then touching mouth, nose, or eyes. The disease can range from mild to severe symptoms and can be fatal, particularly in older adults or those with underlying health conditions. Common symptoms include fever, cough, fatigue, and difficulty breathing. Vaccines and public health measures, such as wearing masks, social distancing, and frequent hand washing, are being used to control the spread of the disease"],

    "what makes COVID-19 fatal": ["COVID-19 can be fatal in some cases because it can cause severe respiratory illness and can lead to complications such as pneumonia, acute respiratory distress syndrome (ARDS), and organ failure. In severe cases, COVID-19 can lead to damage and scarring of the lungs, which can make it difficult for oxygen to pass into the bloodstream."],

    "is corona virus a disease": ["Coronavirus is not a disease itself, but rather a family of viruses that can cause disease in humans and animals. The coronavirus that is currently causing a pandemic is called SARS-CoV-2 and it causes the illness COVID-19. COVID-19 is a respiratory illness that can range from mild to severe, and in some cases can be fatal"],

    "is corona virus a pheic": ["It's possible that you meant to ask if coronavirus is a PHEIC, which stands for Public Health Emergency of International Concern. In that case, the answer is yes. The World Health Organization (WHO) declared COVID-19 a PHEIC on January 30, 2020, due to the rapidly evolving nature of the outbreak and its potential impact on global health."],

    "is coronavirus a virus": ["Yes, coronavirus is a type of virus. Specifically, it is a member of the family of viruses called Coronaviridae. The coronavirus that is currently causing a pandemic is called SARS-CoV-2, which causes the illness COVID-19."],

    "is corona virus actually dangerous": ["Yes, coronavirus, specifically the SARS-CoV-2 virus that causes COVID-19, can be dangerous, especially for certain populations. While many people who contract the virus experience mild to moderate symptoms and recover without the need for hospitalization, COVID-19 can cause severe illness, hospitalization, and even death in some cases."],

    "is corona virus airborne": ["The SARS-CoV-2 virus that causes COVID-19 is primarily spread through respiratory droplets that are expelled when an infected person talks, coughs, or sneezes. These droplets are relatively heavy and generally fall to the ground or other surfaces within a few feet of the person who released them."],

    "is corona virus icos or helical": ["The SARS-CoV-2 virus that causes COVID-19 has a helical symmetry. This means that its genetic material, which is a single-stranded RNA molecule, is enclosed by a helical protein shell, or capsid. The helical capsid is then surrounded by a lipid envelope, which is studded with spike proteins that give the virus its characteristic corona appearance."],

    "what is the symmetry of coronavirus": ["The SARS-CoV-2 virus that causes COVID-19 has a helical symmetry. This means that its genetic material, which is a single-stranded RNA molecule, is enclosed by a helical protein shell, or capsid. The helical capsid is then surrounded by a lipid envelope, which is studded with spike proteins that give the virus its characteristic corona appearance."],

    "is coronavirus a flu virus": ["No, coronavirus is not a flu virus. While both COVID-19 (caused by the SARS-CoV-2 virus) and the flu (caused by influenza viruses) can cause respiratory illness and share some similar symptoms such as fever, cough, and fatigue, they are caused by different viruses and have some important differences in terms of transmission, severity, and treatment."],

    "is coronavirus a pandemic": ["Yes, COVID-19, the disease caused by the SARS-CoV-2 virus, has been declared a pandemic by the World Health Organization (WHO). A pandemic is an outbreak of a disease that has spread over a large geographical area, often affecting multiple countries and continents."],

    "is coronavirus a plague": ["No, coronavirus (specifically, the SARS-CoV-2 virus that causes COVID-19) is not a plague. Plague is a specific infectious disease caused by the bacteria Yersinia pestis, which primarily affects rodents and is transmitted to humans through the bites of infected fleas."],

    "is coronavirus deadly": ["Coronavirus, also known as COVID-19, can be fatal, especially for those who are elderly, immunocompromised, or have underlying health conditions. However, the severity of the illness can vary widely from person to person. Many people who contract the virus experience only mild to moderate symptoms and recover without needing hospitalization. It's important to take preventative measures such as getting vaccinated, wearing masks, and practicing good hygiene to reduce the risk of contracting or spreading the virus."],

    "is coronavirus in the air": ["Coronavirus, also known as COVID-19, can be spread through respiratory droplets that are released when an infected person talks, coughs, or sneezes. These droplets can land on surfaces and objects and can also remain in the air for a short period of time. However, the virus is not considered to be airborne in the sense that it can float around in the air for long distances and time like the measles virus. The risk of airborne transmission can be reduced by taking precautions such as wearing masks, practicing social distancing, improving ventilation, and avoiding crowded indoor spaces with poor ventilation."],

    "is coronavirus more contagious than flu": ["Yes, coronavirus, also known as COVID-19, is generally considered to be more contagious than the flu. COVID-19 spreads more easily from person to person through respiratory droplets, which can be released when an infected person talks, coughs, or sneezes. Additionally, people infected with COVID-19 may be contagious for a longer period of time than those infected with the flu. The level of contagiousness can vary depending on various factors such as the specific strain of the virus, the level of immunity in the population, and the measures taken to prevent the spread of the disease."],

    "is coronavirus seasonal": ["There is some evidence to suggest that coronavirus, also known as COVID-19, may have seasonal patterns, similar to other respiratory viruses such as the flu. However, much is still unknown about the virus, and its seasonality may depend on various factors such as the specific strain of the virus and local weather conditions. The virus has shown to spread rapidly during colder months in some regions, while in other regions, it has spread during warmer months. In any case, it's important to continue taking preventative measures such as getting vaccinated, wearing masks, practicing good hygiene, and following local public health guidelines to reduce the risk of contracting or spreading the virus"],

    "is coronavirus the flu": ["Coronavirus, also known as COVID-19, is not the same as the flu, although they share some similar symptoms. COVID-19 is caused by a different virus than the flu, and it can lead to more severe illness in some cases. COVID-19 and the flu are both respiratory illnesses that can spread from person to person, but COVID-19 appears to be more contagious than the flu, and it has caused more widespread illness and death in recent years. While there are vaccines available for both COVID-19 and the flu, they are different vaccines designed to protect against different viruses. It's important to take precautions to prevent the spread of both COVID-19 and the flu, including getting vaccinated, wearing masks, practicing good hygiene, and following local public health guidelines."],

    "what is the difference between coronavirus and covid 19": ["Coronavirus and COVID-19 are related, but they refer to different things. Coronavirus is a large family of viruses that can cause illness in animals and humans. COVID-19, on the other hand, is a specific illness caused by the SARS-CoV-2 virus, which is a type of coronavirus. COVID-19 is a respiratory illness that can cause a range of symptoms, from mild to severe, and can lead to serious complications and even death, especially for those who are elderly, immunocompromised, or have underlying health conditions. COVID-19 is the official name given by the World Health Organization (WHO) to the illness caused by the SARS-CoV-2 virus."],

    "characteristics of coronavirus": ['''The main characteristics of coronaviruses include:
1.	Enveloped virus: Coronaviruses have an envelope that surrounds the virus particles, which is derived from the host cell.
2.	Spike proteins: These viruses have spike proteins on their surface that give them their characteristic "crown" appearance under a microscope.
3.	RNA virus: Coronaviruses are RNA viruses, which means that their genetic material is made up of ribonucleic acid (RNA).
4.	Zoonotic transmission: Some coronaviruses can be transmitted from animals to humans, such as the SARS-CoV-2 virus that causes COVID-19.
5.	Respiratory illness: Coronaviruses can cause respiratory illnesses ranging from mild colds to severe pneumonia and acute respiratory distress syndrome (ARDS).
6.	Person-to-person transmission: Coronaviruses can be transmitted from person to person through respiratory droplets when an infected person talks, coughs, or sneezes.
7.	Incubation period: The incubation period for coronaviruses can vary from 2 to 14 days, during which an infected person may not show symptoms but can still spread the virus to others.
It's important to note that different strains of coronaviruses can have slightly different characteristics, and the severity of illness can vary widely from person to person.'''],

    "what corona virus consists": ["Coronavirus is a type of virus that consists of a genetic material called RNA, which is surrounded by a protein shell. The virus also has spike proteins on its surface that give it its characteristic crown appearance under a microscope. The spike proteins are important for the virus to infect host cells by attaching to receptors on the surface of human cells. Once inside the host cell, the virus uses the cell's machinery to replicate and produce more virus particles, which can then infect other cells and spread throughout the body."],

    "Update me on the corona virus": ['''As I am an AI language model, I do not have real-time access to current news or statistics, but I can provide you with a general update on the COVID-19 pandemic as of my knowledge cut off date of September 2021
The COVID-19 pandemic, caused by the SARS-CoV-2 virus, continues to affect countries around the world. While some regions have made progress in containing the virus through vaccination and public health measures, others are still experiencing high rates of transmission and severe illness.
As of September 2021, there have been over 220 million confirmed cases of COVID-19 and over 4.5 million deaths reported worldwide, according to data from the World Health Organization. Vaccines have been developed and are being distributed globally, with varying levels of success and challenges in vaccine uptake and distribution.
New variants of the virus, including the Delta variant, have emerged and are causing concern due to their increased transmissibility and potential to evade immunity from previous infections or vaccinations.
Public health measures such as mask-wearing, social distancing, and regular handwashing remain important tools in reducing the spread of the virus, along with vaccination. It's important to stay informed and follow the latest guidance from public health officials and medical experts'''],

    "types of corona ": ['''Some of the common types of coronaviruses that infect humans include:
1.	Alpha coronaviruses: This group includes the human coronavirus 229E and the human coronavirus NL63, which can cause mild to moderate respiratory illness.
2.	Beta coronaviruses: This group includes the human coronaviruses OC43 and HKU1, which can cause mild to moderate respiratory illness, as well as the severe acute respiratory syndrome coronavirus (SARS-CoV), which caused an outbreak of severe respiratory illness in 2003.
3.	Gamma coronaviruses: This group includes the avian infectious bronchitis virus and the porcine epidemic diarrhea virus.
4.	Delta coronaviruses: This group includes the Middle East respiratory syndrome coronavirus (MERS-CoV), which caused an outbreak of severe respiratory illness in 2012.
5.	SARS-CoV-2: This is the virus that causes COVID-19, which emerged in late 2019 and has caused a global pandemic.'''],

    "what are the Symptoms": ['''The symptoms of COVID-19 can vary from person to person, and some individuals may experience no symptoms at all. However, the most common symptoms of COVID-19 include:
1.	Fever or chills
2.	Cough
3.	Shortness of breath or difficulty breathing
4.	Fatigue
5.	Muscle or body aches
6.	Headache
7.	New loss of taste or smell
8.	Sore throat
9.	Congestion or runny nose
10.	Nausea or vomiting
11.	Diarrhoea
It is important to note that some individuals infected with COVID-19 may experience mild symptoms, while others may experience severe symptoms that require hospitalization. If you are experiencing any of these symptoms, it is important to get tested and follow public health guidelines to prevent the spread of the disease.'''],

 
    "what covid-19 stands for": ["COVID-19 stands for CORONAVIRUS DISEASE 2019. The name reflects the fact that this particular strain of coronavirus (SARS-CoV-2) was first identified in 2019 and is responsible for causing the disease that has spread globally and led to the ongoing pandemic. The World Health Organization (WHO) officially named the disease COVID-19 in February 2020."],

    "What is SARS-CoV-2": ["SARS-CoV-2 is a type of coronavirus that causes COVID-19, a respiratory illness that can range from mild to severe. The virus was first identified in Wuhan, China in December 2019 and has since spread globally, causing a pandemic. SARS-CoV-2 is a member of the same family of viruses as the viruses that caused the SARS outbreak in 2003 and the MERS outbreak in 2012. The virus is transmitted primarily through respiratory droplets when an infected person coughs, sneezes, talks, or breathes, and it can also spread through contact with contaminated surfaces. Symptoms of COVID-19 can include fever, cough, shortness of breath, fatigue, body aches, loss of taste or smell, and sore throat. It's important to take precautions to prevent the spread of SARS-CoV-2 and COVID-19, including getting vaccinated, wearing masks, practicing good hygiene, and following local public health guidelines"],

    "What is the Covid-19 strain virus": ["The COVID-19 strain virus is SARS-CoV-2, which is a type of coronavirus. This particular strain of coronavirus is responsible for causing the COVID-19 pandemic, which has led to millions of infections and deaths globally since it was first identified in late 2019. The SARS-CoV-2 virus is highly contagious and primarily spreads through respiratory droplets when an infected person coughs, sneezes, talks, or breathes. It can also spread through contact with contaminated surfaces. Symptoms of COVID-19 can range from mild to severe and may include fever, cough, shortness of breath, fatigue, body aches, loss of taste or smell, and sore throat. Vaccines have been developed and are being distributed globally to help prevent the spread of SARS-CoV-2 and COVID-19."],

    "Symptoms": ['''The symptoms of COVID-19 can vary from person to person, and some individuals may experience no symptoms at all. However, the most common symptoms of COVID-19 include:
1.	Fever or chills
2.	Cough
3.	Shortness of breath or difficulty breathing
4.	Fatigue
5.	Muscle or body aches
6.	Headache
7.	New loss of taste or smell
8.	Sore throat
9.	Congestion or runny nose
10.	Nausea or vomiting
11.	Diarrhoea
It is important to note that some individuals infected with COVID-19 may experience mild symptoms, while others may experience severe symptoms that require hospitalization. If you are experiencing any of these symptoms, it is important to get tested and follow public health guidelines to prevent the spread of the disease.'''],

   "what are the precautions that need to be maintained": ['''To help prevent the spread of COVID-19, it is important to take the following precautions:
1.	Get vaccinated: COVID-19 vaccines have been shown to be safe and effective in preventing COVID-19, including severe illness and hospitalization.
2.	Wear a mask: Wear a mask that covers your nose and mouth when in public places or around others who are not part of your household.
3.	Practice social distancing: Maintain at least six feet of distance from others who are not part of your household, both indoors and outdoors.
4.	Wash your hands frequently: Use soap and water for at least 20 seconds, or use hand sanitizer that contains at least 60% alcohol.
5.	Avoid large gatherings: Crowded indoor spaces, particularly those with poor ventilation, increase the risk of COVID-19 transmission.
6.	Stay home if you are sick: If you have symptoms of COVID-19, have tested positive for COVID-19, or have been in close contact with someone who has tested positive, stay home and follow public health guidelines for self-isolation and quarantine.
7.	Practice respiratory etiquette: Cover your mouth and nose with a tissue or your elbow when coughing or sneezing, and dispose of used tissues in a trash can.
By taking these precautions, you can help protect yourself and others from COVID-19.'''],

    "treatment for covid": ['''Most people with COVID-19 have mild to moderate symptoms and can recover at home with self-care measures such as getting plenty of rest, staying hydrated, and taking over-the-counter pain and fever medications.
For those with more severe symptoms or who are at higher risk of developing complications, such as older adults or those with underlying health conditions, medical treatment may be necessary. Some of the treatments that have been used to manage COVID-19 include:
1.	Oxygen therapy: For those experiencing difficulty breathing or low oxygen levels, supplemental oxygen may be provided through a mask or nasal cannula.
2.	Remdesivir: An antiviral medication that has been shown to reduce the duration of hospital stays for some patients.
3.	Dexamethasone: A steroid medication that has been shown to reduce mortality in patients with severe COVID-19.
4.	Convalescent plasma: Blood plasma from people who have recovered from COVID-19 may be given to patients to boost their immune response.
5.	Monoclonal antibodies: Lab-made proteins that mimic the immune system's ability to fight off the virus may be given to patients who are at high risk of developing severe disease.
It's important to note that the best treatment approach may vary depending on the individual cases.'''],

    "hospitals near me": ["I'm sorry, but as an AI language model, I do not have access to your location information. However, you can easily search for hospitals near your location using any search engine or maps application on your device. Simply type HOSPITALS NEAR ME in the search bar, and the search engine or maps application will provide you with a list of hospitals in your area. You can also use your device's GPS to find nearby hospitals. Additionally, you can contact your local health department or emergency services for information on hospitals in your area"],

    "how covid-19 started": ["The exact origins of COVID-19, the disease caused by the novel coronavirus, are still not entirely clear. However, it is believed that the virus originated in bats and may have been transmitted to humans through an intermediate animal host, possibly a pangolin."],

    "does coronavirus come from bats": ['''It is believed that the novel coronavirus responsible for COVID-19 originated in bats. The virus is a type of coronavirus known as SARS-CoV-2, and genetic analyses suggest that it is closely related to coronaviruses found in bats. However, it is not entirely clear how the virus was transmitted to humans.
It is possible that the virus was transmitted directly from bats to humans, or that it passed through an intermediate host animal, such as a pangolin, before being transmitted to humans. The initial outbreak of COVID-19 was first identified in Wuhan, China, in December 2019, and the first cases were linked to a seafood market where live animals were also sold.'''],

    "medicines for covid": ['''As an AI language model, I can provide general information on medicine for COVID-19, but I cannot prescribe specific treatments or medications. It is important to consult with a healthcare professional for personalized medical advice.
Currently, there are several medications approved for emergency use or under investigation for the treatment of COVID-19. These include:
1.	Remdesivir: An antiviral medication that has been approved for emergency use by the FDA to treat hospitalized patients with severe COVID-19.
2.	Dexamethasone: A corticosteroid medication that has been shown to reduce mortality in hospitalized COVID-19 patients requiring oxygen or mechanical ventilation.
3.	Monoclonal antibodies: These are laboratory-made proteins that mimic the immune system ability to fight off viruses. Several monoclonal antibody treatments have been approved for emergency use to treat mild to moderate COVID-19 in high-risk individuals.
4.	Convalescent plasma: A treatment that involves transfusing plasma from recovered COVID-19 patients to sick patients. It is used to provide passive immunity to the sick patient.
It is important to note that while these medications have shown promise in treating COVID-19, they may not be effective for everyone and their use should be guided by a healthcare professional'''],

    "How can i get infected": ['''As an AI language model, I cannot provide information on how to intentionally get infected with a disease or virus. In fact, it is not recommended to intentionally put yourself at risk of infection, as it can lead to serious health consequences and can also harm others around you.
Instead, I would suggest taking precautions to prevent the spread of infections and diseases, such as practicing good hygiene, washing your hands regularly, wearing a mask in crowded public spaces, avoiding close contact with sick individuals, and getting vaccinated if there is a vaccine available for the particular disease.'''],

    "How can the corona virus be passed on to another person": ['''The coronavirus, also known as COVID-19, can be passed on to another person through respiratory droplets that are produced when an infected person talks, coughs, or sneezes. These droplets can land in the mouth or nose of people nearby, or they can be inhaled into the lungs. The virus can also be spread by touching a surface or object contaminated with the virus and then touching one's mouth, nose, or eyes.
It's important to note that the virus is most contagious when a person is showing symptoms, but it is still possible for people who are asymptomatic (not showing any symptoms) to spread the virus. That's why it's important to practice good hygiene, wear masks, practice physical distancing, and follow other public health guidelines to reduce the risk of transmission.'''],

    "is covid-19 a retrovirus": ['''No, COVID-19 is not a retrovirus. It is caused by a type of virus called a coronavirus, specifically the SARS-CoV-2 virus. Retroviruses, on the other hand, are a different type of virus that use a unique mechanism to replicate their genetic material inside the host cell.
Coronaviruses are a family of viruses that can cause illness in humans and animals. COVID-19 is a respiratory illness that was first identified in Wuhan, China in 2019 and has since become a global pandemic. It is a single-stranded RNA virus, meaning its genetic material is made up of RNA rather than DNA, and it has a unique spike protein on its surface that allows it to enter human cells.
It's important to note that while COVID-19 is not a retrovirus, it is still a serious and potentially deadly illness, and it is important to take precautions to prevent its spread.'''],

    "did coronavirus come from eating bats": ['''The exact origin of the coronavirus (COVID-19) is not yet fully understood, but it is believed to have originated from bats. However, it is not accurate to say that the virus came directly from eating bats.
There are several theories about how the virus first crossed over to humans. One theory is that the virus may have been transmitted to humans through an intermediate host, such as a pangolin, that was sold at a wet market in Wuhan, China where the outbreak was first identified. Another theory is that the virus may have accidentally escaped from a laboratory in Wuhan, although this theory is not supported by the available evidence.
Bats are known to carry a variety of viruses, and they are believed to be the natural reservoir for several types of coronaviruses. However, it is important to note that not all bats carry viruses, and not all viruses that infect bats can infect humans. It is also important to note that eating bats is not a common practice in most parts of the world.'''],

    "did coronavirus came from wuhan lab": ["The exact origin of the coronavirus (COVID-19) is still under investigation, and there is currently no conclusive evidence to suggest that it originated from a laboratory in Wuhan, China. While there have been some reports and speculations about the possibility of a laboratory origin, the most widely accepted theory is that the virus likely originated from bats and then transmitted to humans through an intermediate host, such as a pangolin, that was sold at a wet market in Wuhan."],

    "did coronavirus come from pangolins": ['''The exact origin of the coronavirus (COVID-19) is still being studied, but it is believed that the virus may have originated in bats and then transmitted to humans through an intermediate host. While the exact intermediate host is still not confirmed, recent research suggests that pangolins may have played a role.
Pangolins are mammals that are often illegally trafficked for their meat and scales. A study published in the journal Nature in 2020 found that the SARS-CoV-2 virus, which causes COVID-19, has a very similar receptor-binding domain to a coronavirus found in smuggled pangolins. This suggests that pangolins may have been an intermediate host that facilitated the transmission of the virus from bats to humans.'''],

    "does coronavirus mutate": ['''Yes, the coronavirus (COVID-19) has undergone multiple mutations since it was first identified in late 2019. Like all viruses, the coronavirus has a natural tendency to mutate as it replicates and spreads, and new variants of the virus have emerged over time.
Some of the most well-known variants of the coronavirus include the Alpha (B.1.1.7), Beta (B.1.351), Gamma (P.1), and Delta (B.1.617.2) variants. These variants have different mutations in the virus spike protein, which can affect how the virus spreads and how effective vaccines and treatments are against it.
It is important to note that while the virus has mutated, the basic public health measures to prevent its spread, such as practicing good hygiene, wearing masks, practicing physical distancing, and getting vaccinated, remain effective in reducing the risk of infection and transmission. Vaccines have also been modified to provide protection against the new variants of the virus. However, it is still important to closely monitor the situation and take appropriate measures to control the spread of the virus and its variants.'''],

    "does corona effects on eyesight ": ['''There is growing evidence to suggest that the coronavirus (COVID-19) can have an impact on eyesight. Some individuals who have been infected with the virus have reported experiencing eye-related symptoms such as conjunctivitis (also known as pink eye), blurred vision, light sensitivity, and eye pain.
In some cases, the virus has been detected in the tears and conjunctival secretions of infected individuals, indicating that the virus can infect the eye. However, it is important to note that eye-related symptoms are relatively rare and are not typically the primary symptoms of COVID-19.'''],

    "Can you provide me with the emergency numbers": ["For India: 112 or 100.It is important to remember that in case of an emergency, you should always dial the emergency number specific to your country or region for immediate assistance."],

    "Coronavirus rapid response": ['''The coronavirus (COVID-19) pandemic has required a rapid response from governments, healthcare professionals, and individuals around the world. Some of the key elements of the rapid response to COVID-19 have included:
1.	Identification and containment: When the virus was first identified, public health officials worked quickly to identify cases and contain the spread of the virus. This included measures such as contact tracing, quarantine, and isolation.
2.	Testing and treatment: Healthcare professionals developed tests to identify cases of COVID-19 and worked to develop treatments and therapies to help individuals who were infected.
3.	Vaccine development and distribution: Multiple vaccines have been developed and authorized for emergency use to prevent the spread of COVID-19. Governments and healthcare systems have worked to distribute vaccines to as many people as possible.
4.	Public health messaging and guidelines: Governments and public health officials have provided guidance and information to the public about how to prevent the spread of COVID-19. This has included measures such as wearing masks, practicing physical distancing, and frequent hand washing.
5.	Research: Scientists and researchers around the world have been working to better understand COVID-19 and develop new treatments and therapies.
The rapid response to COVID-19 has been a coordinated effort across many different sectors, and ongoing efforts are needed to continue to control the spread of the virus and its variants.'''],

    "how coronavirus get transmitted": ['''The coronavirus, also known as COVID-19, can be transmitted in several ways. The most common mode of transmission is through respiratory droplets that are released when an infected person talks, coughs, or sneezes. These droplets can land on the mouth or nose of someone nearby, or they can be inhaled into the lungs.
The virus can also spread by touching a surface contaminated with the virus and then touching one face, particularly the mouth, nose, or eyes. Although this mode of transmission is less common, it is still a risk factor, especially in areas with high infection rates.
Additionally, the virus can spread through close contact with an infected person, such as hugging, kissing, or sharing personal items like utensils or towels. The risk of transmission is higher in crowded, poorly ventilated indoor spaces where people are in close proximity to each other.
To prevent the spread of the virus, it is important to practice good hygiene, wear a mask in public settings, maintain physical distance from others, and avoid large gatherings. Vaccination is also an effective way to reduce the risk of infection and severe illness from COVID-19.'''],

    "How can i get infected": ["You can become infected with the coronavirus by coming into contact with the virus. The virus is primarily spread through respiratory droplets that are produced when an infected person talks, coughs, or sneezes. You can inhale these droplets or they can land on surfaces that you touch, allowing the virus to enter your body through your nose, mouth, or eyes when you touch your face."],

    "how much will be the cost of vaccine": ['''The cost of the COVID-19 vaccine can vary depending on the country, the manufacturer, and the type of vaccine. In some countries, the vaccine may be provided for free or at a reduced cost to eligible individuals, while in others it may be sold at a market rate. Additionally, governments or international organizations may negotiate with manufacturers to procure vaccines at a lower cost.
                                             As an AI language model, I do not have up-to-date information on the current cost of the COVID-19 vaccine. I recommend checking with your local health authorities or government agencies to find out more information on the availability and cost of COVID-19 vaccines in your area.'''],

    "vaccination centre near me": ["As an AI language model, I do not have access to your location information. However, you can search for vaccination centres near you by using a search engine or visiting your local health department's website."],

    "what are the vaccines for covid": ['''Some of the COVID-19 vaccines that have been authorized for emergency use include:
•	Pfizer-BioNTech COVID-19 vaccine
•	Moderna COVID-19 vaccine
•	AstraZeneca COVID-19 vaccine
•	Johnson & Johnson COVID-19 vaccine
•	Sinovac COVID-19 vaccine
•	Sputnik V COVID-19 vaccine
•	Bharat Biotech COVID-19 vaccine
It is important to note that the availability of these vaccines may vary depending on the country or region, and the eligibility criteria for receiving the vaccine may also differ.'''],

    "which is the best vaccine for covid": ['''All COVID-19 vaccines that have been authorized for emergency use have been shown to be safe and effective in clinical trials. Each vaccine may have different efficacy rates, side effects, and storage requirements, and the best vaccine for an individual may depend on several factors, such as their age, health status, and availability of the vaccine in their region.
Therefore, I would recommend consulting with your healthcare provider or local health authorities to determine which vaccine may be the best option for you based on your individual circumstances'''],

    "what are the number of deaths and cases": ['''As of my knowledge cut-off in 2021, the COVID-19 pandemic has resulted in over 200 million confirmed cases and more than 4.6 million deaths worldwide. However, it is important to note that these numbers are constantly changing as new cases and deaths are reported.
The number of cases and deaths can vary widely between countries and regions depending on factors such as the effectiveness of public health measures, the availability of healthcare resources, and the age and health status of the population.'''],

    "does corona virus kill animal": ['''The SARS-CoV-2 virus, which causes COVID-19 in humans, has been shown to infect some animals as well. While some animals have been known to get infected with the virus, the severity of the disease and the mortality rate varies between species.
Several cases of COVID-19 have been reported in animals such as dogs, cats, minks, tigers, lions, and even some zoo animals. In some cases, the infected animals have developed mild symptoms, while in others, the disease has been severe and even fatal.''']

    
    





    
}