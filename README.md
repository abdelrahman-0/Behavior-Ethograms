## Behavior Ethograms
A GUI-based application for creating custom ethograms based on output from BORIS ([https://github.com/olivierfriard/BORIS](https://github.com/olivierfriard/BORIS)). Behaviors can be reordered, colored & grouped in the final ethogram.
<details>
<summary>Install</summary>

Clone repository & install conda environment:
```
git clone https://github.com/abdelrahman-0/Behavior-Ethograms.git
cd Behavior-Ethograms
conda env create -f enivornment.yml
```
</details>

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
<br>
<img src="UI Designs/screenshots/start.png" width="75%"/>
</li>
<br>
<li>
Select at least one subject to include in the final ethogram:
<br>
<br>
<img src="UI Designs/screenshots/subjects.png" width="35%"/>
</li>
<br>
<li>
Configure your behavior groups. The groups represent the labels on the y-axis in the final ethogram. In the next step, the single behaviors can be assigned to their respective groups:
<br>
<br>
<img src="UI Designs/screenshots/behavior_groups.png" width="60%"/>
</li>
<br>
<li>
Choose which behaviors to include & assign them to the respective groups. Behaviors belonging to the same group will show up on the same horizontal line in the ethogram:
<br>
<br>
<img src="UI Designs/screenshots/behaviors.png" width="75%"/>
</li>
<br>
<li>
Finally, you can further customize you plots using the matplotlib interface (set x-limits, rename axis labels, ...) & save your figure:
<br>
<br>
<img src="UI Designs/screenshots/final_plot.png" width="100%"/>
<br>
</li>
</ol>
</details>