import pymysql.cursors
import numpy as np
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='',
                             password='',
                             db='NFL_Draft',
                             charset='utf8mb4',
			     local_infile=True,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
	cursor.execute("DROP TABLE `teams`")
	cursor.execute("DROP TABLE `trace`")
    	cursor.execute("CREATE TABLE `teams` (`index` INT, `team` varchar(255) NOT NULL, `OffRush` INT, `OffPass` INT, `DefRush` INT, `DefPass` INT, `OffRatio` FLOAT, `DefRatio` FLOAT, PRIMARY KEY(`team`)) ENGINE = memory;")
	cursor.execute("LOAD DATA LOCAL INFILE 'forServer.csv' INTO TABLE teams FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\n' IGNORE 1 LINES;")
	cursor.execute("CREATE TABLE `trace` (`index` INT, `OffYearRatioReg` FLOAT, `DefYearRatioReg` FLOAT, `Down` FLOAT, `p` FLOAT, `Intercept` FLOAT, `TimeInHalfReg` FLOAT, `DistanceReg` FLOAT, `ScoreDiffReg` FLOAT, `YardsToGoalReg` FLOAT) ENGINE = memory;")
	cursor.execute("LOAD DATA LOCAL INFILE 'trace.csv' INTO TABLE trace FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\n' IGNORE 1 LINES;")
except:
    print 'connection not made'

finally:
        connection.close()
