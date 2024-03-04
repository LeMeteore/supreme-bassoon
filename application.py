# import des bibliothèques streamlit et pandas
import streamlit as st
import pandas as pd

st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')


# écriture d'un bout de code sous forme de string
code = '''
class Hello:
    def __init__(self):
        self.name = "Hello DIT"
    def salut(self):
        return "Hello DIT"

h = Hello()
h.hello()
'''

# st.image('./sunrise.jpg', caption='Sunrise by the mountains')

# appel de la fonction code pour afficher le code se trouvant ds la chaine
# de caractère, je peux préciser le langage utilisé
st.code(code, language='python')


# récupération d'un Dataframe à partir d'un fichier Excel
# df = pd.read_excel("patients_list.xlsx")

# tracé d'une courbe
# st.line_chart(df)


df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

# appel de la fonction dataframe pour afficher le dataframe
st.dataframe(df, use_container_width=True)
