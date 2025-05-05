from behave import *
from Element_xpath import Register_page
from Element_xpath import Home_page
import time, random
registerobj = Register_page.Register_page()
homeobj = Home_page.Home_page()

@given("user navigate to page and click register")
def step_impl(context):
    context.browser.new_context(viewport={"width":2000 ,"height":2200,"fullscreen": False})
    time.sleep(1)
    context.page.goto("https://ecommerce2.khoavida.com/")
    context.page.locator(homeobj.register_page_top_xpath).click()
    time.sleep(1)

@then("user should be navigated to Register page")
def step_impl(context):
    time.sleep(1)
    title = context.page.locator("//h4").text_content()
    assert title == "Register"
    print(f"User is at {title} page.")
@when("user enter new credential and press enter")
def step_impl(context):
    registerobj.username = "abcdef"
    time.sleep(1)
    registerobj.password = "123321123"
    time.sleep(1)
    random_numb = random.randint(0,100) + random.randint(0,100)
    registerobj.email = f"sdasda{random_numb}sd@gmail.com"
    time.sleep(1)
    registerobj.confirm_password = "asdasvcasc"
    time.sleep(1)
    registerobj.fill_user_infor(context.page)
    time.sleep(1)
    registerobj.get_user_infor(context.page)
    time.sleep(1)
    context.page.click(registerobj.register_button_xpath)
    time.sleep(1)
@then("user should be navigated back to home page")
def step_impl(context):
    print("---OBSERVE---")

@when("user click add to cart iphone and headphone on homepage")
def step_impl(context):
    iphone_order_button = homeobj.iphone_15_pro_max_add_to_cart_xpath
    headphons_order_button = homeobj.sony_wh_1000xm5_headphones_add_to_cart_xpath
    context.page.click(iphone_order_button)
    time.sleep(1)
    context.page.click(headphons_order_button)
    time.sleep(1)


@then("cart logo should increase along with the number of clicks")
def step_impl(context):
    cart_logo_xpath = homeobj.cart_page_top_xpath
    number_item = context.page.locator(cart_logo_xpath).inner_text()
    print(f"Number of item: {number_item}")


@when("user click cart logo on the top right corner")
def step_impl(context):
    cart_logo = context.page.locator(homeobj.cart_page_top_xpath)
    time.sleep(1)
    cart_logo_isClickable = cart_logo.is_clickable()
    print(cart_logo_isClickable)
    if cart_logo_isClickable:
        context.page.click(cart_logo)
    else:
        print("cart logo got error")

@then("user should be navigated to cart page")
def step_impl(context):
    