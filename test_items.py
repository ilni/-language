import time
class TestMain(object):
    def test_languages(self,browser):
         link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
         browser.get(link)
         browser.implicitly_wait(5)
         result= browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
         print(result)
         assert result
             
         
        