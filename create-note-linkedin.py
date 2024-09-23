import streamlit as st

# Title of the app
st.title("LinkedIn Note Maker")

# Input fields for name and company
name = st.text_input("Enter your name:")
company = st.text_input("Enter the company:")

role = st.radio("Role Applying for", ["Data Scientist", "Data Analyst", "MLE", "Data"])

# Checkbox or button selection
rec_cb = st.checkbox("Recruiter")
mgr_cb = st.checkbox("Manager")
tl_cb = st.checkbox("Tech Lead")
inMail_cb = st.checkbox("In Mail")

if inMail_cb == True:
    domain = st.text_input("Business Domain")
    subject = st.text_input("Subject", value="Passionate About Data: Ready to Make an Impact" )



rec_note = f'''
Hi {name},
I am Sri Charan, pursuing a master's in Advanced Data Analytics at UNT, graduating Dec 2024. I specialize in Python SQL, &, Machine Learning, and I’m looking for {role} roles. Would love to connect and share my resume: https://is.gd/xyMZGf.
Best,
Sri

'''

mgr_note = f'''
Hi {name},
I’m Sri Charan, finishing my master's in Advanced Data Analytics at UNT (Dec 2024). With skills in Python, Machine Learning, and Data Analysis, I’m exploring {role} roles. I’d love to connect and learn about opportunities at {company}. My resume: https://is.gd/xyMZGf.
Thanks,
Sri
'''

tl_note = f'''
Hello {name},
I’m Sri Charan, completing my master's in Advanced Data Analytics at UNT (Dec 2024). I have experience with Python, Machine Learning, and Data Analysis and am seeking {role} roles. Let’s connect and discuss opportunities at {company}. My resume: https://is.gd/xyMZGf.
Best,
Sri
'''

if inMail_cb:

    inMail_Note = f'''
    \n
    Hi {name},

    I hope you're doing well. 

    I’m Sri Charan, pursuing a master's in Advanced Data Analytics at University of North Texas, graduating in December 2024. 

    With the help of data, we can channelize sales to the right customers and catalyze business growth at {company}. I strongly believe that my expertise in technical skills and {domain} business acumen would prosper {company} with strong financials and tremendous improvement in profits. 

    I am skilled in Python, SQL, Alteryx, Data Analysis & Machine Learning. I'm good at finding business insights and trends.  and looking for {role} roles.

    Would love to connect and disuss opportunities in data science. Here is my resume: https://is.gd/xyMZGf.

    Best,\n
    Sri Charan Bodduna \n
    http://www.linkedin.com/in/scb22
    '''

if st.button("Submit"):

    if rec_cb:
        if name and company:
            st.success(rec_note)
        else:
            st.warning("Please fill in both name and company.")
    if mgr_cb:
        if name and company:
            st.success(mgr_note)
        else:
            st.warning("Please fill in both name and company.")
    if tl_cb:
        if name and company:
            st.success(tl_note)
        else:
            st.warning("Please fill in both name and company.")

    if inMail_cb:
        if name and company and domain and subject:
            st.info(subject)
            st.success(inMail_Note)
        else:
            st.warning("Please fill in both name and company.")


else:
    st.warning("Please fill in both name and company.")

