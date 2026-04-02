import pytest
from playwright.sync_api import Page, expect
from pages.sauce_pages import SaucePage 

def test_full_shopping_flow(page: Page):
    sauce = SaucePage(page)
    
    sauce.navigate()
    sauce.login("prueba-valida@yopmail.com", "Z0ieeeiz")
    page.pause()
    expect(page).to_have_url("https://sauce-demo.myshopify.com/account")
    
    page.goto("https://sauce-demo.myshopify.com/collections/all")
    sauce.add_products_to_cart(2)
    
    sauce.go_to_checkout()
    

    expect(page).to_have_url(lambda url: "checkouts" in url)

