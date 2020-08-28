import framework.base_page


class LoginPage(framework.base_page.BasePage):

    input_userAccount = "x=>//*[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input"
    input_passWord = "x=>//*[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input"
    search_submit_btn = "x=>//*[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/button"
    presentation = "x=>/html/body/div[2]/p"

    def user_account_search(self, text):

        self.type(self.input_userAccount, text)
    def password_search(self, text):

        self.type(self.input_passWord, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def get_real_text(self):
        return self.get_element_text(self.presentation)









