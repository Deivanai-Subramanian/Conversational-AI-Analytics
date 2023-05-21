import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# ---- READ EXCEL ----
df = pd.read_csv('Dataset.csv')
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("PRODUCT DETAILS")

if st.session_state['LOGGED_IN'] == True:
            selected = option_menu(
                        menu_title=None,  # required
                        options=["Accessories", "Appliances", "Home & Kitchen", "Sports & Fitness"],  # required
                        menu_icon="cast",  # optional
                        default_index=0,  # optional
                        orientation="horizontal",
                    )
            df_accessories = df[(df["main_category"] == "accessories")]
            df_appliances = df[(df["main_category"] == "appliances")]
            df_homekitchen = df[(df["main_category"] == "home & kitchen")]
            df_sportsfitness = df[(df["main_category"] == "sports & fitness")]

            if selected == "Accessories":
                df_accessories = df_accessories.sort_values(by=['ratings', 'no_of_ratings'],ascending=[False, False])
                df_accessories = df_accessories.head(25)
                st.table(df_accessories)

            elif selected == "Appliances":
                df_appliances = df_appliances.sort_values(by=['ratings', 'no_of_ratings'],ascending=[False, False])
                df_appliances = df_appliances.head(25)
                st.table(df_appliances)

            elif selected == "Home & Kitchen":
                df_homekitchen = df_homekitchen.sort_values(by=['ratings', 'no_of_ratings'],ascending=[False, False])
                df_homekitchen = df_homekitchen.head(25)
                st.table(df_homekitchen)

            elif selected == "Sports & Fitness":
                df_sportsfitness = df_sportsfitness.sort_values(by=['ratings', 'no_of_ratings'],ascending=[False, False])
                df_sportsfitness = df_sportsfitness.head(25)
                st.table(df_sportsfitness)

