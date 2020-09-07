# Log_Analysis
Log Analysis Project

This project contains application's logs and WorkPhase data. The goal of the project is analyzing and understanding the application's raw logs and answering the question.

Project tasks complexity will be increased due to the deep log analysis. Initial Part is just answering the task questions but there will be more later. (Creating database, analysing each phase, working with more data)

You could find detail informations of the documents which are given. At last, you could find the task questions.

# Data
With this task you are given two documents:
##	Appendix 1 – log.csv
*	Filtered outtake from an application’s logs.
*	Data involves a datetime in UTC and the log message.
*	The solution is used during the assembly and describes the thermal grease application process:
- A new product arrives;
-	The solution recognizes the product (based on image detection);
-	The system loads instructions;
-	The system initiates the preprogrammed process.
-	The product is released and process restarts;
##	Appendix 2 – WorkPhase.txt
*	The steps within the process are described with these states (work phases).
*	Positive outcome: PRODUCT_WORK_DONE
*	Negative outcome: ABORTING

##Additional information:
*	Factory operates in shifts which start from 7:30 and 19:30.
*	Factory is in Tallinn, Estonia.
*	Cycle time – time spent on each product

## Task Questions
The development team is optimizing the assembly process and is looking to answer these questions:
1.	How many products are assembled per shift?
2.	What’s the average cycle time?
3.	How much time does the application spend in each work phase?
