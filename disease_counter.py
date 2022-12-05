import streamlit as st
from pymed import PubMed
import pandas as pd

st.title('GoLem Pharm')
st.write('')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(step=1,
    label = 'Select a number of abstracts ',
    min_value=0, max_value=10000, value=1000)

#input box
int_put = st.text_input('Ask about your disease here:')
if int_put:
   with st.spinner('Please wait...'):

    text = int_put
    max1 =int(add_slider)  # ilosc zapytan ze slidera

    #wporwadzenie zapytania do pubmed
    pubmed = PubMed(tool="MyTool", email="p.karabowicz@gmail.com")
    results1 = pubmed.query(text, max_results=max1)
    lista_abstract_3=[]
    for i in results1:
          lista_abstract_3.append(i.abstract)

    df_abstract = pd.DataFrame(lista_abstract_3, columns = ['abstracts'])
    df_abstract['abstracts_lower'] = df_abstract['abstracts'].str.lower()
    df_abstract_1 = df_abstract.dropna()
    #df_abstract_1

    Not_none_values = filter(None.__ne__, lista_abstract_3)
    list_of_values = list(Not_none_values)
    list_of_values = ' '.join(list_of_values)
    text = str(list_of_values)
    text = text.lower()

    df_drug = pd.read_csv('./humand.csv')

    list_drug = set(list(df_drug['Disease']))
    list_drug = list(list_drug)
    list_drug_lower = [x.lower() for x in list_drug]
    def word_count(str):
     counts = dict()
     words = str.split()

     for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

     return counts
    ww = word_count(text)
    gen = []
    val = []

    for k in ww.keys() & set(list_drug_lower):
     gen.append(k)
     val.append(ww[k])
    df = pd.DataFrame(list(zip(gen, val)), columns =['Name', 'value'])
   st.write('your results for request: ', int_put)
   st.balloons()
   df
