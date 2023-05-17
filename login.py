import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "pk_prod_27GNYP246PME2HPJZEV7FX35XRX5", 
                    company_name = "Team Tech Aspirants",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.markdown("Your Streamlit Application Begins here!")


if st.session_state['LOGGED_IN'] == True:
	st.write("WELCOME!")
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        if selected == "Home":
	        st.write("WELCOME TO HOME")
        elif selected == "Projects":
	        st.write("WELCOME TO PROJECTS")
        elif selected == "Contact":
	        st.write("WELCOME TO CONTACT")

