# Project Overview
# Title: Updating the Industrial Classification of the Workforce in India

# 1. Problem Statement

Objecctive:
 - Classify businesses into appropriate categories based on industry names and worker demographics.

Challenges:

 - Handling missing or ambiguous data in industry names.

 - Clustering industries effectively with minimal supervision.

 - Building a predictive model with limited domain-specific features.

# 2. Tools Used

Python Libraries:

 - Pandas & NumPy: Data cleaning and preprocessing.

Scikit-learn: 
 - TF-IDF, clustering, and model building.

Matplotlib & Seaborn: 
 - Visualization and exploratory data analysis (EDA).

Machine Learning Models:

 - KMeans Clustering

 - Random Forest Classifier

# 3. Approaches

Step 1: Data Cleaning

 - Removed rows with missing or null "NIC Name."

Step 2: Feature Engineering

 - Applied TF-IDF (Term Frequency-Inverse Document Frequency) on industry names.

 - Extracted demographic-related numeric features.

Step 3: Clustering

 - Used KMeans clustering to group industries.

 - Manually mapped clusters to business categories.

Step 4: Model Building

 - Encoded categories into numerical values.

 - Split data into training and testing sets.

 - Trained a Random Forest Classifier to predict business categories.

# 4. EDA Insights

4.1 Worker Demographics:

Key Observations:

 - Male workers dominate most industries, but some clusters have balanced gender distribution.

 - Smaller industries often have high female worker representation.

4.2 Industry Clusters:

Key Observations:

 - Cluster 0: Agriculture-focused industries.

 - Cluster 1: Retail-heavy sectors with diverse demographic trends.

 - Cluster 2: Manufacturing-dominant with the highest number of workers.

4.3 Clustering Results:

 - Businesses could be categorized with moderate granularity based on textual and demographic data.

 - Manual mapping refined results further, especially in industries like "Poultry."

# 5. Outcomes

Results:

 - Achieved an accuracy of ~53% on test data.

 - Identified key areas for improvement, such as better feature selection and cluster refinement.


