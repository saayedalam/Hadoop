## DATA622 HW #4
- Assigned on October 27, 2019
- Due on Nov 24, 2019 11:59 PM EST
- 17 points possible, worth 17% of your final grade

### Instructions:

Use the two resources below to complete both the critical thinking and applied parts of this assignment.

1. Listen to all the lectures in Udacity's [Intro to Hadoop and Mapreduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) course.  

2. Read [Hadoop A Definitive Guide Edition 4]( http://javaarm.com/file/apache/Hadoop/books/Hadoop-The.Definitive.Guide_4.edition_a_Tom.White_April-2015.pdf), Part I Chapters 1 - 3.

### Critical Thinking (10 points total)

Submit your answers by modifying this README.md file.

1. (1 points) What is Hadoop 1's single point of failure and why is this critical?  How is this alleviated in Hadoop 2?

**NameNode is Hadoop 1's single point of failure because it is the centerpiece of an HDFS file system. It keeps the directory tree of all files in the file system, and tracks where across the cluster the file data is kept. When the NameNode goes down, the file system goes offline.**  

**Hadoop 2.0 overcomes this by providing support for many NameNode. HDFS NameNode High Availability architecture provides the option of running two redundant NameNodes in the same cluster in an active/passive configuration with a hot standby.**  
**Active NameNode – It handles all client operations in the cluster.**  
**Passive NameNode – It is a standby namenode, which has similar data as active NameNode. It acts as a slave, maintains enough state to provide a fast failover, if necessary.**

2. (2 points) What happens when a data node fails?

**When a data node fails, the cluster continues normally because HDFS replicates the data nodes three times as its loaded. Therefore when a data nodes fail, the NameNode sees there is only 2 replication and it will rereplicate so it is back to having 3 replication.**

3. (1 point) What is a daemon?  Describe the role task trackers and job trackers play in the Hadoop environment.

**Daemons in computing terms is a process that runs in the background. Hadoop has five such daemons. They are NameNode, Secondary NameNode, DataNode, JobTracker, and TaskTracker. Each daemons runs separately in its cluster.**  

**JobTracker manages TaskTracker and distributes the work between mappers and reducer. TaskTracker administers the code (mapper and reducer tasks) on DataNodes.**

4. (1 point) Why is Cloudera's VM considered pseudo distributed computing?  How is it different from a true Hadoop cluster computing?

**Cloudera's VM is considered pseudo distributed computing because the full cluster is running only on one machine. It is different from a true Hadoop cluster computing. A Hadoop cluster computing is a set of loosely or tightly connected computers that work together to store and analyze huge amounts of unstructured data.**

5. (1 point) What is Hadoop streaming? What is the Hadoop Ecosystem?

**Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.** 

**Hadoop Ecosystem is a platform or a suite that provides various services to solve the big data problems. Some of the tools we have mentioned already such as HDFS and MapReducer.**

6. (1 point) During a reducer job, why do we need to know the current key, current value, previous key, and cumulative value, but NOT the previous value?

**During a reducer job, we need to know the current key, current value, previous key, and cumulative value, but NOT the previous value because in the Hadoop Reducer we do aggregation or summation sort of computation and the previous value is already calculated and stored as cumulative value.**

7. (3 points) A large international company wants to use Hadoop MapReduce to calculate the # of sales by location by day.  The logs data has one entry per location per day per sale.  Describe how MapReduce will work in this scenario, using key words like: intermediate records, shuffle and sort, mappers, reducers, sort, key/value, task tracker, job tracker.  

**This is how MapReduce will work in this scenario:  
Hadoop divides the job into tasks. There are two types of tasks:  
Map tasks (Splits & Mapping)   
Reduce tasks (Shuffling, Reducing)**  

**Splits - An input to a MapReduce job is divided into fixed-size pieces called input splits. Input split is a chunk of the input that is consumed by a single map.  
Mapping - In this phase data in each split is passed to a mapping function to produce output values. In our example, a job of mapping phase is to count a number of sales by location by day from input splits and prepare a list in the form of <location, day, frequency>.  
Shuffling - This phase consumes the output of Mapping phase. Its task is to consolidate the relevant records from Mapping phase output. In our example, the same location and day are grouped together along with their respective frequency.  
Reducing - In this phase, output values from the Shuffling phase are aggregated. This phase combines values from Shuffling phase and returns a single output value. In short, this phase summarizes the complete dataset. In our example, this phase aggregates the values from Shuffling phase i.e., calculates number of sales per store per day.**

**The complete execution process (execution of Map and Reduce tasks, both) is controlled by two types of entities:  
jobTracker - Acts like a master (responsible for complete execution of submitted job)  
taskTrackers - Acts like slaves, each of them performing the job.**

### Applied (5 points total)

Submit the mapper.py and reducer.py and the output file (.csv or .txt) for the first question in lesson 6 for Udacity.  (The one labelled "Quiz: Sales per Category")  Instructions for how to get set up is inside the Udacity lectures.  
