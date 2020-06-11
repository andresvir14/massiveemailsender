# massiveemailsender
Python script to send customized emails with an attachment file

With this script you can send thousands of emails based on a csv file that contains Email, name, and company name (institution) 
of the receiver

Example of data.csv

| Email | Name | Institution |
|-------|------|-------------|
| lruiz@gmail.com | Luis Ruiz | Facebook |
| carl765@gmail.com | Carl Whole | Github |
| . | . | . |
| . | . | . |
| . | . | . |
| nancy987@outlook.com | Nancy Pill | Huawei |

Things to take into account
- A gmail account should be setting up (less secure apps access https://myaccount.google.com/lesssecureapps)
- Fill ```password``` and ```sender_email``` based on your gmail credentials
- ```text``` and ```html``` are the same text for two diffent formats. This helps the message to be displayed 
when the email administrator receiver has blocked access to mails with html content
- Load a csv file called data.csv with the format showed above
- Results.csv is the output file that adds the day and hour the email was sent (0 is there is any trouble when sending the email)
- Also fill ```message["Subject"]``` and ```message["From"]``` according to your preference
- Fill ```file``` based on the attachment file you want to send
- All of the files (data.csv and the attachment file) should be located in the same folder as emailsender.py

...Enjoy sending massive emails
