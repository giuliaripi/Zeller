#Author: Giulia ripi
#email: gripi86@gmail.com
#date: 20260618

# Implementazione della formula di zeller per calcolare quale giorno della settimana fosse una specifica data dela passato
#libraries
import streamlit as st
import random

st.title("Guess the weekday")

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# funzione Zeller
def zeller(q, m, Y):
    if m == 1:
        m = 13
        Y -= 1
    elif m == 2:
        m = 14
        Y -= 1

    K = Y % 100
    J = Y // 100

    h = (q + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7
    return days[h]
def new_date():
    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_30_days = months_31_days+[4, 6, 9, 11]
    d=random.randint(1, 31)
    if d==31:
        m=random.choice(months_31_days)
    elif d==30:
        m=random.choice(months_30_days)
    elif d<=28:
        m=random.randint(1,12)
    y=random.randint(1800, 2100)
    return d,m,y 
# initialize

if "date" not in st.session_state:
    st.session_state.date = new_date()

if "score" not in st.session_state:
    st.session_state.score = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

q, m, Y = st.session_state.date

st.subheader(f"Date: {q}/{m}/{Y}")

chioce = st.selectbox("Guess the weekday", days)

# display punteggio
st.write(f"Score: {st.session_state.score}")
st.write(f"Streak: {st.session_state.streak}")

if st.button("Guess"):
    sol = zeller(q, m, Y)

    if chioce == sol:
        st.success("Correct!")

        st.session_state.score += 1
        st.session_state.streak += 1

    else:
        st.error(f"Stupid Nicolò! The correct answer is: {sol}")

        st.session_state.streak = 0  # reset streak

if st.button("New Challenge"):
    st.session_state.date = new_date()
    st.rerun()
   