# Live Plotter
This is a program that can plot up to four live graphs simultaneously. The program gets the data from databases that are provided by the user. The main purpose of the program is to plot live data streams from up to four different sources.

**Note**: Link for .exe format of the program: https://drive.google.com/drive/folders/1GgzdmUrE66nLKonim3NdTagEMYU6vBB5?usp=share_link

## Files
* **live_plotter.py**: That is the source code of the Live Plotter.
* **data_generator.py**: That is a Python program to generate live data. Thanks to this program, you can try the Live Plotter even if you do not have any live data.
* **metu.png**: That is an image file used in the GUI.
* **live_plotter.mp4**: That is a video that shows how the program works.

## How to Use
To use the program properly, first, you need live data streams. If you do not have any live data stream, you can run "data_generator.py." After giving the desired inputs to "data_generator.py,", you will have databases that the live data is inserted into. Now, you can run the Live Plotter. Initially, you have to select the number of graphs that the program is going to plot and the databases that the data will be gotten from. Then, you need to configure database settings. In this step, you need to select the table and columns including the live data to determine the location of the live data. Now, the program is ready. You can start the plotting process by clicking the plot button, or you can pause the live graphs by clicking the pause button. Also, you can fine-tune the graphs by adjusting the frequency and the number of data in a frame.

**Warning**: When closing the program, please use the exit button to close the database connections properly.

**Note**: You can watch "live_plotter.mp4" to see how the program works.
