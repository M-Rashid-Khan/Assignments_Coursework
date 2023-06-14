### Purpose
The purpose of this project is to build a full data pipeline. Multiple input data sources may be explored. Data input will be monitored by logstash, converted and fed into elasticsearch. Visualizations of data in elasticsearch will then be explored in Grafana.

### Current Status
Data input in the form of multiple text files. Each file contains multiple events. Each event is a single line of JSON.

Logstash monitors files for updates and passes mutated data into Elasticsearch. Grafana takes Elasticsearch input and dashboards can be built.

When connecting using Grafana -  
- Run docker-compose (Grafana may throw a repeated error in the console until you are logged in. It goes away once you log in.)
- Go to localhost:3000
- Login with default user/password  admin/admin and then you have to change the password
- Click the settings icon on the left and the Configuration menu will come up
- Select Add datasource and pick Elasticsearch
- To configure Elasticsearch fill the following boxes:
    - URL: http://elasticsearch:9200
    - Index name: json
    - Pattern: No pattern
    - Time field name: pitime
    - ElasticSearch version: 7.10+
    - Click "Save & test"
- You should now be able to explore adding dashboards


### Next Steps:
- Grafana configuration file
- explore visualizations in Grafana
- explore different data inputs
