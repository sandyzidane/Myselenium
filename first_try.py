from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://219.223.190.240:8081/test/")
elem = driver.find_element_by_name("url")
elem.send_keys("http://www.ciaoke.com/o2o/6408.htm")
elem.send_keys(Keys.RETURN)

def capture(url, save_fn = "capture.png"):
	browser = webdriver.chrome()
	browser.set_window_size(1200, 900)
	browser.get(url)
	browser.execute_script("""
		(fucntion() {
			var y = 0;
			var step = 100;
			window.scroll(0, 0);

			function f() {
				if (y < document.body.scrollHeight) {
				y = y + step;
				window.scroll(0, y);
				setTimeout(f, 50);
				}
				else {
					window.scroll(0, 0);
					document.title += "scroll-done";
				}
			}

			setTimeout(f, 1000);
			})();
	""")

	for i in xrange(30):
		if "scroll-done" in browser.title:
			break
		time.sleep(1)

	browser.save_screenshot(save_fn)
	browser.close()

if __name__ == "__main__":
	capture("http://www.ciaoke.com/o2o/6408.htm")