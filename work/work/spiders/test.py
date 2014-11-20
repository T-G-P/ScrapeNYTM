import json
from validate_email import validate_email

#{"emails": [{"https://www.globaledit.com/company/careers/": ["HR-Marketing@industrialcolor.com", "change.me@globaledit.com"]}]},
#{"emails": [{"http://ordr.in/blog": ["info@ordrin.com", "hackfood@ordr.in", "sam@ordr.in"], "keywords": "(['info', 'JSON', 'job', 'REST'])"}, {"keywords": "(['software'])", "http://ordr.in/about": ["info@ordrin.com", "hackfood@ordr.in", "sam@ordr.in"]}, {"keywords": "(['hiring', 'software', 'resume', 'motivated', 'developer'])", "http://ordr.in/jobs": ["jobs@ordr.in", "jobs@ordrin.com", "info@ordrin.com", "hackfood@ordr.in", "sam@ordr.in"]}, {"keywords": "(['contact', 'software'])", "http://ordr.in/privacypolicy": ["jobs@ordr.in", "jobs@ordrin.com", "info@ordrin.com", "hackfood@ordr.in", "sam@ordr.in"]}]},
#emails: [{url: ['email1','email2'],keywords: ''}]
#Make it so that emails have value associated to them...sl
#ex: tobias@perelste.in: [urls],[keys]
email_file = 'work_emails.txt'
email_dict = {}
keywords = ''
emails = []
json_data=open('work.json')
data = json.load(json_data)
with open(email_file,'a') as f:
    for company in data:
        for stuff in company['emails']:
            for k,v, in stuff.iteritems():
                if isinstance(v,list):
                    emails = v
                elif isinstance(v,str):
                    keywords = v
            for email in emails:
                email = email.replace(' ','')
                email_dict[email] = [k,keywords]
    for email in email_dict.keys():
        if any(ext in email for ext in ['jpg','gmail','example']):
            email_dict.pop(email)
        else:
            is_valid = validate_email(email,verify=True)
            if not is_valid:
                email_dict.pop(email)
        print email
        f.write(email+'\n')
    f.write('Total valid nytm emails:\t'+str(len(email_dict.keys())))
json_data.close()
