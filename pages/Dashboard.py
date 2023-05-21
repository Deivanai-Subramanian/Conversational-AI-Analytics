import pandas as pd
import plotly.express as px
import streamlit as st

# ---- READ EXCEL ----
df = pd.read_csv('Dataset.csv')
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- MAINPAGE ----
st.title("Amazon Sales Dashboard")
st.markdown("**Website:** https://www.amazon.in/ ")
st.markdown("##")

if st.session_state['LOGGED_IN'] == True:
	st.write("WELCOME!")
    	# ---- DATA FILTER ----
	    st.subheader("Filter Here:")
	    Main_category = st.multiselect(
		"Select the Main Category:",
		options=df["main_category"].unique(),
		default=df["main_category"].unique()
	    )
	    df_main_category = df.query("main_category == @Main_category")
	    Sub_category = st.multiselect(
		"Select the Sub-Category:",
		options=df_main_category["sub_category"].unique(),
		default=df_main_category["sub_category"].unique()
	    )

	    if((len(Main_category)==0) or (len(Sub_category)==0)):
		st.error("Select Minimum One Attributes")

	    df_selection = df.query(
		"main_category == @Main_category & sub_category ==@Sub_category
	    )
	    st.markdown("##")

	    #TOP KPI's
	    total_turnover = round(df_selection["actual_price"].sum(),2)
	    average_rating = round(df_selection["ratings"].mean(), 1)
	    star_rating = ":star:" * int(round(average_rating, 0))
	    No_of_ratings = round(df_selection["no_of_ratings"].sum(),0)

	    left_column, middle_column, right_column = st.columns(3)
	    with left_column:
		st.subheader("Total Turnover:")
		st.subheader(f"INR ₹{total_turnover}")
	    with middle_column:
		st.subheader("Average Rating:")
		st.subheader(f"{average_rating} {star_rating}")
	    with right_column:
		st.subheader("Total No. of Ratings:")
		st.subheader(f" {No_of_ratings}")

	    st.markdown("""---""")

	    # SALES BY PRODUCT LINE [BAR CHART]
	    sales_by_product_maincategory = (
		df_selection.groupby(by=["main_category"]).sum()[["no_of_ratings"]].sort_values(by="no_of_ratings")
	    )
	    fig_product_sales_by_main = px.bar(
		sales_by_product_maincategory,
		x="no_of_ratings",
		y=sales_by_product_maincategory.index,
		orientation="h",
		title="<b>Sales by Product Main Category</b>",
		color_discrete_sequence=["#0083B8"] * len(sales_by_product_maincategory),
		template="plotly_white",
	    )
	    fig_product_sales_by_main.update_layout(
		plot_bgcolor="rgba(0,0,0,0)",
		xaxis=(dict(showgrid=False))
	    )

	    # SALES BY HOUR [BAR CHART]
	    sales_by_hour = df_selection.groupby(by=["ratings"]).sum()[["no_of_ratings"]]
	    fig_hourly_sales = px.bar(
		sales_by_hour,
		x=sales_by_hour.index,
		y="no_of_ratings",
		title="<b>Ratings by No.of Ratings</b>",
		color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
		template="plotly_white",
	    )
	    fig_hourly_sales.update_layout(
		xaxis=dict(tickmode="linear"),
		plot_bgcolor="rgba(0,0,0,0)",
		yaxis=(dict(showgrid=False)),
	    )

	    left_column, right_column = st.columns(2)
	    left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
	    right_column.plotly_chart(fig_product_sales_by_main, use_container_width=True)

	    # SALES BY PRODUCT LINE [BAR CHART]
	    sales_by_product_subcategory = (
		df_selection.groupby(by=["sub_category"]).sum()[["no_of_ratings"]].sort_values(by="no_of_ratings")
	    )
	    fig_product_sales_by_sub = px.bar(
		sales_by_product_subcategory,
		x="no_of_ratings",
		y=sales_by_product_subcategory.index,
		orientation="h",
		title="<b>Sales by Product Sub-Category</b>",
		color_discrete_sequence=["#0083B8"] * len(sales_by_product_subcategory),
		template="plotly_white",
	    )
	    fig_product_sales_by_sub.update_layout(
		plot_bgcolor="rgba(0,0,0,0)",
		xaxis=(dict(showgrid=False))
	    )
	    #pie chart
	    rating_1 = round(df_selection["ratings"],0)
	    fig_pie = px.pie(
		sales_by_hour,
		values=sales_by_hour.index,
		names="no_of_ratings",
		title="<b>Product Ratings</b>",
		color_discrete_sequence=["#0083B8"],
		template="plotly_white",
	    )
	    fig_pie.update_layout(
		plot_bgcolor="rgba(0,0,0,0)",
	    )

	    col2,middle_column = st.columns(2)
	    col2.plotly_chart(fig_pie, use_container_width=True)
	    middle_column.plotly_chart(fig_product_sales_by_sub, use_container_width=True)


	    with st.expander("Top 10 Products based on Review"):
		topdf = df_selection.sort_values(by=['ratings', 'no_of_ratings'],ascending=[False, False])
		topdf = topdf.head(10)
		st.table(topdf)

else:
	st.warning("Please Loggin")
