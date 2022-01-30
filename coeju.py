
def executer(course,semester):

    import smtplib
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup as bsp

    fd = pd.DataFrame(columns=['Date','Results'])
    pd.set_option('display.max_colwidth', None)
    r = requests.get('https://www.coeju.com')
    df = bsp(r.content,'html.parser')
    ############ Change to 'Label2' for Notifiations/Circulars ############
    data = df.find('span',{'id':'Label1'})
    #######################################################################
    for ov in data.find_all('td'):
        col = ov.find_all('td')
        if col != []:
            date = col[0].text
            res = col[1].text
            fd = fd.append({'Date':date,'Results':res}, ignore_index=True)
    ######Add Keywords to wordlist #########
    wordlist =[course,semester]
    ########################################
    count =  0
    li =[]
    for result in fd['Results']:
        ######### Change 'any' to 'all' if all words in wordlist must satisify. #############
        if any(word in result for word in wordlist) == True:   
            count = count + 1
            edf =  fd[fd['Results']==result]
            li.append(edf)
            ndf = pd.concat(li)

    def mail():
        msg = """You Have {0} Matching result update(s) on Controller Of Examination JU \n{1} \n\n Visit {2}""".format(count,ndf,'https://coeju.com').encode()
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com',465)
        ########## Enter Usernmame and Password resp. ###############
        smtpobj.login('','')
        ########## Enter 'Frommailid','Tomailid' resp.###############
        smtpobj.sendmail('','',msg)
        
    if count > 0:
        mail()
    ############# Hash it out if you dont need output ###############
        print("Found {} Matching Results :".format(count))
        print(ndf)
        exit()
    return (count)


if __name__=='__main__':
    course,semester = input('Enter Course :'),input('Enter Semester :')
    executer(course,semester)
    







    







