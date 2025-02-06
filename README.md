# buzzline-04-josiah-randleman
## Task 1. Use Tools from Module 1 and 2

Before starting, ensure you have completed the setup tasks in <https://github.com/denisecase/buzzline-01-case> and <https://github.com/denisecase/buzzline-02-case> first. 
Python 3.11 is required. 

## Task 2. Copy This Example Project and Rename

Once the tools are installed, copy/fork this project into your GitHub account
and create your own version of this project to run and experiment with. 
Follow the instructions in [FORK-THIS-REPO.md](https://github.com/denisecase/buzzline-01-case/docs/FORK-THIS-REPO.md).

OR: For more practice, add these example scripts or features to your earlier project. 
You'll want to check requirements.txt, .env, and the consumers, producers, and util folders. 
Use your README.md to record your workflow and commands. 
    

## Task 3. Manage Local Project Virtual Environment

Follow the instructions in [MANAGE-VENV.md](https://github.com/denisecase/buzzline-01-case/docs/MANAGE-VENV.md) to:
1. Create your .venv
2. Activate .venv
3. Install the required dependencies using requirements.txt.

## Task 4. Start Zookeeper and Kafka (2 Terminals)

If Zookeeper and Kafka are not already running, you'll need to restart them.
See instructions at [SETUP-KAFKA.md] to:

1. Start Zookeeper Service ([link](https://github.com/denisecase/buzzline-02-case/blob/main/docs/SETUP-KAFKA.md#step-7-start-zookeeper-service-terminal-1))
2. Start Kafka ([link](https://github.com/denisecase/buzzline-02-case/blob/main/docs/SETUP-KAFKA.md#step-8-start-kafka-terminal-2))

---

## Task 5. Start a Basic (File-based, not Kafka) Sentiment Over Time Application

This will take two terminals:

1. One to run the producer which writes to a file in the data folder. 
2. Another to run the consumer which reads from the dynamically updated file. 

### Producer Terminal

Start the producer to generate the messages. 

In VS Code, open a NEW terminal.
Use the commands below to activate .venv, and start the producer. 

Windows:

```shell
.venv\Scripts\activate
py -m producers.project_producer_case
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.project_producer_case
```

### Consumer Terminal

Start the file-based consumer that will process sentiment scores and visualize them as a real-time animated line chart. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and start the consumer. 

Windows:
```shell
.venv\Scripts\activate
py -m consumers.project_consumer_josiahrandleman
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.project_consumer_josiahrandleman
```

## **Sentiment Over Time - Real-Time Visualization**  

### 🔹 **What This Consumer Does**  
This consumer processes real-time messages stored in a **dynamically updated file** and extracts key sentiment insights from them. Specifically, it:  
- **Reads and parses JSON messages** from a file that is continuously updated by the producer.  
- **Extracts sentiment scores** from each message, which indicates whether the message is positive, negative, or neutral.  
- **Retrieves timestamps** to maintain a chronological order of sentiments.  
- **Updates a real-time sentiment trend chart** to visually represent how sentiment evolves over time.  

By processing this data dynamically, the consumer provides a **continuous stream of emotional insights**, allowing users to observe shifts in mood and engagement trends.  

---

### 📊 **Insight Focus: Sentiment Trends Over Time**  
This visualization focuses on how **sentiments fluctuate** as new messages arrive. By tracking the **emotional tone of messages over time**, we can identify patterns such as:  
- Peaks in **positive sentiment**, indicating engaging or uplifting conversations.  
- Sudden drops in **negative sentiment**, which may signal user frustration or negative discourse.  
- Stable **neutral sentiment**, which suggests balanced communication.  

This insight is valuable for **businesses, social media analysts, and customer experience teams** who need to monitor trends in public opinion, customer feedback, or online discussions in real time.  

---

### 📈 **Chart Type: Real-Time Sentiment Line Chart**  
- **X-axis:** Represents **timestamps** of when messages were received.  
- **Y-axis:** Represents **sentiment scores**, ranging from **-1 (negative)** to **1 (positive)**.  
- **Red Line:** Depicts the **real-time trend of sentiment fluctuations** over time.  

The real-time sentiment line chart is particularly useful because it allows users to **quickly spot trends and patterns** in emotional engagement. A simple glance at the graph can reveal whether sentiment is improving, declining, or remaining stable.  

---

### 🎯 **Why Is This Visualization Interesting?**  
This real-time sentiment analysis is **insightful and actionable** for multiple reasons:  
- **Detects mood shifts in real-time** – Useful for tracking how conversations evolve over time.  
- **Identifies emerging sentiment patterns** – Helps businesses respond quickly to customer reactions.  
- **Supports live monitoring of online discussions** – Valuable for **social media managers, support teams, and analysts** tracking public sentiment.  
- **Enables trend-based decision-making** – Organizations can adjust their messaging or engagement strategies based on sentiment shifts.  

By leveraging this visualization, **businesses, analysts, and researchers** can gain meaningful insights into public perception, allowing them to take proactive steps in improving engagement and satisfaction.  


---


