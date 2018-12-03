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

![utterance_core_menu](https://user-images.githubusercontent.com/10427974/49389386-28194d00-f6f4-11e8-9f41-e0eb4bb72795.png)
![utterance_core_station_pasta](https://user-images.githubusercontent.com/10427974/49389387-28194d00-f6f4-11e8-9495-48ea3b570ff6.png)
![utterance_schilletter_menu](https://user-images.githubusercontent.com/10427974/49389388-28194d00-f6f4-11e8-9ce7-a3dede896f97.png)
![utterance_schilletter_station_grill](https://user-images.githubusercontent.com/10427974/49389389-28194d00-f6f4-11e8-9613-cfd558d149f4.png)


#### Phrases
* Get the whole menu
  * Alexa, ask Tiger Dining what does `{dining location}` have on the menu today.
  * Alexa, ask Tiger Dining what `{dining location}` is serving today
* Get the menu for a specific station
  * Alexa, ask Tiger Dining what the `{station}` at `{dining location}` is serving today.
  * Alexa, ask Tiger Dining what does the `{station}` at `{dining location}` have today
  * Alexa, ask Tiger Dining what's at the `{station}` at `{dining location}`
  * Alexa, ask Tiger Dining what's on the `{station}` at `{dining location}`

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
