from selenium import webdriver
from selenium.webdriver.firefox.options import Options, FirefoxProfile

# Caminho para o perfil do Firefox desejado
profile_path = r"C:\Users\XPTO\AppData\Roaming\Mozilla\Firefox\Profiles\XPTO"

# Configura o perfil no GeckoDriver
# options = Options()
# options.set_preference("profile", profile_path)

options = Options()
options.profile = FirefoxProfile(profile_path)
# firefox_profile = FirefoxProfile(profile_path)

# Inicia o WebDriver com o perfil especificado
driver = webdriver.Firefox(options)

# Agora você pode interagir com o navegador Firefox usando o perfil especificado
driver.get("https://www.youtube.com")

# Finaliza o WebDriver ao terminar
driver.quit()