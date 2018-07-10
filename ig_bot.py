from selenium import webdriver
import time,datetime,string
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome("chromedriver.exe")
browser.get('https://www.instagram.com/accounts/login/')

user_collect = []
username = "your username account"
password = "your password"
user_collect = ['dasilva.chandra']



def login(username,password):
	time.sleep(2)
	# browser.implicitly_wait(5)
	browser.find_element_by_xpath("//input[@name='username']").send_keys("{}".format(username))
	browser.find_element_by_xpath("//input[@name='password']").send_keys("{}".format(password))
	browser.find_element_by_class_name('_5f5mN').click()	

def profil():
	time.sleep(2)
	browser.implicitly_wait(5)
	browser.find_element_by_xpath(u'//a[text()="Profile"]').click()

def search(target):
	time.sleep(2)
	search = browser.find_element_by_css_selector('input.XTCLo.x3qfX')
	search.send_keys(target)
	time.sleep(2)
	# browser.implicitly_wait(10)
	browser.find_element_by_xpath(u'//span[text()="%s"]' % target).click()

def read_file(file_name):
	with open(file_name) as file_in:
		lines = (line.rstrip() for line in file_in) 
		content = list(line for line in lines if line) # Non-blank lines in a list
	return content

def copy_followers(username):
	search(username)
	time.sleep(3)
	browser.find_element_by_css_selector('a.-nal3').click()
	# input('Scrol out')
	time.sleep(3)
	div = browser.find_element_by_css_selector('div.j6cq2') #mulai dari tag div
	li = div.find_elements_by_tag_name('li') #cari tag li di dalam tag div 
	with open('followers.txt', "w", encoding="utf8") as f:#buka file
		for t in li: #cari tag a di setiap tag li
			a = t.find_elements_by_tag_name('a') 
			button =  t.find_elements_by_tag_name('button')
			time.sleep(1)
			for post in a:
				post_a = post.text
				print(post.text)
				if post_a not in user_collect:
					user_collect.append(post_a)
			for post in button:
				post_span = post.text
				print(post.text)
				if post_span == "Follow":
					print("{} Belum di follow".format(post_a))
					time.sleep(30)
					post.click()
				else:
					print("{} tidak di follow karena sudah follow".format(post_a))	
				
				post_span = ""
				post_a = ""

	if len(user_collect) == 0:
		exit()
	else:
		browser.get('https://www.instagram.com/')
		print(user_collect)



login(username,password)
profil()
for user in user_collect:
	try:
		copy_followers(user)
	except:
		continue