content = '''
<?xml version="1.0" encoding="UTF-8"?>
<account>
<type>service</type>
<name>web_master</name>
<uuid>64599677-b4a6-4fe7-8310-61af2050dca6</uuid>
<key>p@$$w0rd</key>
<salt>h@66yp0773R</salt>
</account>
'''

key = content[content.index('<key>')+5:content.index('</key>')]
print(key)
