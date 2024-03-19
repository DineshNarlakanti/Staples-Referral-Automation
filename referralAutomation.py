from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from credentials import USERNAME, PASSWORD  # Assuming you've stored your credentials in a separate file

def run_automation_flow(jobid, email, lastName):
    # Initialize the Safari driver
    driver = webdriver.Safari()

    # Open the website
    driver.get("http://e.staples.com/ODQ5LUxYVy0xMjkAAAGQaa_7xSVKgerOva-vjJLWlneNiZ4vE2UXAa_RHU4-NiqZOa2k5z-JuAkU699MFlLdmn7PHBw=")

    # Create a WebDriverWait object
    wait = WebDriverWait(driver, 20)  # Adjust timeout as needed

    # Login process
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'userid')))
    password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'btnActive')))
    login_button.click()

    home_link = wait.until(EC.element_to_be_clickable((By.ID, 'pt1:_UIShome')))
    home_link.click()

    opportunity_link = wait.until(EC.element_to_be_clickable((By.ID, 'itemNode_my_information_OpportunityMarketplace_0')))
    opportunity_link.click()

    # Enter Job ID and press ENTER
    search_field = wait.until(EC.presence_of_element_located((By.ID, 'ojHcmAdvancedSearchBox_omp-adv-srch|input')))
    search_field.send_keys(jobid + Keys.ENTER)

    # Other actions remain the same, just replace the hardcoded values with the parameters
    time.sleep(5)
    job_field = wait.until(EC.element_to_be_clickable((By.ID, 'search-opportunity-card_primary_text_container')))
    job_field.click()

    time.sleep(10)
    dropdown_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[_afrpopid='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:0:jdUpl:UPsp1:dsktMn']")))
    dropdown_button.click()
    
    option_xpath = "//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:0:jdUpl:UPsp1:refCCMi']/td[2]"
    option_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    option_to_select.click()

    # Continue with the rest of the process, including entering the email and last name using the parameters
    time.sleep(10)
    email_input_xpath = "//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:upl1Upl:UPsp1:rgn1Rgn:0:GPmtfr0:0:emaInp::content']"
    email_input_field = wait.until(EC.visibility_of_element_located((By.XPATH, email_input_xpath)))
    email_input_field.send_keys(email)
    time.sleep(5)

    continue_1 = wait.until(EC.element_to_be_clickable((By.ID, '_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:upl1Upl:UPsp1:rgn1Rgn:0:GPcb10')))
    continue_1.click()
    
    lastName_xpath = '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:upl1Upl:UPsp1:rgn1Rgn:0:GPmtfr1:1:i1Rgn:0:i1:0:lnEInp::content"]'
    lastName_xpath = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, lastName_xpath))
    ) 
    lastName_xpath.send_keys(lastName + Keys.ENTER)
    #time.sleep(10)
    
    button_id = "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:upl1Upl:UPsp1:rgn1Rgn:0:GPcb11"
    
    # Wait for the button to be clickable
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, button_id))
    )
    continue_button.click()
    
    
    submit_button_id = "_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:upl1Upl:UPsp1:SPsb2"
    # Wait for the button to be clickable
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, submit_button_id))
    )
    submit_button.click()

    
        # Proceed with clicking the 'Continue' button and any further steps
        # Make sure to correct any mistakes, like reassigning 'lastName_xpath' instead of creating a 'lastName_field'
    
        # Important: Close or quit the driver at the end if you're done with automation
    print(f"Referral for {lastName} for the jobid {jobid} is DONE")
    time.sleep(20)
    driver.quit()


run_automation_flow('4481', 'ash@gmail.com', 'ash')
