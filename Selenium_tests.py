from selenium import webdriver


class TestsCompetitions:

    def __init__(self, browser):
        if browser == 'Chrome':
            self.driver = self.init_chrome_web_driver()
            self.driver.set_page_load_timeout(30)
        self.run_test_cases()
        self.driver.quit()

    @staticmethod
    def init_chrome_web_driver():
        return webdriver.Chrome('/Users/Nikita/Downloads/chromedriver')

    def open_page(self):
        self.driver.get("https://lamp.ii.us.edu.pl/~mtdyd/zawody/")

    def run_test_cases(self):

        test_cases = {
            1: 'Brak kwalifikacji', # < 10
            2: 'Skrzat',            # Skrzat
            3: 'Blad danych',       # Skrzat bez zgody
            4: 'Blad danych',       # Skrzat bez zaświadczenia
            5: 'Mlodzik',           # Młodzik
            6: 'Blad danych',       # Młodzik bez zgody
            7: 'Blad danych',       # Młodzik bez zaświadczenia
            8: 'Junior',            # Junior
            9: 'Blad danych',      # Junior bez zgody
            10: 'Blad danych',      # Junior bez zaświadczenia
            11: 'Dorosly',          # Dorosły
            12: 'Senior',           # Senior
            13: 'Blad danych',      # Senior bez zaświadczenia
            14: 'First name must be filled out',     # Obowiązkowe imię
            15: 'Nazwisko musi byc wypelnione',      # Obowiązkowe nazwisko
            16: 'Data urodzenia nie moze byc pusta'  # Obowiązkowa data urodzenia
        }

        for case_number, accepted_result in test_cases.items():
            self.run_case(case_number, accepted_result)

    def run_case(self, case_number, accepted_result):
        self.open_page()
        result = self.set_data_case(case_number)
        state = 'passed' if result == accepted_result else 'failed'
        print(f'Test {case_number} {state} (Expected: {accepted_result}, got: {result})')

    def set_data_case(self, case_number):

        self.clear_inputs()

        self.driver.maximize_window()

        if case_number == 1:  # < 10
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("12-06-2009")
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 2:  # Skrzat
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2008")
            self.driver.find_element_by_id("rodzice").click()
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 3:  # Skrzat bez zgody
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2008")
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 4:  # Skrzat bez zaświadczenia
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2008")
            self.driver.find_element_by_id("rodzice").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 5:  # Młodzik
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2006")
            self.driver.find_element_by_id("rodzice").click()
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 6:  # Młodzik bez zgody
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2006")
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 7:  # Młodzik bez zaświadczenia
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2006")
            self.driver.find_element_by_id("rodzice").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 8:  # Junior
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2003")
            self.driver.find_element_by_id("rodzice").click()
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 9:  # Junior bez zgody
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2003")
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 10:  # Junior bez zaświadczenia
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2003")
            self.driver.find_element_by_id("rodzice").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 11:  # Dorosły
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-04-1984")
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 12:  # Senior
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-04-1939")
            self.driver.find_element_by_id("lekarz").click()
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 13:  # Senior bez zaświadczenia
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-1939")
            self.confirm()
            return self.get_last_alert_text()
        elif case_number == 14:  # Obowiązkowe imię
            self.driver.find_element_by_id("inputEmail3").send_keys("")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2008")
            self.confirm()
            return self.get_first_alert_text()
        elif case_number == 15:  # Obowiązkowe nazwisko
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("")
            self.driver.find_element_by_id("dataU").send_keys("11-03-2008")
            self.confirm()
            return self.get_first_alert_text()
        elif case_number == 16:  # Obowiązkowa data urodzenia
            self.driver.find_element_by_id("inputEmail3").send_keys("Adam")
            self.driver.find_element_by_id("inputPassword3").send_keys("Nowak")
            self.driver.find_element_by_id("dataU").send_keys("")
            self.confirm()
            return self.get_first_alert_text()

    def confirm(self):
        self.driver.find_element_by_css_selector("button.btn.btn-default").click()

    def get_last_alert_text(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def get_first_alert_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def clear_inputs(self):
        self.driver.find_element_by_id("inputEmail3").clear()
        self.driver.find_element_by_id("inputPassword3").clear()
        self.driver.find_element_by_id("dataU").clear()
        if self.driver.find_element_by_id("rodzice").is_selected():
            self.driver.find_element_by_id("rodzice").click()
        if self.driver.find_element_by_id("lekarz").is_selected():
            self.driver.find_element_by_id("lekarz").click()


TestsCompetitions('Chrome')
