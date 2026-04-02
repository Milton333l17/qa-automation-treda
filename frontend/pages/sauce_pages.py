from playwright.sync_api import Page, expect

class SaucePage:
    def __init__(self, page: Page):
        self.page = page
        
        self._user_input = "input[name='customer[email]']"
        self._pass_input = "input[name='customer[password]']"
        self._login_btn = "input[value='Sign In']" 
        self._product_cards = ".product-card"
        self._add_to_cart_btn = "button[name='add']"
        self._cart_icon = "a[href='/cart']"
        self._checkout_btn = "button[name='checkout']"

    def navigate(self):
        self.page.goto("https://sauce-demo.myshopify.com/account/login")

    def login(self, email, password):
        self.page.fill(self._user_input, email)
        self.page.fill(self._pass_input, password)
        self.page.click(self._login_btn)

    def add_products_to_cart(self, count):
    
        for i in range(count):
            self.page.locator(self._product_cards).nth(i).click()
            self.page.click(self._add_to_cart_btn)
            self.page.goto("https://sauce-demo.myshopify.com/collections/all")

    def go_to_checkout(self): 
        self.page.goto("https://sauce-demo.myshopify.com/cart")
        self.page.click(self._checkout_btn)