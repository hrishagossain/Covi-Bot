#Define a function to get medication for user specific symptoms
d=[]
def symptom_list(symptom):
    d.append(symptom)
def medication(d):
    med=[]
    base="As a basic medication , you can follow : "
    if "fever" in d:
        med.append("paracetamol(for adults) and calpol(for children).")
    if "cough" in d:
        med.append("try using vapour")
    if "breath" in d:
        med.append("No specific over-the-counter medication. Seek immediate medical attention.")

    if "fatigue" in d:
        med.append("Get plenty of rest and sleep. Stay hydrated.")

    if "taste_smell" in d:
        med.append("No specific over-the-counter medication. This symptom may resolve on its own.")

    if "throat" in d:
        med.append("Throat lozenges, saltwater gargles, or OTC pain relievers for throat pain")

    if "head" in d:
        med.append("OTC pain relievers such as Acetaminophen (e.g., Tylenol) or Ibuprofen (e.g., Advil, Motrin)")

    if "muscle or body aches" in d:
        med.append("OTC pain relievers such as Acetaminophen (e.g., Tylenol) or Ibuprofen (e.g., Advil, Motrin)")

    if "nose" in d:
        med.append("Decongestant nasal sprays or oral decongestants (e.g., pseudoephedrine)")

    if "dia" in d:
        med.append("OTC anti-diarrheal medications (e.g., loperamide)")
    
    if "chest" in d:
        med.append("Seek immediate medical attention. Medication will depend on the underlying cause.")

    if "body_muscle" in d:
        med.append("OTC pain relievers such as Acetaminophen (e.g., Tylenol) or Ibuprofen (e.g., Advil, Motrin)")

    if "vomit" in d:
        med.append("No specific medication. Maintain hydration and rest.")

    med=list(set(med))
    return base + " ".join(med)

def cheeker():
    des = list(dict.fromkeys(d))
    r=len(des)
    if r>=3:
        if any(word in des for word in ['fever', 'nose', 'cough', 'taste']):
            res="By checking your symptoms, I can say you may have Covid. Start your medications as soon as possible (prescribed by your age). Do maintain Covid precautions. Get well soon."
            rec=res+ medication(des)
            return rec
        else:
            res="By checking your symptoms, I can say you may not have Covid.But if you experience any symptoms like fever or runny nose or cough or loss of taste and smell then you have possibility of having Covid. Do maintain Covid precautions. Get well soon."
            rec=res+ medication(des)
            return rec
    else:
        if any(word in des for word in ['fever', 'nose', 'cough', 'taste']):
            res="By checking your symptoms, I can say you may not have Covid.But your symptom is a strong symptom for Covid.If you experience any further symptoms, start your medications as soon as possible (prescribed by your age). Do maintain Covid precautions. Get well soon."
            rec=res+ medication(des)
            return rec
        res="You probably do not have Covid. If you further experience any difficulties,come back to me or consult nearby doctor."
        rec=res+medication(des)
        return rec
