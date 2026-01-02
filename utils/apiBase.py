from http.client import responses

from playwright.sync_api import Playwright
apipayload={  "country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}

class APIUtil:

    def createOrder(self,playwright: Playwright):
        api_request_context = playwright.request.new_context("https://rahulshettyacademy.com")
        response = api_request_context.post( url="/api/ecom/order/create-order",
                                 data=apipayload,
                                 headers={"Authorization": token,
                                     "Content-Type": "application/json"})
        print(response.json())