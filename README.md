# PollutionTracker

This is a [Twitter bot](https://twitter.com/gachlilit) tracking pollution in Israel and posting when its values are abnormal.

## Operation

Upon operation, the code queries ```svivaaqm.net```'s API all stations in Israel 
for levels of 
1. NO2
2. SO2
3. Benzene

as detailed in ```conf.py``` and checks if the last hour's average is below what's 
recommended [by law](https://www.nevo.co.il/law_html/law00/77858.htm).

If an abnormality is found, an image is rendered using ```placid.app``` service
and posted to the Twitter account via Twitter's API.