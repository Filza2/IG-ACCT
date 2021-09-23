try:
	import requests,secrets,random,os
	from user_agent import generate_user_agent
except Exception as B:
	err='[Please Download] <requests,secrets,random,user_agent,os> if You dont have it already lib Name:\n'+str(B)
	exit(err)
def Test_account():
	global username,pess,email
	print("[/] Trying To Login into Account")
	headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '321','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YMEcQAALAAEv7JAHx0HGAT9oOg5e; ig_did=BBD1FACB-65E8-433F-BB27-1554B5DC41E6; ig_nrcb=1; shbid=13126; shbts=1624283106.1767957; rur=PRN; csrftoken=kKQkGJjUqYTQVCewP9FEp6SZypK8iiSt','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','x-asbd-id': '437806','x-csrftoken': 'kKQkGJjUqYTQVCewP9FEp6SZypK8iiSt','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgSX-','x-instagram-ajax': 'a90c0f3c9877','x-requested-with': 'XMLHttpRequest',}
	data={'username': username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pess}','queryParams': '{}','optIntoOneTap': 'false','stopDeletionNonce': '','trustedDeviceRecords': '{}',}  
	GO=requests.post('https://www.instagram.com/accounts/login/ajax/',headers=headers,data=data).text
	if '"authenticated":true' in GO:
		print('[+] Done Login')
		print("[•] Account is Active You can use it")
		print("[$] By @TweakPY ")
		with open('account_insta.txt', 'a') as x:
			inf=str(f"{email}:{pess}\tuser:{username}")
			x.write(inf+'\n')
			x.close
	elif ('"user":true,"authenticated":false')in GO:exit('[-] WRONG PASSWORD')			
	elif ('"user":false') in GO:exit('[?] USERNAME WAS NOT FOUND')
	elif '"checkpoint_required"'in GO:
		print('[+] Done Testing')
		print('[+] Done Login')
		print("[•] Account is Active You can use it")
		print("[$] By @TweakPY ")
		with open('account_insta.txt', 'a') as x:
			inf=str(f"{email}:{pess}\tuser:{username}")
			x.write(inf+'\n')
			x.close
	elif '"authenticated":false,'in GO:exit('[-] wrong username or password ! ')
	else:print("[!!] Error , Retry Later")
def crate_insta():
	global pess,username,email
	Coke=secrets.token_hex(8)*8
	idd='X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
	email=input("[+] Type The Email: ")
	length=(int(9))
	chars="wwertyuiopasdfghjklzxcvbnmq_"
	for user in range(1):
		user=""
		for item in range(length):
			user+=random.choice(chars)
	for password in range(1):
		password=""
		for item in range(length):
			password+=random.choice(chars)
	username=str(user)
	pess=str(password)
	print("[/] Your Username is:",username)
	print("[\] Your Password is:",pess)
	with open('acc_iG_Un.txt', 'a') as x:
		inf=str(f"{email}:{pess}\tuser:{username}")
		x.write(inf+'\n')
		x.close
	head_get_code={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '67','content-type': 'application/x-www-form-urlencoded','cookie': Coke,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(),'x-asbd-id': '437806','x-csrftoken': 'missing','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': 'missing',}
	head={'Host': 'www.instagram.com','Cookie': Coke,'User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': 'missing','X-Instagram-Ajax': 'missing','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '437806','X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k','Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Content-Length': '432','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/accounts/emailsignup/','Te': 'trailers','Connection': 'close'}
	try:
		data_age={'day': '18','month': '11','year': '1999'}
		data_attemp={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pess}','username': username,'first_name': 'BY @TweakPY - @VV1CK','client_id': idd,'seamless_login_enabled': '1','opt_into_one_tap': 'false',}
		data_get_code={'device_id': idd,'email': email}
		req_attemp=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=head,data=data_attemp)
		req_age=requests.post(f'https://www.instagram.com/web/consent/check_age_eligibility/',headers=head,data=data_age)
		print("[#] (Auto) Day:18| Month:11 | Y:1999")
		req_get_code=requests.post(f'https://i.instagram.com/api/v1/accounts/send_verify_email/',headers=head_get_code,data=data_get_code)
		code=input("[?] The Confirmation Code: ")
		data_send_code={'code': code,'device_id': idd,'email': email}
		req_send_code=requests.post(f'https://i.instagram.com/api/v1/accounts/check_confirmation_code/',headers=head_get_code,data=data_send_code)
		try:singup_code=req_send_code.json()['signup_code']
		except:print("[!!] Ops You have a Error Check Your Info\n")
		try:data_crate={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pess}','username': username,'first_name': 'By @TweakPY','month': '11','day': '18','year': '1999','client_id':idd,'seamless_login_enabled': '1','tos_version': 'row','force_sign_up_code': singup_code,}
		except:print(f"[!] Your code , {code} is Not Correct Please Check it And Try Agine")
		req_crate=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/',headers=head,data=data_crate)
		try:
			if '"account_created": true' in req_crate.text:
				print('[+] Done Crate Account ')
				print('[+] Now Trying To Test The Account ')
				Test_account()
			elif "checkpoint_required" in req_crate.text:
				print('[+] Done Crate Account ')
				print('[+] Now Trying To Test The Account ')
				Test_account()
			elif "The IP address you are using has been flagged as an open proxy. If you believe this to be incorrect, please visit https://help.instagram.com/" in req_crate.text:
				print("[!] IP Ban.")
				print("[~] Retry With Another Email + VPN")
				#print(req_crate.text)
			elif "signup_block"==req_crate.json():
				print("[!] IP Ban.")
				print("[~] Retry With Another Email + VPN")
				#print(req_crate.text)
			elif "false"==req_crate.json()['account_created']:
				print("[~] Error in Crateing Account. ")
				print("[-] Retry After A One Min ")
			else:print("[-] Error , Retry Later")
		except:print("[!!] Ops You have a Error Check Your Info\n")
	except:print("[!!] Ops You have a Error Check Your Info\n")
def main():
	White="\033[1;37;40m";red="\033[1;31;40m"
	VV1CK=int(input("""
1/k) [ Kali linux / Windows ]
2/p) [ iphone / android]
Enter your device type : """))
	if VV1CK==1:
		os.system('clear')
		print(red+"""		
 ▄█     ▄██████▄          ▄████████  ▄████████  ▄████████     ███     
███    ███    ███        ███    ███ ███    ███ ███    ███ ▀█████████▄ 
███▌   ███    █▀         ███    ███ ███    █▀  ███    █▀     ▀███▀▀██ 
███▌  ▄███               ███    ███ ███        ███            ███   ▀ 
███▌ ▀▀███ ████▄       ▀███████████ ███        ███            ███     
███    ███    ███        ███    ███ ███    █▄  ███    █▄      ███     
███    ███    ███        ███    ███ ███    ███ ███    ███     ███     
█▀     ████████▀         ███    █▀  ████████▀  ████████▀     ▄████▀
                                                                      
      ▄︻̷̿┻̿═━一 By Filza (@TweakPY | @VV1CK) ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)"""+White);crate_insta()
	else:
		print("""
╦╔═╗  ╔═╗╔═╗╔═╗╔╦╗
║║ ╦  ╠═╣║  ║   ║ 
╩╚═╝  ╩ ╩╚═╝╚═╝ ╩""");crate_insta()
main()