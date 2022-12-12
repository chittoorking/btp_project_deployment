# About the Project
## The Project is Digital Twin Manufacturing using data analytics
The code from data collection to the model building is present in the ipynb notebook in the Python code folder
### Walk through of the notebook
- We imported the necessary libraries
- Mount to the google drive 
- Change the path to the folder where the dataset is downlaoded in the drive
- Load the dataset in the mat format and convert it into csv format and load the dataframe
- In the dataframe the column names are actually the indexes and the indexes are the columns. We will transpose the DataFrame to make them proper.
- Rename the columns in the dataframe
- Synthetic data generation
- Exploratory data analytics(Histograms,Correlation analysis,Heatmaps)
- Outlier Detection and removal
- Model building for predicting final positions and velocities
- Model building for detecting anomaly along with addressing class imbalance problem
- Select the best model in terms of accuracy and F1 score( Decision Tree Classifier)
- Link to previous deployment on streamlit
# BTP Deployment

- First, using the Flask a simple Web Application was made.
- Downloaded a ubuntu virtual machine and installed docker using official documentation
- Used Docker to run the project.
```bash
docker build -t <name> . # This is the command to build the docker image from the Dockerfile.
docker run -d -p 5000:5000 <name> # To run the application in docker container.
```
