import os
import streamlit as st


st.set_page_config(page_title="Muhammad Danish | Data Scientist Portfolio", layout="wide")


def load_image(image_path):
    if os.path.exists(image_path):
        return image_path
    else:
        st.warning(f"Image not found: {image_path}")
        return None


st.sidebar.title("Danish Portfolio")
section = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Skills", "Contact"])

if section == "Home":
    st.title("Muhammad Danish")
    st.subheader("Data Scientist | Data Analyst")

    col1, col2 = st.columns([1, 2])  

    with col1:
        profile_image_path = os.path.expanduser(r"C:\myimg.jpg")  
        profile_image = load_image(profile_image_path)
        if profile_image:
            st.image(profile_image, width=200, caption="Muhammad Danish")

    with col2:
        st.write("""
            Hello and welcome to my portfolio!  
            I am **Muhammad Danish**, a Data Scientist based in Lahore, Pakistan. I specialize in transforming complex data into actionable insights to solve real-world business problems.

            My expertise includes:
            - Building predictive models and automating workflows.
            - Creating interactive dashboards using **Power BI** and **Tableau**.
            - Leveraging **machine learning** to drive business decisions.

            Explore my **Projects**, **Skills**, and **About Me** sections to learn more about my work!
        """)




elif section == "About Me":
    st.header("About Me")

    col1, col2 = st.columns([1, 2])  
    
    with col1:
        about_image_path = os.path.expanduser(r"C:\myimg.jpg")  
        about_image = load_image(about_image_path)
        if about_image:
            st.image(about_image, width=200, caption="About Me")

    with col2:
        st.subheader("Professional Summary")
        st.write("""
        I am a dedicated and ambitious 5th-semester Data Science student with a solid foundation 
        in data analysis, programming, and quality assurance. My passion lies in ensuring the 
        reliability and efficiency of software systems through rigorous QA processes and testing 
        methodologies.

        Alongside my academic journey, I have gained practical experience in marketing, social media 
        management, and event promotion, showcasing my ability to manage projects and engage diverse audiences. 
        Eager to contribute and grow, I seek opportunities to apply my skills in data-driven solutions, 
        software testing, and quality assurance while gaining hands-on industry experience.
        """)

        st.subheader("Education")
        st.write("""
        - **University of Central Punjab, Lahore**  
          Bachelor of Science in Data Science | 2022 - 2026  
        - **Forman Christian College**  
          F.Sc Pre Engineering | 2019 - 2021  
        - **Allied School(Hazoori Campus)**  
          Matric | 2017 - 2019  
        """)

        st.subheader("Professional Experience")
        st.write("""
        - **Freelancer** (2023 - Present): Completed over 20 projects  
        - **Teaching** (2022 - Present): Working as a teacher  
        - **Capper Soft** (2023 - 2024): Worked as a Junior Data Scientist  
        """)



elif section == "Projects":
    st.header("Projects")

    projects = [
        {
            "title": "Credit Card Dashboard",
            "desc": "Advanced dashboard for predicting credit card sales trends using historical data and machine learning techniques.",
            "tech": "Python, Power BI",
            "link": "https://github.com/Muhammad-Danish12/PRODIGY_DS_01",
            "image": os.path.expanduser(r"C:\prj2.jpg")
        },
        {
            "title": "Blinkit Power BI Project",
            "desc": "Conducted in-depth analysis of grocery data to identify the trends of sales.",
            "tech": "Python, Power BI, Excel",
            "link": "https://github.com/Muhammad-Danish12/Blinkit_Project",
            "image": os.path.expanduser(r"C:\prj3.png")
        },
        {
            "title": "Sales Dashboard Project",
            "desc": "The Sales Dashboard Project is a Power BI initiative designed to analyze and visualize superstore sales data. It provides actionable insights through interactive visualizations and KPIs to enhance business decision-making.",
            "tech": "Python, Scrapy, BeautifulSoup, SQLite",
            "link": "https://github.com/Muhammad-Danish12/sales_project",
            "image": os.path.expanduser(r"C:\sales.jpg")
        }
    ]

    for project in projects:
        with st.expander(project["title"]):  
            project_image = load_image(project["image"])
            if project_image:
                st.image(project_image, width=400, caption=project["title"])
            
            st.write(f"**Description:** {project['desc']}")
            st.write(f"**Technologies Used:** {project['tech']}")
            st.markdown(f"[View Project]({project['link']})")



elif section == "Skills":
    st.header("My Skills")
    skills = {
        "Python": 90,
        "Data Analysis": 90,
        "Machine Learning": 85,
        "Deep Learning": 90,
        "Data Visualization": 88,
        "SQL": 85,
        "Power BI": 95
    }
    for skill, proficiency in skills.items():
        st.write(f"{skill}")
        st.progress(proficiency / 100)


elif section == "Contact":
    st.header("Contact Me")
    

   
    st.write("Feel free to reach out through any of the methods below:")
    st.write("- *Email*: miand7083@gmail.com")
    st.write("- *LinkedIn*: [Muhammad Danish](https://www.linkedin.com/in/muhammad-danish-aa1b95284/)")
    st.write("- *GitHub*: [Muhammad Danish](https://github.com/Muhammad-Danish12)")
    st.write("Alternatively, you can fill out the form below:")
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")
        if submit_button:
            st.success("Thank you for your message! I'll get back to you soon.")

st.sidebar.markdown("---")
st.sidebar.write("Muhammad Danish")