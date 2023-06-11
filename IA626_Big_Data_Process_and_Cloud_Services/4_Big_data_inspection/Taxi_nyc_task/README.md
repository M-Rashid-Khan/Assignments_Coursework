### rashidm-taxi dataset working

## Initials:
Uploading dataset to into the environment:

Note* (I have used [trip_data_7](https://clarksonmsda.org/datafiles/taxi_trips/trip_data_7.csv.zip) dataset for my project)
```python
import pandas as pd
data = pd.read_csv('trip_data_7.csv')
data.sample(10)
```


1. What datetime range does your data cover?  How many rows are there total?
- I can get number of rows in my dataset by: 
```python
len(data)
```
![Results](images\img2.png)

- To get datatime format (for pickup_datetime in data):

![date_time_format](images\img3.png)

- The format is %Y-%m-%d %H:%M:%S, so the accoding to pickup date time range for the data is: 
![date_time_range](images\img4.png)

2. What are the field names?  Give descriptions for each field.

<!---
- Following will print out all the field names in the first column of data
--->

![field_names](images\img5.png)

![fields_description](images\img6.png)

3. Give some sample data for each field.

| medallion| hack_license| vendor_id| rate_code| store_and_fwd_flag| pickup_datetime| dropoff_datetime| passenger_count| trip_time_in_secs| trip_distance| pickup_longitude| pickup_latitude| dropoff_longitude| dropoff_latitude|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9406D2C34715E1DA10AD4D4DDADF4DA5 | 0602DFD837433635FE860BDE2F14BC3A | VTS | 1 | NaN | 2013-07-01 01:47:00 | 2013-07-01 01:52:00 | 1 | 300 | 1.17 | -74.013229 | 40.714718 | -74.003494 | 40.725285 |
|73495B48481E673AD8D7578764C9EC98 | 66DA261DA2E0305435786C152085CCC2 | VTS | 1 | NaN | 2013-07-01 01:39:00 | 2013-07-01 01:52:00 | 1 | 780 | 4.17 | -73.980865 | 40.763947 | -73.933884 | 40.767677|
|85B6168FC88F4914E4741015B1678BF4 | C2DB36C1124AB69269DBE1D3D39D37DB | VTS | 1 | NaN | 2013-07-01 01:36:00 | 2013-07-01 01:50:00 | 1 | 840 | 2.98 | -74.007568 | 40.740898 | -73.980118 | 40.713985|


4. What MySQL data types / len would you need to store each of the fields? 
    - int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
    - Following shows the datatypes of data in csv file and those I will use for SQL injections: 

![dtypes_csv](images\img7.png)
    
| Fields | SQL Data Types |
| :---:   | :---: |
| medallion | varchar(50)  |
| hack_license | varchar(50) |
| vendor_id | varchar(5) |
| rate_code | int(10) |
| store_and_fwd_flag | bool |
| pickup_datetime | datetime |
| dropoff_datetime | datetime |
| passenger_count | int(10) |
| trip_time_in_secs | int(10) |
| trip_distance | Decimal(5,5) |
| pickup_longitude | Decimal(9,6) |
| pickup_latitude | Decimal(8,6) |
| dropoff_longitude | Decimal(9,6) |
| dropoff_latitude | Decimal(8,6) |

5. What is the geographic range of your data (min/max - X/Y)? 
    - Plot this (approximately on a [map](http://www.gps-coordinates.net/))
    
6. What is the average computed trip distance? (You should use [Haversine Distance](https://stackoverflow.com/a/4913653))
7. Draw a histogram of the trip distances binned anyway you see fit.
8. What are the distinct values for each field? (If applicable)
![distint_values](images\img8.png)

9. For other numeric types besides lat and lon, what are the min and max values?

10. Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)
11. Create a new CSV file which has only one out of every thousand rows.
12. Repeat step 9 with the reduced dataset and compare the two charts.

<!---
![ScreenShot](images/img1.png)
--->

<!---
This is how code can be displayed: 

```python
print("hello")

```
--->
