#Symptoms Checker - Short Version
DISEASES = {
    "Cold":["runny nose","sore throat","sneezing"],
    "Flu":["fever", "body aches","fatigue","headache"],
    "Allergies":["sneezing","itchy eyes","runny nose"]
}
def check():
    #1. Get and clean user input
    s = input("Enter symptoms (comma-separated):").lower().split(',')
    user_symptoms = {i.strip() for i in s if i.strip()}

    #2. Match symptoms to diseases
    matches = {}
    for disease, symptoms in DISEASES.items():
        #Find the intersection (common elements) between sets
        matched_count = len(user_symptoms.intersection(set(symptoms)))
        if matched_count>0:
            matches[disease] = matched_count
    #3. Output results
            print("\n--- Potential Diagnosis ---")
            if matches:
                #Sort by match count, descending
                sorted_results = sorted(matches.items(), key=lambda item:item[1], reverse=True)
                for disease, count in sorted_results:
                    print(f"-**{disease}**:{count} match(es).")
                else:
                    print("No matches found in the current database.")

if __name__== "__main__":
        check()
