# (Unofficial) Clemson Dining Alexa Skill
Find out what's on the menu at Clemson's dining halls.


<a href="https://www.amazon.com/gp/product/B07L342K1S">
    ![image](https://user-images.githubusercontent.com/10427974/49385079-7de8f780-f6ea-11e8-869e-eb74c0859c50.png)
</a>

### Awards

This project won `Best Software Hack` at the CUHackIt Hello World 2018 hackathon!  
[See this project on DevPost](https://devpost.com/software/clemson-dining-alexa-skill)

### What it does

You can ask Alexa about the overall menu for a campus dining location or for just a single station at a specific location.

![utterance_core_menu](https://user-images.githubusercontent.com/10427974/49389224-c527b600-f6f3-11e8-86c6-48894d9a2358.png)
![utterance_core_station_pasta](https://user-images.githubusercontent.com/10427974/49389225-c527b600-f6f3-11e8-97ba-817933fb5e64.png)
![utterance_schilletter_menu](https://user-images.githubusercontent.com/10427974/49389226-c527b600-f6f3-11e8-8f4a-fc1be9ac3130.png)
![utterance_schilletter_station_grill](https://user-images.githubusercontent.com/10427974/49389227-c527b600-f6f3-11e8-8209-e752ee2fed30.png)


#### Phrases
* Get the whole menu
  * `Alexa, ask Tiger Dining what does {dining_hall} have on the menu today.`
  * `Alexa, ask Tiger Dining what is {dining_hall} serving today`
* Get the menu for a specific station
  * `Alexa, ask Tiger Dining what does the {station} at {dining_hall} have today`
  * `Alexa, ask Tiger Dining what's at the {station} at {dining_hall}`
  * `Alexa, ask Tiger Dining what's on the {station} at {dining_hall}`

##### Dining Halls
Supports both `Core` and `Schilletter`.

##### Stations

<table>
  <tr>	<th>Stations at Core:</th>	<th>Stations at Schilletter:</th>	</tr>
  <tr>	<td>Deli</td>	<td>Fresh Focus</td>	</tr>
  <tr>	<td>Dessert</td>	<td>Deli</td>	</tr>
  <tr>	<td>Entree Station</td>	<td>Grill</td>	</tr>
  <tr>	<td>Grill</td>	<td>Pizza</td>	</tr>
  <tr>	<td>Lite-sy Corner</td>	<td>Salad Bar</td>	</tr>
  <tr>	<td>Mongolian Grill</td>	<td>Dessert</td>	</tr>
  <tr>	<td>Pasta</td>	<td>Mongolian</td>	</tr>
  <tr>	<td>Pizza</td>	<td>Saute</td>	</tr>
  <tr>	<td>Salad</td>	<td>Soup</td>	</tr>
  <tr>	<td>Soup</td>	<td>Taste of Home</td>	</tr>
  <tr>	<td></td>	<td>Vegetarian</td>	</tr>
</table>
