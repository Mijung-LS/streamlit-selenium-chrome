import streamlit as st


with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            options=options
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    url = "https://www.lme.com/api/trading-data/chart-data?datasourceId=39fabad0-95ca-491b-a733-bcef31818b16&startDate=2024-02-19&endDate=2024-03-17"
    driver.get(url)

    st.code(driver.page_source)
