import streamlit as st

# Title of the app
st.title("Proposal Questionnaire")

# 1. What is your name?
name = st.text_input("What is your name?")

# 2. Do You know me?
know_me = st.radio("Do you know me?", ('Yes', 'No'))

# If the answer is 'No', ask for an explanation
if know_me == 'No':
    reason_know = st.text_area("Please tell us why you don't know me:", help="This field is mandatory.")
    if not reason_know:
        st.warning("Explanation is mandatory if the answer is 'No'. Please provide a reason.")
else:
    reason_know = None

# 3. Will you die for me?
die_for_me = st.radio("Will you die for me?", ('Yes', 'No'))

# If the answer is 'No', ask for an explanation
if die_for_me == 'No':
    reason_die = st.text_area("Please tell us why you wouldn't die for me:", help="This field is mandatory.")
    if not reason_die:
        st.warning("Explanation is mandatory if the answer is 'No'. Please provide a reason.")
else:
    reason_die = None

# 4. What will you do if I make a kiss, or will you agree if I did it forcefully to that baby fat?
kiss_option = st.radio("If I make a kiss, what will you do?", ('Agree', 'Disagree'))

# Additional option: let them fill in the blank or choose Yes/No
kiss_forced = st.selectbox("Let say I did it forcefully to that baby fat, do you agree?", ['Yes', 'No'])

# 5. If you get an option to choose between hug & kiss, what will you do? (You have to do both)
hug_or_kiss = st.radio("If you had to choose between a hug & a kiss, what will you do?", ('Hug', 'Kiss'))

# 6. Tell me how much you feel you are close to me
closeness = st.slider("How much do you feel you are close to me?", 0, 100, 50)

# Button to submit the answers
submit_button = st.button("Submit")

# Show summary when submitted (if all mandatory fields are filled)
if submit_button:
    if (know_me == 'No' and not reason_know) or (die_for_me == 'No' and not reason_die):
        st.warning("Please provide a reason for your 'No' answer before submitting.")
    else:
        st.subheader("Your Responses:")
        st.write(f"Name: {name}")
        st.write(f"Do you know me? {know_me}")
        if know_me == 'No':
            st.write(f"Reason: {reason_know}")
        st.write(f"Will you die for me? {die_for_me}")
        if die_for_me == 'No':
            st.write(f"Reason: {reason_die}")
        st.write(f"Will you agree with the kiss? {kiss_option}")
        st.write(f"Did you agree if I did it forcefully? {kiss_forced}")
        st.write(f"Choice between hug and kiss: {hug_or_kiss}")
        st.write(f"How close do you feel to me? {closeness}")
