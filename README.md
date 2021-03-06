## Behavior Ethograms
A GUI-based application for creating custom ethograms based on output from BORIS ([https://github.com/olivierfriard/BORIS](https://github.com/olivierfriard/BORIS)). Behaviors can be reordered, colored & grouped in the final ethogram.

<br>
<p align="center">
<img src="UI Designs/screenshots/example_ethogram.png" width="85%"/>
</p>
<br>
<details>
<summary>Install</summary>

Clone repository & install conda environment:
```
git clone https://github.com/abdelrahman-0/Behavior-Ethograms.git
cd Behavior-Ethograms
conda env create -f environment.yml
```
</details>
<br>
<details open>
<summary>Run</summary>
<ol>
<li>
Activate conda environment & launch application:

```
conda activate behavior_ethograms
python start.py
```
</li>
<br>
<li>
Select the BORIS .csv file which contains behaviors, subjects and the start & stop times:

<br>
<p align="center">
<img src="UI Designs/screenshots/start.png" width="65%"/>
</p>
</li>
<br>
<li>
Select at least one subject to include in the final ethogram:

<br>
<p align="center">
<img src="UI Designs/screenshots/subjects.png" width="35%"/>
</p>
</li>
<br>
<li>
Configure your behavior groups. The groups represent the labels on the y-axis in the final ethogram. In the next step, the single behaviors can be assigned to their respective groups:

<br>
<p align="center">
<img src="UI Designs/screenshots/behavior_groups.png" width="60%"/>
</p>
</li>
<br>
<li>
Choose which behaviors to include & assign them to their respective groups. Behaviors belonging to the same group will show up on the same horizontal line in the ethogram. You can also set the x-limits and change the bar heights by clicking on <i>additional settings</i> :

<br>
<p align="center">
<img src="UI Designs/screenshots/behaviors.png" width="75%"/>
</p>
</li>
<br>
<li>
Finally, you can further customize your plots using the matplotlib interface (rename axis labels, set title, ...) & save your figure:

<br>
<p align="center">
<img src="UI Designs/screenshots/final_plot.png" width="85%"/>
</p>
<br>
</li>
</ol>
</details>
