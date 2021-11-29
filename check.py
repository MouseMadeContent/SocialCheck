import requests
from colorama import Fore, Back, Style
from random import choice

class ChecK():

    
    def __init__(self):
        self.email = str(input(Fore.CYAN +  "Enter Email: "))
        self.twitter()
        self.instagram()
        self.pinterest()
        self.spotify()


    def PrintT(self):
        print(Fore.GREEN + f"{self.email} =  Linked"+"\n")

    def PrintF(self):
        print(Fore.RED + f"{self.email} = Unlinked"+"\n")

    def twitter(self):
        self.printTarget("Twitter")
        r = requests.Session()  
        url = "https://api.twitter.com/i/users/email_available.json?email="+self.email
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        Host = "api.twitter.com"
        Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        r.headers = {'User-Agent': user_agent}
        r.headers = {'Host': Host}
        r.headers = {'Accept': Accept}
        req = r.get(url).json()
        text = str(req)
        print(text)
        print('')
        if text.find("'valid': False") == True:
            self.PrintT() 
        else:
            self.PrintF()
        

    def printTarget(self,target):
        print("==================")
        print(Fore.MAGENTA + "[+] "+target+" [+]")
        print("")


    def instagram(self):
        self.printTarget("Instagram")
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"email_or_username":self.email}
        req = r.post(url,data=data)
        print('')
        print('')
        if req.text.find("We sent an self.email to")>=0:
            self.PrintT()
        elif req.text.find("password")>=0:
            self.PrintT()
        elif req.text.find("sent")>=0:
            self.PrintT()
        else:
            self.PrintF()
        
        
    def pinterest(self):
        self.printTarget("Pinterest")
        r = requests.Session()
        url = "https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"email_or_username":self.email}
        req = r.post(url,data=data)
        print('')
        print('')
        if req.text.find("We sent an self.email to")>=0:
            self.PrintT()
        elif req.text.find("password")>=0:
            self.PrintT()
        elif req.text.find("sent")>=0:
            self.PrintT()
        else:
            self.PrintF()
   
        
    def spotify(self):
        self.printTarget("Spotify")
        r = requests.Session()
        url = "https://spclient.wg.spotify.com/signup/public/v1/account"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"

        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        
        response = r.get(url,params={"validate": 1, "email": self.email}).json()
        print('')

        if response["status"] == 20:
            self.PrintT()
        else:
            self.PrintF()
            
if __name__ == "__main__":
    print(Fore.MAGENTA + """
             [-] SocialMediaChecker [-]
          [ Twitter - Instagram - Pinterest - Spotify ]  """)

    print(Fore.CYAN + """
  _________             .__       .__  _________ .__                   __    
 /   _____/ ____   ____ |__|____  |  | \_   ___ \|  |__   ____   ____ |  | __
 \_____  \ /  _ \_/ ___\|  \__  \ |  | /    |  \/|  |  \_/ __ \_/ ___\|  |/ /
 /        (  <_> )  \___|  |/ __ \|  |_\    |____|   Y  \  ___/\  \___|    < 
/________/\____/ \_____>__(______/_____/\________/___|__/\_____>\_____>__|___\
      
                        Cody by N3LL4
       """)
    ChecK()


print('')    
print('Press enter to exit .')

