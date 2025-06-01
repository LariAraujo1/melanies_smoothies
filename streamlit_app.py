# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
#streamlit.title('My Parents New Healthy Diner')
#streamlit.subheader('Breakfast Menu')
# ou st.markdown("### Breakfast Menu")

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw: ")
st.write(
  """ Choose the fruits you want in your custom Smoothie!
  """
    # as 3 aspas permitem a quebra de linha e evita ter que usar o \n
)


# 🥋 Remove the SelectBox
# option = st.selectbox(
#     "What is your favorite fruit?",
#     ("Banana", "Strawberries", "Peaches"),
# )

# st.write("Your favorite fruit is:", option)

# 🥋 Exiba a lista de opções de frutas no seu Streamlit no aplicativo Snowflake (SiS).
# e agora o nome!

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be: ", name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect('Choose up to 5 ingredients:'
, my_dataframe
, max_selections=5)
# st.write() - quando quiser mostrar qualquer conteúdo de forma automática, formatada e bonitinha.
#st.write(ingredients_list)

# st.text() - Exibe texto sem formatação, tipo um bloco de notas. Não interpreta markdown, HTML, nem dá estilo.
#st.text(ingredients_list) 

# pra deixar mais bonitinho
# if ingredients_list:
#     st.markdown("### 🍓 Seu Smoothie terá:")
#     for item in ingredients_list:
#         st.markdown(f"- 🥤 {item}")
# else:
#     st.info("Nenhum ingrediente selecionado ainda.")

# 2- caixa verde com os ingredientes escolhidos
#st.success(f"🍹 Ingredientes: {', '.join(ingredients_list)}")

  
# -----------------------------------------------------------------------------------

# aplicar um bloco if 

# if ingredients_list:
#     st.write(ingredients_list)
#     st.text(ingredients_list) 

#     ingredients_string = ''

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen
       
#     st.write(ingredients_String)

# O comando st.write() deve fazer parte do bloco IF, mas não do loop FOR.
# Você pode experimentá-lo como parte do loop FOR e ver um resultado interessante. 
# Em ambos os casos, você verá que o resultado precisará de algum trabalho adicional.
# Não se preocupe, melhoraremos um pouco a aparência da string no próximo laboratório. 
# ------------------------------------------------------------------------------------------

# SEM O BOTÂO SUBMIT

# if ingredients_list:
   

#     ingredients_string = ''

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen + ' '
       
#     st.write(ingredients_string)

#     my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
#             values ('""" + ingredients_string + """')"""

#     st.write(my_insert_stmt)

#     #Insert the Order into Snowflake
#     if ingredients_string:
#         session.sql(my_insert_stmt).collect()
#         st.success('Your Smoothie is ordered!', icon="✅")

    
#-------------------------------------------------------------------------------------------------
 
if ingredients_list:
   

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
       
    st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+ """')"""


    # st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success("✅ " + 'Your Smoothie is ordered, '+ name_on_order+'!')


# display smoothiefroot nutrition information
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
#st.text(smoothiefroot_response.json())
sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)



