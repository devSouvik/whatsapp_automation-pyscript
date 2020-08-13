

#  step 1- -> pip install pywhatkit <- in your IDE terminal or if you are using anaconda notepad write -> conda install pywhatkit


import pywhatkit as kit


#  step 2 -> open whatsapp web in your preferred browser and be logged in with your whatsapp account

#  step 3-> schedule a message with a minumum time of 7 minutes from the execution of the script

#  step 4->  if you want to multiple messages from 1 script...don't forget to give  a time diff of minimum 5 minutes from the previous message....

#  fromat --->>> kit.sendwhatmsg("phone number with +91","text message ",hour(in 24 hrs format),minutes) 

#  example ->  kit.sendwhatmsg("+91xxxxxxxxxx","good night ",23,35)

