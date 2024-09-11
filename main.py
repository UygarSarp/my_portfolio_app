import streamlit as st

st.set_page_config("wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/stone.png")
st.write("Below you can find some apps that I build in Python."
         " Feel free to contact me!")

with col2:
    st.title("Dwayne (The Rock) Johnson")
    content = """It's about drive, it's about power, we stay hungry, we devour
Put in the work, put in the hours and take what's ours
Black and Samoan in my veins, my culture bangin' with Strange
I change the game so what's my motherfuckin' name? (Rock)
What they gonna get though?
Desecration, defamation, if you wanna bring it to the masses
Face to face now we escalatin' when I have to put boots to asses
Mean on ya like a dream when I'm rumblin'
You're gonna scream, "Mama"
So bring drama to the king Brahma (Then what?)
Comin' at ya' with extreme mana (Ahoo, ahoo, ahoo)"""
    st.write(content)