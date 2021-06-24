# NewCybAccTeleBot
Hello future panda welcome to the very fun world of figuring out what i was thinking if i dont can remmember to ill add comments but we both know they wont help 
you anyways if you wanna run it on aws you'll have to change the seleneum settings to 

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = "/usr/bin/google-chrome"  # chrome binary location specified here
    driver = webdriver.Chrome(executable_path='/home/ubuntu/PCA/chromedriver', chrome_options=chrome_options)
    
what else right the email part if you start getting auth errors with the email feature use a proxy to login to gmail i used tinyproxy 

yeah thats it goodluck 
