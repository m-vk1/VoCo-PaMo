# VoCo-PaMo
Voice Controlled-Parametric Modelling

---

_Requirements:_
* Dynamo file with parameter inputs from an excel sheet.*

  *Please make sure that the location of the excel sheet in Dynamo is the same as the location of the Excel sheet on your system. 

---

_Excel Sheet Requirements:_

The excel sheet needs to be formatted as shown in the image below.**

|![image](https://user-images.githubusercontent.com/119511990/217298639-8b09a24c-86e2-4bd5-b52c-5db6ffe38b52.png)|
|:--:|
|*Parameters in column A and values in column B*|
 
 **Please make sure that the excel sheet is formatted as shown in the image above. 

---
Upon running the python script, the following UI will open up. Once button 1 is clicked and a Dynamo file (that meets the requirements mentioned above) is selected, button 2 is activated.

![image](https://user-images.githubusercontent.com/119511990/222201768-a0ec378e-5a98-496d-b4fe-55229d8d6843.png)

If all the steps were followed as mentioned, upon loading the Dynamo file, the list of parametrs that can be changed with voice commands is shown below button 2 which is now activated and can be clicked before giving a voice command.

![image](https://user-images.githubusercontent.com/119511990/222205838-9ef481dc-25b7-4ae1-91a1-05e063cb9426.png)

|![image](https://user-images.githubusercontent.com/119511990/222206762-3f5bab41-225e-4b60-b05f-4c5d0aaa95db.png)|
|:--:|
|*Initial Dynamo file, where bridge height is 30*|


If the user's voice command is understood by the app, an audio message stating the new changes will be played followed by an update on the UI stating the change made to the parameter.

![image](https://user-images.githubusercontent.com/119511990/222203556-10cd2a93-8312-4fc3-86a2-79c2e9cab396.png)

|![image](https://user-images.githubusercontent.com/119511990/222206960-7062d27b-4753-44bc-9dcc-656e53fbc4a1.png)|
|:--:|
|*Updated Dynamo file, with new bridge height as 60*|

If the app fails to understand the user's voice command, the following screen is shown.

![image](https://user-images.githubusercontent.com/119511990/222205387-0cda04f2-1126-4b3f-9e63-aa9326c70c3b.png)

---

# Demonstration video

https://user-images.githubusercontent.com/119511990/223112367-48db5ae0-0ee1-4ac9-99d0-cfdc491e0b7b.mp4
