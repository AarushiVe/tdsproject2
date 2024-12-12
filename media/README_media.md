# Analysis Report

### Summary of the Dataset

The dataset, `media.csv`, contains information about various media items, comprising 2,652 rows and 8 columns. The columns provide details about the media items, including the date of release, language, type, title, creator, and ratings on overall quality, repeatability, and other attributes. 

### Key Insights

1. **Overall Distribution**:
   - The dataset has 2,652 entries, with a notable number of missing values, particularly in the 'by' column (262 missing values) and 'date' column (99 missing values). This indicates that some media items lack information about the creator and release date.

2. **Language and Type**:
   - There are 11 unique languages represented, with English being the most frequent (1,306 instances).
   - The dataset contains 8 different types of media, with 'movie' being the predominant type (2,211 instances).

3. **Rating Insights**:
   - The average overall rating is approximately 3.05 (out of 5), indicating a generally favorable perception.
   - The average quality rating is slightly higher at around 3.21, suggesting that while the overall experience is decent, the quality is perceived even better.
   - The repeatability rating averages at 1.49, implying that most media items are not frequently revisited or rewatched.

4. **Popular Titles and Creators**:
   - The title "Kanda Naal Mudhal" is the most frequently mentioned, appearing 9 times, while "Kiefer Sutherland" is the most prominent creator, credited with 48 works.

5. **Date Analysis**:
   - The date field has 99 missing values, which could skew any time-series analysis if not addressed. The most frequent date recorded is '21-May-06'.

### Recommendations

1. **Data Cleaning**:
   - Address the missing values in the 'date' and 'by' columns. Consider imputation methods or removing entries with excessive missing data, especially if the missing data is systematic.

2. **Detailed Exploration of Ratings**:
   - Conduct a deeper analysis of the ratings. Use visualizations like box plots to investigate the distribution of overall ratings compared to quality and repeatability. This can help identify any potential outliers or patterns over time.

3. **Investigate Language and Type Trends**:
   - Analyze how the popularity of different media types and languages has changed over time. This could be visualized through a time series analysis to uncover trends.

4. **Creator and Title Popularity**:
   - Create visualizations to show the top creators and titles within the dataset. This could help identify trends in content production and consumer preferences.

5. **Repeatability Improvement**:
   - Explore why repeatability ratings are low. This could involve surveys or analyzing the content of media items to discern what factors contribute to lower revisitation rates.

By implementing these recommendations and further exploring the data, valuable insights can be gained to enhance the understanding of media trends and improve future content strategies.

![Chart](./media_heatmap.png)
![Chart](./media_barplot.png)
