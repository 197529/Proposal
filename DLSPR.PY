import streamlit as st

# Title of the app
st.title("Proposal Questionnaire")

# 1. What is your name?
name = st.text_input("What is your name?")

# 2. Do You know me?
know_me = st.radio("Do you know me?", ('Yes', 'No'))

# If the answer is 'No', ask for an explanation
if know_me == 'No':
    reason_know = st.text_area("Why babe? What happened?", help="This field is mandatory.")
    if not reason_know:
        st.warning("Explanation is mandatory if the answer is 'No'. Please provide a reason.")
else:
    reason_know = None

# 3. Will you die for me?
die_for_me = st.radio("Will you die for me?", ('Yes', 'No'))

# If the answer is 'No', ask for an explanation
if die_for_me == 'No':
    reason_die = st.text_area("Why babe? What happened?", help="This field is mandatory.")
    if not reason_die:
        st.warning("Explanation is mandatory if the answer is 'No'. Please provide a reason.")
else:
    reason_die = None

# 4. Why don't you love me?
dont_love = st.radio("Why don't you love me?", ('Yes', 'No'))

# If the answer is 'No', ask for an explanation
if dont_love == 'No':
    reason_dont_love = st.text_area("Why don't you love me?", help="This field is mandatory.")
    if not reason_dont_love:
        st.warning("Explanation is mandatory if the answer is 'No'. Please provide a reason.")
else:
    reason_dont_love = None

# 5. Do you love me?
love_me = st.radio("Do you love me?", ('Yes', 'No'))

# If the answer is 'No', ask for an explanation
if love_me == 'No':
    reason_love = st.text_area("Why don't you love me?", help="This field is mandatory.")
    if not reason_love:
        st.warning("Explanation is mandatory if the answer is 'No'. Please provide a reason.")
else:
    reason_love = None

# 6. What will you do if I make a kiss, or will you agree if I did it forcefully to that baby fat?
kiss_option = st.radio("If I make a kiss, what will you do?", ('Agree', 'Disagree'))

# Additional option: let them fill in the blank or choose Yes/No
kiss_forced = st.selectbox("Let say I did it forcefully to that baby fat, do you agree?", ['Yes', 'No'])

# 7. If you get an option to choose between hug & kiss, what will you do? (You have to do both)
hug_or_kiss = st.radio("If you had to choose between a hug & a kiss, what will you do?", ('Hug', 'Kiss'))

# 8. Tell me how much you feel you are close to me
closeness = st.slider("How much do you feel you are close to me?", 0, 100, 50)

# Button to submit the answers
submit_button = st.button("Submit")

# Show summary when submitted (if all mandatory fields are filled)
if submit_button:
    # Check if explanations are provided for "No" responses
    if ((know_me == 'No' and not reason_know) or 
        (die_for_me == 'No' and not reason_die) or
        (dont_love == 'No' and not reason_dont_love) or 
        (love_me == 'No' and not reason_love)):
        st.warning("Please provide an explanation for your 'No' answer before submitting.")
    else:
        # Creating the content for the DLSPR download link
        response_content = f"""
        Proposal Questionnaire Responses:

        1. Name: {name}
        2. Do you know me? {know_me}
        {f"Reason: {reason_know}" if know_me == 'No' else ''}
        3. Will you die for me? {die_for_me}
        {f"Reason: {reason_die}" if die_for_me == 'No' else ''}
        4. Why don't you love me? {dont_love}
        {f"Reason: {reason_dont_love}" if dont_love == 'No' else ''}
        5. Do you love me? {love_me}
        {f"Reason: {reason_love}" if love_me == 'No' else ''}
        6. Will you agree with the kiss? {kiss_option}
        7. Did you agree if I did it forcefully? {kiss_forced}
        8. Choice between hug and kiss: {hug_or_kiss}
        9. How close do you feel to me? {closeness}
        """
        
        # Save the content to a file named DLSPR
        file_path = "DLSPR_proposal_responses.txt"
        with open(file_path, "w") as file:
            file.write(response_content)
        
        # Provide the download link
        st.subheader("Your responses have been saved!")
        st.markdown(f"**Download your responses here:** [Download DLSPR Proposal Responses](/{file_path})")
        
        # Optional: You can also show the responses on screen
        st.write(response_content)
