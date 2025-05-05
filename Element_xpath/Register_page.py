class Register_page():
    username_field_xpath = "(//input[contains(@class,'MuiOutlinedInput-input')])[1]"
    password_field_xpath = "(//input[contains(@class,'MuiOutlinedInput-input')])[3]"
    email_field_xpath = "(//input[contains(@class,'MuiOutlinedInput-input')])[2]"
    confirm_password_field_xpath = "(//input[contains(@class,'MuiOutlinedInput-input')])[4]"
    register_button_xpath = "//button[text()='Register']"
    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.confirm_password = None
    def fill_user_infor(self,context):
        context.fill(self.username_field_xpath, self.username)
        context.fill(self.password_field_xpath, self.password)
        context.fill(self.email_field_xpath, self.email)
        context.fill(self.confirm_password_field_xpath, self.confirm_password)
        time = 0
        while time <= 5:
            time +=1
            if self.password != self.confirm_password:
                print("Passwords do not match\nPlease enter again!".upper())
                self.confirm_password = input("Re-confirm password: ")
            elif self.password == self.confirm_password:
                context.fill(self.confirm_password_field_xpath, self.confirm_password)
                print("Confirm password is correct.")
                break
    def get_user_infor(self,context):
        username = context.input_value(self.username_field_xpath)
        password = context.input_value(self.password_field_xpath)
        email = context.input_value(self.email_field_xpath)
        confirm_password = context.input_value(self.confirm_password_field_xpath)
        print(f"- Username: {username}\n- Password: {password}\n- Email: {email}\n- Confirm password: {confirm_password}")
